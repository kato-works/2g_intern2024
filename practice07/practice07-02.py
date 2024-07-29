import time
from machine import Pin

led = None

def set_event(led_pin_no=2, button_pin_no=0):
    """
    PINにイベントを設定

    Parameters
    ----------
    led_pin_no : int
        LED割り当てピン
    button_pin_no : int
        BUTTON割り当てピン
    """
    global led
    led = Pin(led_pin_no, Pin.OUT)
    button = Pin(button_pin_no, Pin.IN)
    button.irq(trigger=Pin.IRQ_FALLING, handler=button_push) 


def button_push(pin):
    """
    BUTTONが押された際の処理、
    点灯していれば消灯、消灯していれば点灯する

    Parameters
    ----------
    pin : Pin
        イベントが発生したピン（ボタン）
    """
    print(f'PIN: {pin}')
    # 前回と異なる値を生成する
    value = (led.value() + 1) % 2
    led.value(value) 

if __name__ == "__main__":
    led_pin_no = 2
    button_pin_no = 0

    set_event(led_pin_no=2, button_pin_no=0)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # Ctl-Cによる中断を検出
        print("例外'KeyboardInterrupt'を捕捉")
        if led is not None:
            led.off()
