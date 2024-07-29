import time
import network
import urequests

from machine import Pin

# サーバ設定
SSID = 'intern2024'       # Wi-FiのSSID
PASSWORD = 'pasword2024'  # Wi-Fiのパスワード
URL = 'http://192.168.4.1:5000/'  # POSTリクエストを送信するURL

# 入出力設定
led_sensor_detect = Pin(13, Pin.OUT)  # センサー反応中に点灯するLED
led_post_status = Pin(2, Pin.OUT)  # サーバPOST時に点灯するLED
sensor = Pin(4, Pin.IN)  # 人感センサー
button = Pin(0, Pin.IN)  # オンボードのボタン

# データ用
USRE_NAME = 'KATO-WORKS'

# グローバル変数
sensor_status = 0  # 前回割り込み時のセンサーの状態
count = 0   # センサーの反応回数

def sensor_triggerd(sensor_pin):
    """
    センサーが押されたら

    Parameters
    ----------
    sensor_pin : Pin
        トリガされたセンサーのピン
    """
    global sensor_status, count

    data = {
        'name': USRE_NAME,
    }
    status = sensor.value()
    if sensor_status != status:  # 前回のステータスと比較
        if status == 1:
            print('Sensor: ON')
            led_sensor_detect.on()
            count = count + 1
            data['AM312'] = 1
            data['AM312_SW'] = count
        else:
            print('Sensor: OFF')
            led_sensor_detect.off()
            data['AM312'] = 0
        response = post_data(URL, data)
        sensor_status = status

    return

def button_push(button_pin):
    """
    ボタンが押された際には、現在の状態を通知する

    Parameters
    ----------
    button_pin : Pin
        トリガされたボタンのピン
    """
    data = {
        'name': USRE_NAME,
        'AM312': sensor_status,
        'AM312_SW': count,
        'trigger': 'button',
    }
    response = post_data(URL, data)

    return

def connect_wifi(ssid, password):
    """
    Wi-Fiへ接続

    Parameters:
    ssid : str
        接続先のSSID
    password : str
        Wi-Fiのパスワード
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():  # 接続するまで待機
        print('Connecting to network...')
        time.sleep(1)
    print('Network connected:', wlan.ifconfig())
    return wlan

def post_success(interval=0.5):
    """
    POST成功（LEDを１回0.5秒点灯）
    """
    led_post_status.on()
    time.sleep(interval)
    led_post_status.off()

def post_failed(interval=0.1, count=3):
    """
    POST失敗（LEDを３回明滅）
    """
    for i in range(count):
        led_post_status.on()
        time.sleep(interval)
        led_post_status.off()
        time.sleep(interval)

def post_data(url, data):
    """
    WebサーバへデータのPOST実行

    Parameters:
    url : str
        送信するサーバのURL
    data : dict
        送信するデータのDict
    """
    try:
        response = urequests.post(url, json=data)
        print('Response status:', response.status_code)

        if response.status_code != 200:  # HTTPは200が成功のコード
            print(f'POST Failed.')
            post_failed()
            return None
        else:
            print('Response content:', response.text)
            post_success()
        return response.text
        
    except Exception as e:
        print(f'POST Failed. {e}')
        post_failed()
        return None


if __name__ == "__main__":
    # Wi-Fiに接続
    wlan = connect_wifi(SSID, PASSWORD)
    
    sensor.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=sensor_triggerd) 
    button.irq(trigger=Pin.IRQ_FALLING, handler=button_push)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
        led_sensor_detect.off()
        led_post_status.off()

    # WiFiから切断
    wlan.disconnect()
