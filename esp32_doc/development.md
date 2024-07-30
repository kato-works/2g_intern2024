# Thonny 開発チュートリアル

## はじめに

書いたコードは大事な財産なので、都度保存して消さないようにしましょう。
（保存する癖をつけることは、今後の社会生活でも重要です）

今日の研修用のフォルダを自分のPCの任意の場所に作成してください。

## Thonnyとは

Thonny は、初心者向けに設計された Python 用の無料のオープンソース統合開発環境です。エストニアのプログラマー、Aivar Annamaa によって作成されました。

機能は限定的ですが、Raspberry Pi / Arduino / ESP32 などのMicroPythonの開発によく用いられます。

## 表示の変更

デフォルトの表示だと非常にそっけなく、使いずらいのでファイルビューを追加することをお勧めします。

1. "View"から"Files"を選択しビューを追加
   - <image src="../images/thonny_dev_00.png" width="250px">
1. 左側のFilesビューで研修用に作成したフォルダを開く
   - <image src="../images/thonny_dev_01.png" width="350px">

## ソースコードの作成～実行

1. "File"から"New"を選択して、新規ソースファイルを作成
   - <image src="../images/thonny_dev_02.png" width="350px">
1. ソースコードを書いたら、保存ボタンを押下
   - ここでは仮に print("Hello KATO-WORKS") と書き込む
   - <image src="../images/thonny_dev_03.png" width="350px">
1. PC(This Computer)に保存するか、ESP32(MicroPython Device)に保存するか聞かれるので、"This Computer"を選択し、ファイル名を記入して保存を押下
   - <image src="../images/thonny_dev_04.png" width="350px">
   - <image src="../images/thonny_dev_05.png" width="350px">
1. ファイルビューに保存したファイルが表示され、編集エリアもファイル名が記載される。
   - <image src="../images/thonny_dev_06.png" width="350px">
1. 上部の緑のRUNボタンを押下することで、プログラムを実行することが出来る
   - 中断する場合には赤のSTOP/RESTARTボタンを押下
   - <image src="../images/thonny_dev_07.png" width="350px">

[トップへ戻る](../README.md)