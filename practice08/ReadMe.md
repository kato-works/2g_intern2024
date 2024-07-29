# IoT練習

## 08.Wi-Fiに接続してデータを送信してみよう

ESP32は、Wi-FiやBluetoothを搭載しており、簡単に他のデバイスと通信したり、
サーバと通信したりすることが出来ます。

### HTTPとは

**HTTP（HyperText Transfer Protocol）**は、ウェブブラウザとサーバー間でデータを送受信するためのプロトコルです。インターネット上でウェブページを表示するために使われる主要な通信手段です。

- クライアント：ウェブブラウザやモバイルアプリなど、ユーザーが操作する端末。
- サーバー：ウェブサイトのデータをホスティングしているコンピュータ。

### HTTPの基本動作

クライアントがリクエストを送信：ユーザーがウェブサイトにアクセスすると、クライアントがサーバーにリクエストを送ります。

サーバーがレスポンスを返す：サーバーはリクエストを受け取り、必要なデータを探し、クライアントにレスポンスを返します。

クライアントがデータを表示：クライアントは受け取ったデータを処理し、ユーザーに表示します。

### HTTPリクエストの種類

HTTPにはいくつかのリクエストメソッドがありますが、ここではGETとPOSTについて説明します。

#### GETリクエスト

GETリクエストは、サーバーからデータを取得するために使われます。主に以下の特徴があります：

- データの取得：特定のリソース（例：ウェブページやAPIからのデータ）を取得する際に使用されます。
- URLにデータを含む：リクエストする際のパラメータはURLに付加されます。例：https://example.com/api?name=John&age=30
- セキュリティ面：URLにデータが含まれるため、機密情報の送信には適しません。

#### POSTリクエスト

POSTリクエストは、サーバーにデータを送信するために使われます。主に以下の特徴があります：

- データの送信：フォームの送信やデータのアップロードなど、サーバーに新しいデータを送信する際に使用されます。
- 本文にデータを含む：送信するデータはリクエストの本文に含まれ、URLには表示されません。
- セキュリティ面：GETリクエストに比べて、データがURLに表示されないため、より安全にデータを送信できます。

### Wi-Fiに接続して、Webサーバに自分の名前をPOST（送信）してみよう

以下にテスト用のアクセスポイントを用意しました。(インターネットには接続していません。)

- SSID : intern2024
- PASSWORD : pasword2024

データを"http://192.168.4.1/"にPOSTすると、サーバ側に時刻とデータが表示されます。

サーバからESP32へは、投稿時刻が返却されます。

データはJSONと呼ばれる形式であれば、なんでも受け取る状態となっているので、好きに試して下さい。

※JSONは、データを簡単かつ効率的に交換するための軽量データ形式です。特にウェブアプリケーションでサーバーとクライアント間でデータを送受信するために広く使われています。

```json
{
  "name": "John",
  "age": 30,
  "isStudent": false
}
```

### 以下を実行して結果を確認してみましょう

Wi-Fiへの接続

```python
import time
import network

SSID = 'intern2024'       # Wi-FiのSSID
PASSWORD = 'pasword2024'  # Wi-Fiのパスワード

wlan = network.WLAN(network.STA_IF)  # ステーションインターフェース（STAモード）で初期化
wlan.active(True)  # チップを起動
wlan.connect(SSID, PASSWORD)  # Wi-Fiアクセスポイントへ接続
while not wlan.isconnected():  # 接続状態になるまでループして待機
    print('Connecting to network...')
    time.sleep(1)
print('Network connected:', wlan.ifconfig())
```

Webサーバへのデータの送信

```python
import urequests

url = 'http://192.168.4.1:5000/'  # POSTリクエストを送信するURL

data = {
    'name': 'KATO-WORKS',
}
response = urequests.post(url, json=data)
print('Response status:', response.status_code)
print('Response content:', response.text)
```
