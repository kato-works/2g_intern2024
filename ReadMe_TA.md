# 講師準備編

2024年度実施インターンの準備をまとめて、以降に講師になる人がいた場合のためのメモ

## 講師スキルセット

- 基本的なPythonのプログラミング・デバッグが可能
- 簡単な電気回路の知識
- HTTPに関する知識と理解
- Linuxに関する知識（指示通りにセットアップが出来る）

## 準備物

- ESP-WROOM-32
  - ESP32の30PinでType-Cインタフェースのもの、時々オンボードのLEDがないタイプがあるので注意
  - https://www.amazon.co.jp/gp/product/B0C1444DRX
  - @¥1,080
- SAD-101
  - サンハヤトの6穴ブレッドボード、5穴のボードの場合にはESP32が幅広なので2枚連結させる必要がある。
  - https://shop.sunhayato.co.jp/products/sad-101
  - @¥649-
- PIR AM312
  - ミニ赤外線赤外線 モーションセンサー
  - https://www.amazon.co.jp/gp/product/B084VMYMFZ/
  - @¥200-
- LED
  - 適当に複数色を準備
- 抵抗
  - 200Ω・1KΩ・2kΩ
  - https://www.amazon.co.jp/gp/product/B0CY56DP8Z
  - 抵抗600本とLED200個で￥915のセット
- ジャンパー線
  - ある程度本数があったほうが良いので、以下のようなセット(4人分)
  - https://www.amazon.co.jp/gp/product/B094ML2RLP
  - @¥200-
- Typ-C USBケーブル（データ通信対応のもの）

- Webサーバ動作用RaspberryPi + ディスプレイ
  - 2024年度のインターンではreTerminalを利用

## ストレッチ課題で出た質問・人気のセンサーなど

- 三色信号LEDが人気
  - 抵抗が入っているので、2重に入れる必要がないことを周知
- アナログ温度センサー
  - 0~100℃までリニアに測るが、10mV/℃で信号が返るので計算時に注意
  - 温度センサーは実際の温度の確認が難しいので、デバッグが難しい旨を伝える（ヒートガンで実施した）

## ストレッチ課題用センサー

- 振動センサー
  - アナログ信号処理を学ぶために利用、実際には電圧センサーと圧電素子
  - https://www.amazon.co.jp/gp/product/B084VNBV8J
  - @¥200-
- 音センサー
  - 特に課題には表記していないが、アナログ信号処理用として
  - https://www.amazon.co.jp/gp/product/B087RC7TMF
  - @¥140-
- I2Cセンサー
  - 以下はAHT20を搭載したI2Cセンサー、詳細はデータシートを参照
  - https://www.amazon.co.jp/gp/product/B0C6KBWRTZ
  - @¥200-
- KEYESTUDIO センサーアソートキット センサモジュール スターター キット(keyestudio 48 in 1 sensor kit)
  - https://wiki.keyestudio.com/KS0349_Keyestudio_48_in_1_Sensor_Kit
  - https://www.amazon.co.jp/gp/product/B0CQJBQ4Y3
  - @¥6,499-
- 分圧回路のための抵抗 1KΩ / 2KΩ
  - 分圧回路 : https://www.kairo-nyumon.com/resistor_divider.html

## 開発環境など

- Thonny : MicroPython開発環境（ファーム書き込みツール付）
  - https://thonny.org/ 
- Fritzing : ブレッドボード回路図作成ツール
  - 有償版 https://fritzing.org/
  - OSS版 https://github.com/fritzing/fritzing-app/releases/tag/CD-548
  - 今回の実習の部品 [.fzpzファイル](images/fritzing)
 
## その他、課題作成時の参照サイト

- ESP32 メーカーサイト
  - https://www.espressif.com/en/products/devkits/esp32-devkitc
- ESP32 Micropython リファレンス
  - 英語 : https://docs.micropython.org/en/latest/esp32/quickref.html
  - 日本語(ちょっと情報が古い) : https://micropython-docs-ja.readthedocs.io/ja/latest/esp32/quickref.html
- SORACOM IoT DIY レシピ : ESP32に限らずIoTのDIY事例集
  - https://soracom.jp/iot-recipes/
- Pythonの基礎学習
  - https://paiza.jp/works/python/trial
  - プログラミングとは
    - コンピュータを制御するプログラムをつくること
    - ソースコード：プログラムの記述内容
    - プログラミング言語：ソースコードを記述する専用言語
  - はじめてのプログラミング
    - print('Hello World')
  - 間違いやすいポイント
    - エラーを出してみる
    - 全角半角・大文字小文字
  - 数値を扱う
  - プログラムで計算する
  - 変数にデータを入れる
  - データを受け取る
  - 標準入力と標準出力
  - 条件に一致したら処理を実行する
  - 条件に合わせて処理を変える
  - 数値を分類する
  - 同じ処理を何度も繰り返す
  - 複数のデータを受け取る
  - 複数データを分類する

https://github.com/targetblank/micropython_ahtx0/blob/master/ahtx0.py

## 追加で購入したセンサー

- AHT20 温度・湿度センサー
  - I2Cを介して温度と湿度のデータを取得出来るセンサー
  - データレイアウト
    - 0: 0x00 (常に0)
    - 1: Status (ステータス)
    - 2: Humidity MSB (湿度上位バイト)
    - 3: Humidity LSB (湿度中位バイト)
    - 4: Humidity/Temperature Mixed (湿度下位/温度上位バイト)
    - 5: Temperature MSB (温度上位バイト)
    - 6: Temperature LSB (温度下位バイト)
  - コマンド
    - 初期化コマンド : 0xBE
      - センサーをリセットし、初期化
    - 測定開始コマンド : 0xAC 0x33 0x00
      - 測定を開始
- 振動センサー
  - PIN
    - S(AO): 振動量
    - +: 3.3V / 5V
    - -: GND
- コンデンサーマイク（LM393）
  - PIN
    - AO(AO): マイクのリアルタイム電圧信号
    - G: GND
    - +: 3.3V / 5V
    - DO(DO): 音の強度がしきい値に達すると、信号を出力
