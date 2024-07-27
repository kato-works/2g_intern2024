# IoT練習

## 01.Hello Worldと表示してみよう

### １秒間隔で、"Hello"と"World"を交互に表示してみよう。

サンプルを準備したので、自分のスキルに合わせて以下を学習しましょう。
- PRINT句の使い方
- スリープのさせかた
- ループ（WHILE句、FOR句）の使い方
- 変数の使い方
- 関数の作り方・使い方

### 以下を実行して結果を確認してみましょう

■ PRINT句:　シリアルに文字を表示する
```
print('Hello')
```

■ SLEEPの方法:　一定時間プログラム実行を停止する  
```
import time  # ライブラリのインポート

print('Hello')
time.sleep(1)
print('Hello!')
time.sleep_ms(500)
print('Hello!!')
```

■ WHILE句(Ctl+Cでプログラム実行の中断): 終了条件を決めて処理をループする
```
import time

while True:
  print('Hello')
  time.sleep(1)
```

■ FOR句: 実行回数を決めて処理をループする
```
import time

for i in range(5):
  print(f'Hello:{i}')
  time.sleep(1)
```

■ 変数: 値を入れたり取り出せたり出来る箱
```
message = 'Hello'
print(message)

message = message + '!'
print(message)
```

■ 関数: 処理をまとめて、再利用可能にする仕組み
```
def print_with_exclamation(message, count=3):
  print(message + '!' * count)

print('Hello')
```

