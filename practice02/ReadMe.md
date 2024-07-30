# IoT練習

## 02.オンボードのLEDを光らせてみよう

本練習の目的

- GPIOの出力を経験する
- タイマーや繰り返しを使いこなす

### １秒間隔で、オンボードのLEDを交互に表示してみよう

オンボードのLEDのピンは"2"です。

### 以下を実行して結果を確認してみましょう

点灯する

```python
from machine import Pin

# GPIO2に接続された内蔵LEDを制御するためのPinオブジェクトを作成
# 2番のピンを、出力（Pin.OUT）に設定する。
led = Pin(2, Pin.OUT)
led.on()  # LEDを点灯
```

```python
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(1)  # LEDを点灯

print(f'LED:{led.value()}')  # 現在のピンの状態を取得して表示
```

消灯する

```python
from machine import Pin

led = Pin(2, Pin.OUT)
led.off()  # LEDを消灯
```

```python
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(0)  # LEDを消灯

print(f'LED:{led.value()}')
```
