# 制御システム部２G　インターン　2024

## IoTって何？

"Internet of Things"の頭文字で、
従来はインターネットに接続していなかった様々なデバイスが、
ネットワークを通じてサーバーやクラウドに接続されて、情報交換をする仕組みを指します。

デバイスと一口にいっても、様々なものが現在では接続されています。
- センサー機器
- 駆動装置（アクチュエーター）
- 建機
- 住宅・建物
- 車
- 家電製品
- 電子機器

### 建機とデータを送受信できるとどんないいことがあるか考えてみよう

発展中の分野なので、様々なアイデアが生まれています。自分なりの答えを考えてみましょう。
- データを集められると何に使えるでしょう？
- データを建機に送れると何に使えるでしょう？
- データを欲しがっているのは誰でしょう？

## ESP32を使って、IoTの基本を勉強しよう

今回は、ESP-WROOM-32(ESP32)を使ってIoTの基本を勉強します。

"ESP32"は上海のEspressif Systems社が開発し台湾のTSMCが製造する、Wi-FiとBluetoothを搭載したSoCマイクロコントローラです。
動作温度が-40℃から＋125℃まで安定した動作が可能で、超低消費電力設計で、多様な機能を実装した安価な製品で、IoTギークに大人気な製品です。

似たような用途で、ArduinoやRaspberry Piといったものが存在するので、興味があれば調べてみましょう。

### ESP32のリファレンス

https://micropython-docs-ja.readthedocs.io/ja/v1.17ja/esp32/quickref.html

### ESP32に組み込まれているセンサー

- 温度センサー
- ホールセンサー（磁気）
- 静電容量タッチセンサー

### Hello Worldと表示してみよう

１秒間隔で、"Hello"と"World"を交互に表示してみよう。

### オンボードのLEDを光らせてみよう

### 抵抗と電流、LEDと抵抗を接続して光らせてみよう

### 人感センサーを接続して、状態をシリアルに表示しよう

### Wi-Fiに接続してデータを送信してみよう

### 人がいたら、LEDを点灯して、サーバーに通知してみよう

