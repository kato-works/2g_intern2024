from machine import Pin
from hx711 import HX711
import time

# Define the HX711 pins
HX711_DT_PIN = 5  # Change this to your actual DOUT pin
HX711_SCK_PIN = 18  # Change this to your actual SCK pin

# Create an instance of HX711
hx = HX711(Pin(HX711_DT_PIN), Pin(HX711_SCK_PIN))

# Calibrate the load cell (adjust based on your calibration)
def calibrate_load_cell():
    hx.set_scale(1)  # Adjust calibration value based on your setup
    hx.tare()  # Reset tare for the load cell

# Main function
def main():
    calibrate_load_cell()

    try:
        while True:
            weight = hx.read_average(5)  # Read average weight over 5 samples
            print(f"Weight: {weight}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped")

if __name__ == "__main__":
    main()
