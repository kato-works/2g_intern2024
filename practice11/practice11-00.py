from machine import Pin, PWM
import time

# GPIOピンの番号を指定
led_pin = 13

# Pinオブジェクトを作成
led = Pin(led_pin, Pin.OUT)

# PWMオブジェクトを作成
pwm = PWM(led)

# PWMの周波数を設定（例: 500Hz）
pwm.freq(20)

duty = 256

# 25%デューティサイクル
pwm.duty(duty)