// ds3231.h

#ifndef DS3231_H
#define DS3231_H

#include <time.h>
#include "driver/i2c.h"

#define DS3231_ADDR 0x68           // DS3231のI2Cアドレス
#define I2C_MASTER_NUM I2C_NUM_0   // I2Cポート番号

// 初期化関数
void i2c_master_init();

// DS3231から時刻を取得する関数
void get_time_from_ds3231(struct tm *timeinfo);

// NTPで取得した時刻をDS3231に設定する関数
void set_time_to_ds3231(const struct tm *timeinfo);

// I2Cデバイスをスキャンする関数
void i2c_scan();

#endif // DS3231_H
