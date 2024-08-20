from machine import Pin
import time

"""
a -> 4
b -> 5
c -> 12
d -> 13
e -> 14
f -> 18
g -> 19
dp -> 25
"""
# a, b, c, d, e, f, g, dp
digits = {
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

pin_assign = [4, 5, 12, 13, 14, 18, 19, 25]

pins = []
for pin_no in pin_assign:
    pin = Pin(pin_no, Pin.OUT)
    pins.append(pin)

while True:
    for digit in '0123456789':
        print(digit)
        data = digits[digit]
        for i, pin in zip(data, pins):
            pin.value(i)
        time.sleep(0.2)

    