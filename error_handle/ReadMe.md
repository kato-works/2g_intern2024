# MicroPythonにおけるエラーのハンドリング

## 本練習の目的

- エラーを発生させてみる
- エラーハンドリングに慣れる

## MicroPythonにおけるエラーとは

MicroPythonのエラーは主に２つに分類されます。

- 構文エラー : Syntax Error
- 例外 : Exception

構文エラーはプログラムの記述方法の誤りがある場合に発生するエラーで、
例外は構文は正しいがプログラムの実行中に出るエラーです。

MicroPythonはエラーが出た場合に、プログラムの何行目で何のエラーが出たか（どう呼ばれたか）トレースバックという形で表示してくれます。本練習ではエラーを発生させて、その対応に慣れていきましょう。

初心者が良く遭遇するエラー

- [SyntaxError](#syntaxerror--構文エラー)
- [IndentationError](#indentationerror--インデントのエラー)
- [NameError](#nameerror--変数名関数名のエラー)
- [TypeError](#typeerror--型のエラー)
- [ValueError](#valueerror--値の型や数などのエラー)
- [ImportError](#importerror--ライブラリをインポートする際のエラー)
- [ZeroDivisionError](#zerodivisionerror--0で割り算を行った)

## エラーが発生したときの基本の"キ"

プログラミングをするうえで、エラーの対応は常について回る課題です。例外処理こそが本来のプログラミングの本質と言っても過言ではありません。

エラーハンドル（エラー対処）と、デバッグ（バグの発見と修正）に慣れていきましょう。

### エラーが発生したときの対応の流れ

- エラーの場所を特定する
- エラーの発生原因を特定する
- エラーを再現させ、原因が合っていることを確認する
- エラーの対処方法を検討する
  - 発生しないようにプログラムを変更する
  - 発生するものとして、発生した際の処理をプログラムに追加する
- エラーが再現しない（対処されている）ことを確認する

### 場所の特定の仕方

エラーにトレースバックが表示されている場合には、どのような順にプログラムが実行されエラーになったかが分かります。最終的にエラーが発生した場所が分かるだけなので、原因はここからさかのぼっていく必要があるかもしれません。

```text
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>   # line 2 と表記があるので、２行目でエラー
NameError: name 'Name' isn't defined
```

### 発生したエラーの内容の確認

どんなエラーが起きたのか、エラーの内容は何かが表示されます。
下記のエラー例であればエラーの種類は、"NameError"で、エラーの内容は"name 'Name' isn't defined"なので、「'Name'という名前が定義されていないよ」となります。

```text
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'Name' isn't defined   # NameErrorが発生
```

### 原因の追い込み（デバッグ）

エラーが発生したということは、値（変数）が想定外か、処理内容の記述が間違っているかどちらかです。print句で値を表示して原因を追い込んでいきましょう。

一般的にはこれをデバッグ文と呼びます。

悪いデバッグ文の例 : どこで何の値を表示しているのか出力から判断できない。

```python
value1 = 123
value2 = 456
print(value1, value2)
```

以下のように数字が表示されるだけなので、量が多くなるとどこの何の値かわからない。

```text
123 456
```

良いデバッグ文の例 : デバッグ文の場所・表示内容が明確（行数などは変更されるので記載しない方が良い）

```python
value1 = 123
value2 = 456
print(f'main.py onChangeValue(): value1={value1}, value2={value2}')
```

以下のように、変数value1,value2が表示されることを確認しましょう。

```text
MPY: soft reboot
main.py onChangeValue(): value1=123, value2=456
>>> 
```

> [!NOTE]
> 実際の製品などは、日付時刻付きでログと呼ばれる実行履歴を出力しており、モードを変更することでログの詳細度を変えられるようにしていることが多いです。（DEBUG, INFO, WORNING, ERROR, FATALの5段階で出力量を調整する）

## 以下を実行して結果を確認してみましょう

### SyntaxError : 構文エラー

構文エラーは様々な要因によって発生します。

- (), {}, "", '' などが正しく閉じられていない
- 間違えて全角のスペースを入れている
- 関数の定義に":"をつけ忘れている

構文エラーはケアレスミスですが、以下のような対策によって減らすことができます。

- (), {}, "", '' は、先頭を書いたら、中身を書く前に閉じる
- 全角文字は出来るだけ使わない、コメントも環境が許せば英語で書く

```python
print('Hello!)　　# コメント

def hello(message)
    print(message

hello('Hi!')
```

このようなエラーが表示されるはずです。これは、"line 1" 1行目にSyntaxErrorが含まれると教えてくれています。このプログラムには4つのSyntaxErrorを入れてあります。直してみましょう。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 1
SyntaxError: invalid syntax
>>> 
```

### IndentationError : インデントのエラー

MicroPythonはインデント（文頭の空白）が大切なプログラミング言語です。他の言語ではプログラム内のブロックを{}で表すことが多いですが、MicroPython/Pythonではスペースやタブでインデントを揃えることで同じブロックであることを表します。

※ 一般的にインデントは半角スペース2個もしくは4個です。

IndentationErrorは、インデントが正しくない場合に発生するエラーです。

```python
number = 10
  print(number)

def hello(message):
  message = message + " hello"
 print(message)

hello('indent!')
```

このようなエラーが表示されるはずです。エラー文言の後ろに詳細なメッセージが表示され、どのようにインデントが悪いかが読み取れます。"unexpected indent"であれば"予期せぬインデント"なので入るべきでないインデントが2行目にあるという意味です。他にも"unindent doesn't match any outer indent level"とあれば、インデントのレベルが前後であっていないということになります。2つのIndentationErrorを入れています。直してみましょう。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 2
IndentationError: unexpected indent
>>> 
```

### NameError : 変数名・関数名のエラー

NameErrorは、変数や関数名がプログラム上で存在しない場合に発生するエラーです。MicroPython/Pythonは大文字小文字を区別するプログラミング言語なので、大文字小文字の間違いや、スペルミスによって発生することが多いです。

```python
name = 'KATO-WORKS'
print(Name)

def hello(message):
    prin(message)

helo(name)
```

実行すると以下のようなエラーが表示されます。これは、プログラムの2行目に書かれた"Name"という名前がプログラム上に存在していないと教えてくれています。このプログラムには3つのNameErrorを入れています。直してみましょう。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'Name' isn't defined
```

### TypeError : 型のエラー

プログラミング言語には、型という概念があります。文字列、ブール（真偽値）、整数、実数などが存在しています。このうち、ブール・整数・実数は互いに計算可能ですが、文字列は計算が出来ないため発生することが多いです。

```python
a = 12
b = 'KATO'
c = 'WORKS'

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b + c)
print(f'{b} + {a}')
```

以下のようにエラーが表示されます。これは、'int'型（整数）と'str'型（文字列）を"__add__"(加算)出来ないと教えてくれています。いくつか計算式を書きましたが、計算可能な式が含まれています、それはどれでしょう。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
TypeError: unsupported types for __add__: 'int', 'str'
>>> 
```

### ValueError : 値の型や数などのエラー

ValueErrorはプログラム内で処理を行う場合に、値が処理可能な範囲外であったり、数が異なっていたりすると発生するエラーで、様々な発生パターンが存在します。

```python
number = int("123,456")
print(number)

a, b, c = [1, 2]  # 配列の中身をa, b, cに代入
```

エラーがこのように表示されたかと思います、" invalid syntax for integer with base 10"は10進数でない数字構文だと教えてくれています。2つのValueErrorを入れています。修正してみましょう。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid syntax for integer with base 10
>>> 
```

### ImportError : ライブラリをインポートする際のエラー

ImportErrorは、対応していないモジュールをインポートしようとした際に発生するエラーです。スペルミスや、ファームウェアのバージョン、ライブラリのインストールミスなど、様々な要因で発生します。

```python
import Time
from Machine import PIN

pin = Pin(2, Pin.OUT)
pin.on()
time.sleep(1)
pin.off()
```

以下のようなエラーが表示されます。これは1行目に記載された'Time'というライブラリがESP32上で見つからないと教えてくれています。エラーが出なくなるように修正してみましょう。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: no module named 'Time'
>>> 
```

### ZeroDivisionError : 0で割り算を行った

数字を0で割ると、無限大になってしまいます。Pythonでは数字の桁数に制限がないためメモリを無限に使ってしまうことになるので、ZeroDivisionErrorが発生します。

```python
a = 123
b = 0

print(a / b)
```

以下のように4行目で0による除算が行われたことが表示されます。

```text
MPY: soft reboot
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ZeroDivisionError: divide by zero
>>> 
```

プログラム上では、数字をチェックすることで発生を防ぐ必要があります。

```python
a = 123
b = 0

if(b == 0):
    print('bが0')
else:
    print(a / b)
```
