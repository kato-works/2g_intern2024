# 電動キャリア仕様

## リモコン操作のシリアル信号

シリアル通信仕様

```python
# ポートは環境によって
port = '/dev/serial0'
baud_rate = 9600

ser = serial.Serial(port)
ser.baudrate = baud_rate
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 1
```

以下の式に従って、起動・前後・左右・スピードを指示する。

（起動信号は、通信開始時に必要）

```python
signal = max(switch_boot, (switch_fb * 3 + switch_lr) * 6 + dial_speed)
```

- 起動 : switch_boot
  - BOOT : 54 (0x36)
- 前後 : switch_fb
  - NEUTRAL : 0
  - MOVE_BACKWARD : 1
  - MOVE_FORWARD : 2
- 左右 : switch_lr
  - NEUTRAL : 0
  - TURN_RIGHT : 1
  - TURN_LEFT : 2
- スピード : dial_speed
  - SPEED_LOW : 0
  - SPEED_HIGH : 5

### ex

操作を開始する際には、BOOTの0x36を送信

```python
data = struct.pack('B', 0x36)
ser.write(data)
```

速度レベル1で、前方＋右旋回の場合には、0x2Bを送信

```python
switch_fb = 2
switch_lr = 1
dial_speed = 1
signal = (switch_fb * 3 + switch_lr) * 6 + dial_speed
#  signal = 43 (0x2B)
data = struct.pack('B', signal)
ser.write(data)
```

```python
import time
from machine import UART
import struct

# UARTの設定
uart = UART(1, baudrate=9600, tx=17, rx=16)  # 使用するピンやボーレートを適宜変更してください

# 信号値
NEUTRAL = 0
MOVE_FORWARD = 2
MOVE_BACKWARD = 1
TURN_LEFT = 2
TURN_RIGHT = 1
BOOT = 54
SPEED_LOW = 0
SPEED_HIGH = 5

def send_signal(commnd, duration):
    start = time.time()
    while time.time() - start < duration:
        date = struct.pack('B', commnd)
        print(f'CONNECT:{date}')
        uart.write(date)
        time.sleep(0.1)
        
def calc_signal(switch_fb, switch_lr, dial_speed):
    """
    PICの仕様に合わせてシリアルコードに変換
    :return:
    """
    # 右の３速：(0*3 + 1) * 6 + 3 = 9
    d = max(0, (switch_fb * 3 + switch_lr) * 6 + dial_speed)
    return d

def boot():
    send_signal(54, 2)

def stop():
    send_signal(0, 1)

# 接続
boot()
# 左旋回
send_signal(calc_signal(NEUTRAL, TURN_LEFT, SPEED_LOW), 1)
# 前進
send_signal(calc_signal(MOVE_FORWARD, NEUTRAL, SPEED_LOW), 1)
# 右旋回
send_signal(calc_signal(NEUTRAL, TURN_RIGHT, SPEED_LOW), 1)
# 後退
send_signal(calc_signal(MOVE_BACKWARD, NEUTRAL, SPEED_LOW), 1)
# 停止
stop()

```

## LiDAR仕様

## カメラ仕様

## ロードセル仕様

<image src='load_cell.jpg' width='500'>

- HX711
  - Python : pip install hx711==1.1.2.3
  - microPython : https://github.com/SergeyPiskunov/micropython-hx711
  - microPython : https://github.com/robert-hh/hx711

## 3色LED仕様

## 超音波センサ仕様
