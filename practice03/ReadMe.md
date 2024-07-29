# IoT練習

## 03.オンボードの静電容量センサーを読み込んでみよう

ESP32は静電容量の測定が可能なピンが存在します。人がピンに触ると、ピンにたまった電化が解放されるので数字が下がり、タッチセンサーとして利用することが出来ます。

### 0.2秒間隔で静電容量センサーの値を読み込み、タッチされたら数字がどのように変化するのか確認しましょう。

利用可能なピンは、ピン一覧のTouchの列に記載のあるピンですが、GPIO2は別の機能（LED）が割りあてられているので、別のピンを選びましょう。

- T0 : GPIO4
- T3 : GPIO15
- T4 : GPIO13
- T5 : GPIO12
- T6 : GPIO14
- T7 : GPIO27
- T8 : GPIO33
- T9 : GPIO32

センサーがグラウンドに繋がると、エラーが出るので対処したプログラミングが出来ると尚良いでしょう。
```
ValueError: Touch pad error
```

一定の値以下になったら、オンボードのLEDを点灯してみましょう。

### 以下を実行して結果を確認してみましょう

センサーの値を読み込む
```
from machine import Pin
from machine import TouchPad  # ライブラリからTouchPadを読み込む

pin = Pin(32)
touch_pad = TouchPad(pin)  # ピン32をタッチパッドとして設定する
touch_value = touch_pad.read()  # タッチパッドの静電容量を読み込む
print(f'Touch value:{touch_value}')
```

エラーハンドリング
```
from machine import Pin
from machine import TouchPad

touch_pad = TouchPad(Pin(2))
try:
    touch_value = touch_pad.read()
except ValueError:  # ValueErrorが発生したら、-1を読み込み値に設定する
    touch_value = -1
print(f'Touch value:{touch_value}')

```