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

https://micropython-docs-ja.readthedocs.io/ja/v1.17ja/esp32/quickref.html

### ESP32に組み込まれているセンサー

- 温度センサー
- 静電容量タッチセンサー

### ESP32のピン一覧

ESP32では、40本のGPIOを持ち、プログラムから各ピンの入出力を設定することができ、入力の場合にはON/OFFの読み出しを、
出力の場合にはON/OFFの書き込みと読み出しができます。

各ピンからセンサーの状態を入力として読み込んだり、出力から周辺のデバイスを操作したりすることで、制御を実現します。

■　ピン機能一覧

| GPIO | 特殊機能	| コメント | | GPIO | 特殊機能	| コメント |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | BOOT/Flash Button | プルアップ内部抵抗 | | 16 |  | 内部プルアップ | 
| 1 | TXD0 | UART0送信 (デフォルト) | | 17 | 	|  | 
| 2 | BUILTIN LED | プルダウン内部抵抗 | | 18 |  |  | 
| 3 | RXD0 | UART0受信 (デフォルト) |  | 19 |  |  | 
| 4 |  |  |  | 21 |  |  | 	
| 5 |  | プルアップ内部抵抗 |  | 22 |  |  | 
| 6 | FLASH_CLK | フラッシュメモリ用 (使用しない) | | 23 |  |  | 
| 7 | FLASH_Q | フラッシュメモリ用 (使用しない) | | 25 | DAC1 | |  	
| 8 | FLASH_D | フラッシュメモリ用 (使用しない) | | 26 | DAC2 | | 	
| 9 | FLASH_HD | フラッシュメモリ用 (使用しない) | | 27 |  |  | 
| 10 | FLASH_WP | フラッシュメモリ用 (使用しない) | | 32 |  | ADC1_4 | 
| 11 |  | 使用しない | | 33 |  | ADC1_5 | 
| 12 | Boot Mode | プルダウン内部抵抗 | | 34 |  | 	入力専用、ADC1_6 | 
| 13 | 	|  | | 35 |  | 	入力専用、ADC1_7 | 
| 14 | 	|  | | 36 | (VP) | 	入力専用、ADC1_0 | 
| 15 | 	| プルダウン内部抵抗 | | 39 | (VN) | 	入力専用、ADC1_3 | 

■　ピンの配置

| Touch | SPI/DAC | ADC | IO | | IO | ADC | SPI/Serial  | I2C/Touch |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | EN | | GPIO23 | |  VSPID | | 
| | | A0(1-0) | GPI 36(VP) | | GPIO22 | | VSPIWP | SCL |
| | | A3(1-3) | GPI 39(VN) | | GPIO1 | | TXD0 | |
| | | A6(1-6) | GPI 34 | | GPIO3 | | RXD0 | |
| | | A7(1-7) | GPI 35 | | GPIO21 | | VSPIHD | SDA |
| T9 | | A4(1-4) | GPIO32 | | GPIO19 | | VSPIQ | |
| T8 | | A5(1-5) | GPIO33 | | GPIO18 | | VSPICLK | |
| | DAC_1 | A18(2-8) | GPIO25 | | GPIO5 | | VSPICS0 | |
| | DAC_2 | A19(2-9) | GPIO26 | | GPIO17 | | TXD2 | |
| T7 | | A17(2-7) | GPIO27 | | GPIO16 | | RXD2 | |
| T6 | HSPICLK | A16(2-6) | GPIO14 | | GPIO4 | A10(2-0) | HSPIHD | T0 |
| T5 | HSPIQ | A15(2-5) | GPIO12 | | GPIO2 | A12(2-2) | HSPIWP | T2 |
| T4 | HSPID | A14(2-4) | GPIO13 | | GPIO15 | A13(2-3) | HSPICS0 | T3 |
| | | | GND | | GND | | | |
| | | | 5V | | 3.3V | | | |

■　参考
- UART: 非同期式シリアルで２本で通信、機器間での通信に利用することが多い
  - 送信（TXD）
  - 受信(RXD)
- I2C: 同期式シリアルで２本で通信、１対多の通信を行なう。
  - SDA (Serial Data Line): データ転送のためのライン
  - SCL (Serial Clock Line): クロック信号のためのライン
- SPI: 同期式シリアルで4本で通信、１対多の通信を行なう。
  - 送信線　(SDO/MOSI[master]/MISO[Slave]) SPID
  - 受信線　(SDI/MISO[master]/MOSI[Slave]) SPIQ
  - クロック信号　(SCLK,CLK,SCK[Serial Clock]) SPICLK
  - スレーブ選択　(CS[Chip Select]/SS[Slave Select]/SYNC/ENABLE) SPICS0
  - 書き込み保護ライン(HSPI_WP / VSPI_WP)デバイスで書き込み保護機能を制御するために使用
  - 保持データライン（HSPI_HD / VSPI_HD）　デバイスを一時的に停止させるために使用さ


### 01.Hello Worldと表示してみよう

１秒間隔で、"Hello"と"World"を交互に表示してみよう。

### 02.オンボードのLEDを光らせてみよう

オンボードのLED

### 03.オンボードのセンサーを読み込んでみよう

### 04.抵抗と電流、LEDと抵抗を接続して光らせてみよう

### 05.人感センサーを接続して、状態をシリアルに表示しよう

### 06.イベントハンドラを実装してみよう

### 07.Wi-Fiに接続してデータを送信してみよう

### 07.人がいたら、LEDを点灯して、サーバーに通知してみよう

