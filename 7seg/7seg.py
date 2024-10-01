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

# Bootボタン
button = Pin(0, Pin.IN)
# オンボードLED
led_pin = Pin(2, Pin.OUT)
# シフトレジスタのピン設定
data_pin = Pin(18, Pin.OUT)  # データ
latch_pin = Pin(19, Pin.OUT)  # ラッチ
clock_pin = Pin(21, Pin.OUT)  # クロック

# 数字と7セグメントの対応（共通カソード）
# dp, g, f, e, d, c, b, a
DIGITS = {
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

# 対応する表示一覧
DIGITS_KEYS = list(DIGITS.keys())

running = False

def button_push(pin):
    global running
    if running == False:
        running = True
    else:
        running = False

# 割り込み処理の設定
button.irq(trigger=Pin.IRQ_FALLING, handler=button_push)  # 値が0->1になったら関数を呼び出し

# シフトレジスタにバイトを書き込み
def display_digit(digit: str, dp: int):
    data = DIGITS[digit]
    data[0] = dp
    # ラッチをOFFにしてデータを準備する
    latch_pin.off()
    for i in data:
        # clockをOFFにする
        clock_pin.off()
        # 下位ビットから処理されるので、dp,g,f,e,d,c,b,aの順に書き込む。
        data_pin.value(i)
        # clockがONになった時のデータを読み込む
        clock_pin.on()
    # ラッチがONになったタイミングでデータを反映
    latch_pin.on()

# 表示ループ
index = 0
sleep_time = 0.05
while True:
    if running:
        led_pin.off()
        # print(f'digit : {digit}')
        digit = DIGITS_KEYS[index]
        display_digit(digit, 0)
        time.sleep(sleep_time/2)
        display_digit(digit, 1)
        time.sleep(sleep_time/2)
        index = index + 1
        if index >= len(DIGITS_KEYS):
            index = 0
    else:
        led_pin.on()
        time.sleep(sleep_time)
