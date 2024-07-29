import time
from machine import Pin
from machine import TouchPad

def read_touch_pad(touch_pin, sleep_time_ms, threshold: int = 150):
    """
    指定されたスリープ間隔でTouchPadの静電容量を読み込む、
    中断されるまで繰り返す。

    Parameters
    ----------
    touch_pin : int
        設定対象のピン
    sleep_time_ms : int
        明滅間隔（ミリ秒）
    threshold : int
        タッチ判定の閾値（デフォルト150）
    """

    touch_pad = TouchPad(Pin(touch_pin))  # PIN32を、タッチパッドとして設定

    try:
        while True:
            touch_value = touch_pad.read()  # タッチパッドの静電容量の読み込み

            try:
                touch_value = touch_pad.read()
            except ValueError:  # ValueErrorが発生したら、-1を読み込み値に設定する
                touch_value = -1
            
            if touch_value == -1:
                print('Grouded...')
            elif touch_value <= threshold:
                print(f'Touched! ({touch_value})')
            else:
                print(f'No touch. ({touch_value})')

            time.sleep_ms(sleep_time_ms)
            
    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")

if __name__ == "__main__":
    SLEEP_TIME_MS = 200
    read_touch_pad(
        touch_pin=32,
        sleep_time_ms=SLEEP_TIME_MS,
    )