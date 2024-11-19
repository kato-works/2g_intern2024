# 講師準備編

2024年度実施インターンの準備をまとめて、以降に講師になる人がいた場合のためのメモ

## 講師スキルセット

- 基本的なPythonのプログラミング・デバッグが可能
- 簡単な電気回路の知識
- HTTPに関する知識と理解
- Linuxに関する知識（指示通りにセットアップが出来る）

## 2024年度インターン生による課題整理

- 良かったこと
  - 全体
    - 立川事業所だけでなく茨城工場や群馬の工場なども体験できたこと
  - プログラミング研修
    - 未経験でも入りやすいカリキュラムが用意されていた
    - センサ一覧があって、どのようなセンサなのか、ピン配列はどうなのか資料が準備されていた
    - オムニホイールの台車が手元で動かせたためトライ＆エラーがすぐにできる
    - ESP32を使用し様々なセンサを取り付け、結果を取得する場面でオムニホイールの台車がありトライ＆エラーが机上で可能だった
    - やってみたいことや使ってみたいセンサーなどを希望通りに準備された
- 改善点
  - 全体
    - 資材業務体験や製造業務体験を最後に詰めるのではなく分散してもらいたい
    - 直接関わる社員が少なかったので朝の挨拶やお昼など疎外感を感じた
    - 他の社員が今どのような仕事をして、クレーンのどこで利用されているか仕事内容について詳しく教えて欲しかった
    - 会議を見学としての参加をさせて欲しかった
  - プログラミング研修
    - 提供されるセンサが多すぎて組み合わせに迷った、事前に組み合わせのサンプルがあると良いと思った
    - 実際にクレーン等で使用しているセンサを使用してプログラミングを行ってみたかった
    - 台車を動かしたいタイミングと、動かせるタイミングがうまくかみ合わず、作業できな時間が発生した
    - オムニホイールだけではなく、台車と同じクローラーのミニチュアがあると、トライ＆エラーが行いやすかったかもしれない
    - ミニチュアを走行させるコースがあると良かった

## 岸本課題

- 良かった点
  - サイトを準備することで、1Wインターンはかなり手離れが良くなった
  - データ分析よりは、インターン生が退屈しないように見受けられた
  - 自分自身のESP32・センサーの勉強にもなった
- 悪かった点
  - 建機・クレーンの仕組みを教える時間がKATOに来たのだからもっと必要かもしれない
  - 社員紹介・仕事紹介の時間が取れると良かった
  - コミュニケーション・進捗・ゴールコントロール含め、面談などの時間を設けた方が良かった
  - 座学の時間（1Wインターンでは１回・1Mインターンでは2回のみ実施）をもう少し増やしてもよかった
  - サイトがある分、1Mインターンは早期にレベルが上がり、目標レベルが上がったため結局時間を多く費やすことになった
  - 自主性に任せたが黙々とサイトの課題を解く時間が長くなってしまい、コミュニケーションが減少した
  - 勉強に近すぎたので、実務に近い実装をしてもらってもよかった
  - Wi-Fi / HTML よりも、CANでデバイスを作ってもらうのもありだった
  - 台車を動かすのはハードルが高いので、もう少し改造できるようなサンプルを提供してもよかった

## 準備物

以下を買いそろえる、2024年度はESP32はインターン生にプレゼントした。

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
- 7セグ　LED
- シフトレジスタ
- コンデンサ
- NPN

## ストレッチ課題での実装例

- 赤外線センサーと超音波センサーで接近検知を行い、三色LEDを光らせる
- 人感センサーと温度センサーで、一定温度以上で人を検知するとLEDを点灯しサーバに通知

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
- OLEDディスプレイ
  - KeeYees OLEDディスプレイ OLEDモジュール 0.96インチ I2C 128X64 SSD1306 4ピン 白 Arduinoに対応 Raspberry Piに対応 3個入り
  - https://www.amazon.co.jp/gp/product/B08CTZVVLS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
- ロードセル
  - Youmile 4個DIY 110lbs 50KGハーフブリッジボディロードセル重量歪みセンサー抵抗+ HX711 ADモジュール
  - https://www.amazon.co.jp/dp/B084VNV4P6?ref=ppx_yo2ov_dt_b_fed_asin_title

## 追加で購入した台車

- オムニホイール台車
  - OSOYOO メカナムホイール ロボットカーシャーシ 4WD 80mm DC12Vモーター スマートロボット ミニ四駆 台車ロボットSTEM 組み立ておもちゃアルドゥイーノ Raspberry Pi micro bit適用 360°全方向移動Omni directional DIY【グリーンと黒はランダムに発送されます】
  - https://www.amazon.co.jp/dp/B07Z19HDXP?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1
- クローラ型台車
  - ロボット自動車シャーシ、エンコーダ付き直流モータ付きロボット戦車車、サスペンションダンパーシャーシ車Ardduion Rpi Microb Jetson Python DIY知能ロボット自動車全金属ロボット移動プラットフォーム軌道 単層
  - https://www.amazon.co.jp/dp/B0CW36K1J5?ref=ppx_yo2ov_dt_b_fed_asin_title
- モータードライバ
  - Ren He 3個セット L298N DCステッパ モータドライバ コントローラ ボード モジュール デュアル Hブリッジ 適用 ステッピングモーター ロボット スマートカー Arduinoと互換
  - https://www.amazon.co.jp/dp/B092VSCZ5H?ref=ppx_yo2ov_dt_b_fed_asin_title
  - 
