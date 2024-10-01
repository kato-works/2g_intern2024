from machine import Pin
import time

"""
ピンのアサイン
a -> 4
b -> 5
c -> 12
d -> 13
e -> 14
f -> 18
g -> 19
dp -> 25
"""
# GPIOピンアサイン
PIN_ASSIGIN = [4, 5, 12, 13, 14, 18, 19, 25]

# 各数字のピンのON・OFF定義
# a, b, c, d, e, f, g, dp
DIGITS = {
    '0': [1, 1, 1, 1, 1, 1, 0, 0],
    '1': [0, 1, 1, 0, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1, 0],
    '3': [1, 1, 1, 1, 0, 0, 1, 0],
    '4': [0, 1, 1, 0, 0, 1, 1, 0],
    '5': [1, 0, 1, 1, 0, 1, 1, 0],
    '6': [1, 0, 1, 1, 1, 1, 1, 0],
    '7': [1, 1, 1, 0, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1, 0],
    '9': [1, 1, 1, 1, 0, 1, 1, 0],
}

# ピン出力の初期化
pins = []
for pin_no in PIN_ASSIGIN:
    pin = Pin(pin_no, Pin.OUT)
    pins.append(pin)

# 表示のループ
while True:
    # 0~9までの表示を繰り返す
    for digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]:
        # ピンのON・OFFを取得
        data = DIGITS[digit]
        print(f'{digit}: {data}')
        # 各ピンのON・OFFを設定
        for i, pin in zip(data, pins):
            pin.value(i)
        time.sleep(0.2)
