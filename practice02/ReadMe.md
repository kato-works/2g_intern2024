# IoT練習

## 02.オンボードのLEDを光らせてみよう

### １秒間隔で、オンボードのLEDを交互に表示してみよう。

オンボードのLEDのピンは"2"です。

### 以下を実行して結果を確認してみましょう

点灯する
```
from machine import Pin

# GPIO2に接続された内蔵LEDを制御するためのPinオブジェクトを作成
led = Pin(2, Pin.OUT)
led.on()  # LEDを点灯
```

```
from machine import Pin

# GPIO2に接続された内蔵LEDを制御するためのPinオブジェクトを作成
led = Pin(2, Pin.OUT)
led.value(1)  # LEDを点灯

print(f'LED:{led.value()}')  # 現在のピンの状態を表示
```

消灯する
```
from machine import Pin

led = Pin(2, Pin.OUT)
led.off()  # LEDを消灯
```

```
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(0)  # LEDを消灯

print(f'LED:{led.value()}')
```