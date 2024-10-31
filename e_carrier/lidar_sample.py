"""
pyserial==3.5
rplidar-roboticia==0.9.5
"""

import os
import time
import threading
import traceback

import socketio
import numpy as np
from rplidar import RPLidar

SERIAL_PORT = os.environ.get('SERIAL_PORT', default='/dev/ttyUSB0')
LIDAR_MIN_DISTANCE = int(os.environ.get('LIDAR_MIN_DISTANCE', default='300'))
LIDAR_SIGNAL_INTERVAL = int(os.environ.get('LIDAR_SIGNAL_INTERVAL', default='200')) / 1000.0
LIDAR_BAUD_RATE = int(os.environ.get('LIDAR_BAUD_RATE', default='115200'))

LIDAR_MIN_DISTANCE = int(os.environ.get('LIDAR_MIN_DISTANCE', default='300'))
LIDAR_MAX_DISTANCE = int(os.environ.get('LIDAR_MAX_DISTANCE', default='5000'))

DEVICE_NAME_SPACE = os.environ.get('DEVICE_NAME_SPACE', default='/device')


class RPLiDARSocketIONamespace(socketio.ClientNamespace):

    def __init__(self, namespace, lidar_sensor):
        self.lidar_sensor = lidar_sensor
        super().__init__(namespace)

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_user_count_update(self, msg):
        print(f'RPLiDARSocketIONamespace:{msg}')
        self.lidar_sensor.set_client_cout(msg['user_count'])


class RPLiDARSensor:

    __instance = None
    __thread = None
    sio = None
    __con = None

    @staticmethod
    def get_instance(port: str = SERIAL_PORT, baudrate: int = LIDAR_BAUD_RATE, loop=None):
        if RPLiDARSensor.__instance is None:
            RPLiDARSensor(port=port, baudrate=baudrate)
        return RPLiDARSensor.__instance

    @staticmethod
    def set_instance(obj):
        RPLiDARSensor.__instance = obj

    @staticmethod
    def get_lidar_info():
        return RPLiDARSensor.__instance.lidar_info

    def __init__(self, port: str = SERIAL_PORT, baudrate: int = LIDAR_BAUD_RATE):

        RPLiDARSensor.set_instance(self)
        self.port = port
        self.baudrate = baudrate
        self._lidar = None
        self._iterator = None
        self.connect_lidar()
        self.client_count = 0
        self.running = True
        self.lidar_info = {}
        self.last_send_perf = 0
        RPLiDARSensor.__thread = threading.Thread(target=self.run)
        RPLiDARSensor.__thread.daemon = True
        RPLiDARSensor.__thread.start()

    def connect_lidar(self):
        print(f'connect_lidar')
        if self._lidar is not None:
            print(f'stop connection')
            # self._lidar.stop()
            self._lidar.disconnect()

        while True:
            try:
                self._lidar = RPLidar(self.port, baudrate=self.baudrate)
                self._iterator = self._lidar.iter_scans()
                __ = next(self._iterator)
            except Exception as e:
                print(e, traceback.format_exc())
                self._lidar.stop()
                self._lidar.disconnect()
                continue
            except ValueError as e:
                print(e, traceback.format_exc())
                self._lidar.stop()
                self._lidar.disconnect()
                continue

            break

    def set_client_count(self, count):
        self.client_count = count

    @staticmethod
    def _np_min(front):
        if len(front) == 0:
            min_front = 2000
        else:
            min_front = np.min(np.abs(front))
        return min_front

    def scan(self):
        """
        LiDARからデータの読み込み
        :return:
        """
        scan = next(self._iterator)

        # 定期的に信号を送り続ける
        start_time = time.perf_counter()
        if start_time - self.last_send_perf > LIDAR_SIGNAL_INTERVAL:
            # meas[0]: 強度
            # meas[1]: 角度 : 時計回り
            # meas[2]: 距離(mm)
            rad_dist = np.array([[np.radians((- meas[1]) % 360), meas[2]] for meas in scan])
            rad_dist = rad_dist[rad_dist[:, 1] >= LIDAR_MIN_DISTANCE]
            rad_dist = rad_dist[rad_dist[:, 1] <= LIDAR_MAX_DISTANCE]
            # print(f'offset[0]:{np.min(rad_dist[:,0])} ~ {np.max(rad_dist[:,0])}')
            # print(f'offset[1]:{np.min(rad_dist[:,1])} ~ {np.max(rad_dist[:,1])}')

            # front_angle = 20
            # front_angle_2 = 34
            # back_angle = 33
            # back_angle_2 = 54

            range_front = (rad_dist[:,0] >= np.radians(340)) | (rad_dist[:,0] <= np.radians(20))

            range_front_left = (rad_dist[:, 0] >= np.radians(20)) & (rad_dist[:,0] <= np.radians(34))
            range_front_right = (rad_dist[:, 0] >= np.radians(326)) & (rad_dist[:,0] <= np.radians(340))

            range_left = (rad_dist[:, 0] >= np.radians(34)) & (rad_dist[:,0] <= np.radians(126))
            range_right = (rad_dist[:, 0] >= np.radians(234)) & (rad_dist[:,0] <= np.radians(326))

            range_back_right = (rad_dist[:, 0] >= np.radians(126)) & (rad_dist[:,0] <= np.radians(147))
            range_back_left = (rad_dist[:, 0] >= np.radians(213)) & (rad_dist[:,0] <= np.radians(234))

            range_back = (rad_dist[:, 0] >= np.radians(147)) & (rad_dist[:,0] <= np.radians(213))

            front = rad_dist[range_front][:, 1]
            front_right = rad_dist[range_front_right][:, 1]
            front_left = rad_dist[range_front_left][:, 1]
            right = rad_dist[range_right][:, 1]
            left = rad_dist[range_left][:, 1]
            back_right = rad_dist[range_back_right][:, 1]
            back_left = rad_dist[range_back_left][:, 1]
            back = rad_dist[range_back][:, 1]

            min_front = RPLiDARSensor._np_min(front)
            min_front_right = RPLiDARSensor._np_min(front_right)
            min_front_left = RPLiDARSensor._np_min(front_left)
            min_back_right = RPLiDARSensor._np_min(back_right)
            min_back_left = RPLiDARSensor._np_min(back_left)
            min_back = RPLiDARSensor._np_min(back)

            lidar_min_info = {
                'front': min_front,
                'front_right': min_front_right,
                'front_left': min_front_left,
                'back_right': min_back_right,
                'back_left': min_back_left,
                'back': min_back,
            }
            # print(lidar_min_info)

            # X,Y座標へ変換（X=0,Y=1 方向が進行方向)
            x = np.sin(-rad_dist[:,0]) * rad_dist[:, 1]
            y = np.cos(rad_dist[:,0]) * rad_dist[:, 1]
            r = rad_dist[:, 1]
            points = np.concatenate([[x], [y], [r]], axis=0).T
            points = points.astype(np.int64)
            #print('points', points)
            #print(points.shape)
            #print('range_front', range_front)
            #print(range_front.shape)
            # IndexError: boolean index did not match indexed array along dimension 0;
            # dimension is 394 but corresponding boolean dimension is 197

            self.lidar_info = {
                'front': points[range_front].T.tolist(),
                'front_right': points[range_front_right].T.tolist(),
                'front_left': points[range_front_left].T.tolist(),
                'right': points[range_right].T.tolist(),
                'left': points[range_left].T.tolist(),
                'back_right': points[range_back_right].T.tolist(),
                'back_left': points[range_back_left].T.tolist(),
                'back': points[range_back].T.tolist(),
            }
            # print('lidar_info', len(json.dumps(self.lidar_info)))

            if self.client_count > 0:
                # print(lidar_min_info)
                RPLiDARSensor.sio.emit('_lidar_min_info', lidar_min_info, namespace=DEVICE_NAME_SPACE)
                RPLiDARSensor.sio.emit('_lidar_info', [], namespace=DEVICE_NAME_SPACE)

            self.last_send_perf = start_time

    def run(self):
        """
        起動時にスレッドとして実行
        :return:
        """
        try:
            RPLiDARSensor.sio = socketio.Client()
            RPLiDARSensor.connect_io()
        except Exception as e:
            print(e, traceback.format_exc())

        while self.running:
            # print(f'loop:{start_time}')
            try:
                self.scan()
            except Exception as e:
                print(e, traceback.format_exc())
                # RPLiDARSensor.connect_io()
                self.connect_lidar()
            except ValueError as e:
                print(e, traceback.format_exc())
                # RPLiDARSensor.connect_io()
                self.connect_lidar()

        self._lidar.stop()
        self._lidar.disconnect()

    def set_client_cout(self, count):
        self.client_count = count

    @staticmethod
    def connect_io():
        if RPLiDARSensor.sio is not None:
            RPLiDARSensor.sio.disconnect()

        while True:
            try:
                RPLiDARSensor.sio.register_namespace(RPLiDARSocketIONamespace(DEVICE_NAME_SPACE, RPLiDARSensor.__instance))
                RPLiDARSensor.sio.connect('ws://localhost:8081', namespaces=[DEVICE_NAME_SPACE])
            except Exception as e:
                print(e, traceback.format_exc())
                time.sleep(1)

            if RPLiDARSensor.sio.connected:
                break


class DummyRPLiDARSensor(RPLiDARSensor):

    __instance = None

    @staticmethod
    def get_instance(port: str = SERIAL_PORT, baudrate: int = LIDAR_BAUD_RATE, loop=None):
        if DummyRPLiDARSensor.__instance is None:
            DummyRPLiDARSensor(port=port, baudrate=baudrate)
        return DummyRPLiDARSensor.__instance

    def __init__(self, port: str = SERIAL_PORT, baudrate: int = LIDAR_BAUD_RATE):

        DummyRPLiDARSensor.__instance = self
        RPLiDARSensor.set_instance(self)

        self.client_count = 0
        self.running = True
        self.lidar_info = {}

        RPLiDARSensor.__thread = threading.Thread(target=self.run)
        RPLiDARSensor.__thread.daemon = True
        RPLiDARSensor.__thread.start()

    def set_client_cout(self, count):
        self.client_count = count

    def scan(self):
        """
        LiDARからデータの読み込み
        :return:
        """

        lidar_min_info = {
            'front': 1000,
            'front_right': 1000,
            'front_left': 1000,
            'back_right': 1000,
            'back_left': 1000,
            'back': 1000,
            'time': time.time(),
        }

        self.lidar_info = {
            'front': [[],[],[]],
            'front_right': [[],[],[]],
            'front_left': [[],[],[]],
            'back_right': [[],[],[]],
            'back_left': [[],[],[]],
            'back': [[],[],[]],
            'time': time.time(),
        }
        time.sleep(1)
        if self.client_count > 0:
            RPLiDARSensor.sio.emit('_lidar_min_info', lidar_min_info, namespace=DEVICE_NAME_SPACE)
            RPLiDARSensor.sio.emit('_lidar_info', [], namespace=DEVICE_NAME_SPACE)


if __name__ == '__main__':
    obj = RPLiDARSensor.get_instance()
    while True:
        time.sleep(100)
