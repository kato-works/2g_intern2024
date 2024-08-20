from machine import Pin
import time

"""
ESP32 GPIO -----> DS (74HC595)
ESP32 GPIO -----> SH_CP (74HC595)
ESP32 GPIO -----> ST_CP (74HC595)

74HC595:
  Q0 ----[220Ω]-----> a
  Q1 ----[220Ω]-----> b
  Q2 ----[220Ω]-----> c
  Q3 ----[220Ω]-----> d
  Q4 ----[220Ω]-----> e
  Q5 ----[220Ω]-----> f
  Q6 ----[220Ω]-----> g
  Q7 ---------------> dp

7セグメントディスプレイ（共通カソード）:
  a ----> [220Ω] ----> Q0 (74HC595)
  b ----> [220Ω] ----> Q1 (74HC595)
  c ----> [220Ω] ----> Q2 (74HC595)
  d ----> [220Ω] ----> Q3 (74HC595)
  e ----> [220Ω] ----> Q4 (74HC595)
  f ----> [220Ω] ----> Q5 (74HC595)
  g ----> [220Ω] ----> Q6 (74HC595)
  共通カソード ----> GND
"""

button = Pin(0, Pin.IN)
led_pin = Pin(2, Pin.OUT)

# シフトレジスタのピン設定
data_pin = Pin(18, Pin.OUT)
latch_pin = Pin(19, Pin.OUT)
clock_pin = Pin(21, Pin.OUT)

# 数字と7セグメントの対応（共通カソード）
# dp, g, f, e, d, c, b, a
digits = {
    '0': [0, 0, 1, 1, 1, 1, 1, 1],
    '1': [0, 0, 0, 0, 0, 1, 1, 0],
    '2': [0, 1, 0, 1, 1, 0, 1, 1],
    '3': [0, 1, 0, 0, 1, 1, 1, 1],
    '4': [0, 1, 1, 0, 0, 1, 1, 0],
    '5': [0, 1, 1, 0, 1, 1, 0, 1],
    '6': [0, 1, 1, 1, 1, 1, 0, 1],
    '7': [0, 0, 0, 0, 0, 1, 1, 1],
    '8': [0, 1, 1, 1, 1, 1, 1, 1],
    '9': [0, 1, 1, 0, 1, 1, 1, 1],
}

running = False

def button_push(pin):
    global running
    if running == False:
        running = True
    else:
        running = False


button.irq(trigger=Pin.IRQ_FALLING, handler=button_push)  # 値が0->1になったら関数を呼び出し

# シフトレジスタにバイトを書き込み
def display_digit(digit, dp):
    data = digits[digit]
    data[0] = dp
    latch_pin.off()
    for i in data:
        clock_pin.off()
        # 下位ビットから処理されるので、dp,g,f,e,d,c,b,aの順に書き込む。
        data_pin.value(i)
        clock_pin.on()
    latch_pin.on()

index = 0
sleep_time = 0.05
while True:
    if running:
        led_pin.off()
        # print(f'digit : {digit}')
        digit = '0123456789'[index]
        display_digit(digit, 0)
        time.sleep(sleep_time/2)
        display_digit(digit, 1)
        time.sleep(sleep_time/2)
        index = index + 1
        if index >= len(digits):
            index = 0
    else:
        led_pin.on()
        time.sleep(sleep_time)

