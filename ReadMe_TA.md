# 講師準備編

2024年度実施インターンの準備をまとめて、以降に講師になる人がいた場合のためのメモ

## 準備物

- ESP-WROOM-32
  - ESP32の30PinでType-Cインタフェースのもの、時々オンボードのLEDがないタイプがあるので注意
- SAD-101
  - サンハヤトの6穴ブレッドボード、5穴のボードの場合にはESP32が幅広なので2枚連結させる必要がある。
  - https://shop.sunhayato.co.jp/products/sad-101
- PIR AM312
  - ミニ赤外線赤外線 モーションセンサー
- LED
- 抵抗200Ω程度
- ジャンパー線（オスオス、オスメス）
- USBケーブル（データ通信対応のもの）

## ストレッチ課題用センサー

- KEYESTUDIO センサーアソートキット センサモジュール スターター キット(keyestudio 48 in 1 sensor kit)
  - https://wiki.keyestudio.com/KS0349_Keyestudio_48_in_1_Sensor_Kit
  - https://www.amazon.co.jp/gp/product/B0CQJBQ4Y3
- 抵抗 1KΩ / 2KΩ

## 開発環境など

- Thonny : MicroPython開発環境（ファーム書き込みツール付）
  - https://thonny.org/ 
- Fritzing : ブレッドボード回路図作成ツール
  - 有償版 https://fritzing.org/
  - OSS版 https://github.com/fritzing/fritzing-app/releases/tag/CD-548
  - 今回の実習の部品 [.fzpzファイル](images/fritzing)
 
## その他参照サイト

- ESP32 メーカーサイト
  - https://www.espressif.com/en/products/devkits/esp32-devkitc
- ESP32 Micropython リファレンス
  - 英語 : https://docs.micropython.org/en/latest/esp32/quickref.html
  - 日本語(ちょっと情報が古い) : https://micropython-docs-ja.readthedocs.io/ja/latest/esp32/quickref.html
- SORACOM IoT DIY レシピ : ESP32に限らずIoTのDIY事例集
  - https://soracom.jp/iot-recipes/
