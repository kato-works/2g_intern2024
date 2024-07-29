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

勘違いの内容に書いておくと、加藤製作所の建機がESP32で動いているわけではありません。

### ESP32のリファレンス

[参照](esp32_doc/ReadMe.md)

## 実習

### 実習に必要なツール・ファームなど

シリアルドライバイアは、接続した際にCOMポートに表示がされない場合にインストールしてください。（WindosではCOM、Macでは/dev/tty.*を確認）

- [Thonny](https://thonny.org/) Python IDE for beginners
- [FirmWare](https://micropython.org/download/ESP32_GENERIC/) ESP32 MicroPython FirmWare
- [CP210x USB Serial Driver](https://jp.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) シリアル接続ドライバ

### 利用するデバイス

サンプルプログラムでは、以下のデバイスを想定しています。

- [開発ボード ESP32 ESP-WROOM-32 WiFi Bluetooth (USB Type-C)](https://www.amazon.co.jp/gp/product/B0C1444DRX/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&th=1)
- [IRヒューマンセンサーAM312](https://www.amazon.co.jp/gp/product/B084VMYMFZ/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&th=1)
- ブレッドボード（ESP32-Devの幅が独特なので、通常の５穴のボードであれば２枚必要）
- LED（3.3Vで駆動する任意のLED１個）
- 抵抗器（3.3V電圧に応じたLEDに対する抵抗１個）
- ジャンパー線数本

### ESP32を使って実際のIoTセンサーデバイスを作成しよう。

課題をクリアして、自分でIoTデバイスを作れるようになろう！

- [01.Hello Worldと表示してみよう](practice01/ReadMe.md)
- [02.オンボードのLEDを光らせてみよう](practice02/ReadMe.md)
- [03.オンボードの静電容量センサーを読み込んでみよう](practice03/ReadMe.md)
- [04.オンボードの温度センサーを読み込んでみよう](practice04/ReadMe.md)
- [05.抵抗と電流、LEDと抵抗を接続して光らせてみよう](practice05/ReadMe.md)
- [06.人感センサーを接続して、状態をシリアルに表示しよう](practice06/ReadMe.md)
- [07.イベントハンドラを実装してみよう](practice07/ReadMe.md)
- [08.Wi-Fiに接続してデータを送信してみよう](practice08/ReadMe.md)
- [09.人がいたら、LEDを点灯して、サーバーに通知してみよう](practice09/ReadMe.md)
