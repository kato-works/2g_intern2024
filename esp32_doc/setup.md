# 開発環境のセットアップとESP32へのファームウエアの書き込み

## PCとの接続（ドライバのインストール）

1. ESP32のFirmwareをダウンロード
   - 本実習ではESP32_GENERIC-20240602-v1.23.0.binで動作確認を行っています
1. ESP32をPCにUSBケーブルで接続
1. Windowsの「デバイスマネージャ」を起動し「ポート(COMとLPT)」に「USB-SERIAL CH340 (COMXX) 」と表示されていることを確認
   - COMXXは各自で異なるので、メモしてください
   - <image src=",,/images/device_manager.png">
1. USB-SERIALの表示がない場合には、先述のCH340のドライバをインストールして再接続

## ファームウェアの書き込み

1. ThonnyをPCにインストール
1. Thonnyを起動して、上部メニューの「Tools」-「Options」を選択
1. 「Thonny Options」画面の、「Interpreter」のタブを開く
1. Which kind of interpreter から「MicroPython(ESP32)」を選択、Port WebREPLから、先ほどメモしたCOMの番号を選択
1. 「Install or Update MicroPython (esptool)」のリンクを選択
1. 「Install MicroPython (esptool)」のTarget portから、先ほどメモしたCOMの番号を選択
1. 下部の「≡」からSelect local MicroPython imageを選択し、先ほどダウンロードしたFirmwareを選択する。
1. 「Install」ボタンを押すと、書き込みがはじまる
1. 書き込みが完了したら、「Cancel」を押して「Install or Update MicroPython (esptool)」画面を閉じる
1. 「Thonny Options」画面の「OK」を押してオプション画面を閉じる

## プログラム実行の確認

1. Thonnyの上部の入力欄に、print('Hello')と入力し「F5」ボタンまたは緑の「Run」ボタンを押下
1. 下部の出力に"Hello"と表示されることを確認
