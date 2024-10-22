# 電動キャリア仕様

## リモコン操作のシリアル信号

以下の式に従って、起動・前後・左右・スピードを指示する。

（起動信号は、通信開始時に必要）

signal = max(switch_boot, (switch_fb * 3 + switch_lr) * 6 + dial_speed)

- 起動 : switch_boot
  - BOOT : 54 (0x36)
- 前後 : switch_fb
  - NEUTRAL : 0
  - MOVE_BACKWARD : 1
  - MOVE_FORWARD : 2
- 左右 : switch_lr
  - NEUTRAL : 0
  - TURN_RIGHT : 1
  - TURN_LEFT : 2
- スピード : dial_speed
  - SPEED_LOW : 0
  - SPEED_HIGH : 5

### ex

操作を開始する際には、BOOTの0x36を送信

速度レベル1で、前方＋右旋回の場合には、0x2Bを送信

signal = (2 * 3 + 1) * 6 + 1 = 43 (0x2B)

## LiDAR仕様

## カメラ仕様

## ロードセル仕様

## 3色LED仕様

## 超音波センサ仕様
