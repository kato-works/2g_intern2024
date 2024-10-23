import RPi.GPIO as GPIO
from hx711 import HX711

# ピンの設定
HX711_DT_PIN = 5  # DT: データ
HX711_SCK_PIN = 6  # SCK: シリアルクロック

# ライブラリを初期化
hx = HX711(dout=HX711_DT_PIN, pd_sck=HX711_SCK_PIN)

GPIO.setmode(GPIO.BCM)

# キャリブレーションの実行
def calibrate_load_cell():
    hx.set_reference_unit(1)
    hx.tare()

# ループして重量を表示
def main():
    calibrate_load_cell()

    try:
        while True:
            weight = hx.get_weight_mean(5)  # 5回サンプリングして平均を求める
            print(f"Weight: {weight}")
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
