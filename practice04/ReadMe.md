# IoT練習

## 04.オンボードの温度センサーを読み込んでみよう

### １秒間隔で、温度を表示してみよう

ESP32は内部温度を測定できるので、温度を測定してみよう。華氏で値が返却されるので、華氏と摂氏を変換する関数を作ってみよう。

華氏を摂氏に変換するには32を引いてから 5/9をかけます。

### 以下を実行して結果を確認してみましょう

華氏で温度を計測する
```
import esp32

temperature_fahrenheit = esp32.raw_temperature() # MCUの内部温度を華氏で読み取る
print(f'temperature_fahrenheit: {temperature_fahrenheit} ℉')
```

華氏と摂氏を変換する
```
def fahrenheit_to_celsius(temperature_fahrenheit):
    temperature_celsius = (temperature_fahrenheit - 32) * 5.0 / 9.0
    return int(temperature_celsius)

temperature_fahrenheit = 119
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
print(f'temperature_celsius: {temperature_celsius} ℃')
```