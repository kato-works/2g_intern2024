#include "ds3231.h"
#include "esp_log.h"

static const char *TAG = "DS3231";

// I2Cの設定
#define I2C_MASTER_SCL_IO 22       // SCLピンのGPIO番号
#define I2C_MASTER_SDA_IO 21       // SDAピンのGPIO番号
#define I2C_MASTER_NUM I2C_NUM_0   // I2Cポート番号
#define DS3231_ADDR 0x68           // DS3231のI2Cアドレス

// BCDから10進数に変換する関数
static uint8_t bcd_to_dec(uint8_t val) {
    return ((val / 16 * 10) + (val % 16));
}

// 10進数をBCDに変換する関数
static uint8_t dec_to_bcd(uint8_t val) {
    return ((val / 10 * 16) + (val % 10));
}

// I2Cの初期化関数
void i2c_master_init() {
    i2c_config_t conf = {
        .mode = I2C_MODE_MASTER,
        .sda_io_num = I2C_MASTER_SDA_IO,
        .sda_pullup_en = GPIO_PULLUP_ENABLE,
        .scl_io_num = I2C_MASTER_SCL_IO,
        .scl_pullup_en = GPIO_PULLUP_ENABLE,
        .master.clk_speed = 100000
    };
    i2c_param_config(I2C_MASTER_NUM, &conf);
    i2c_driver_install(I2C_MASTER_NUM, conf.mode, 0, 0, 0);
}

// DS3231から時刻を取得する関数
void get_time_from_ds3231(struct tm *timeinfo) {
    uint8_t data[7];
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();

    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, (DS3231_ADDR << 1) | I2C_MASTER_WRITE, true);
    i2c_master_write_byte(cmd, 0x00, true);  // 先頭アドレスを指定
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, (DS3231_ADDR << 1) | I2C_MASTER_READ, true);
    i2c_master_read(cmd, data, 7, I2C_MASTER_LAST_NACK);
    i2c_master_stop(cmd);
    esp_err_t ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);

    if (ret == ESP_OK) {
        timeinfo->tm_sec = bcd_to_dec(data[0]);
        timeinfo->tm_min = bcd_to_dec(data[1]);
        timeinfo->tm_hour = bcd_to_dec(data[2] & 0x3F);
        timeinfo->tm_mday = bcd_to_dec(data[4]);
        timeinfo->tm_mon = bcd_to_dec(data[5] & 0x1F) - 1;
        timeinfo->tm_year = bcd_to_dec(data[6]) + 100;
        timeinfo->tm_wday = bcd_to_dec(data[3]) - 1;

        ESP_LOGI(
            TAG, 
            "DS3231から取得した時刻: %04d-%02d-%02d %02d:%02d:%02d",
            timeinfo->tm_year + 1900, 
            timeinfo->tm_mon + 1, 
            timeinfo->tm_mday,
            timeinfo->tm_hour, 
            timeinfo->tm_min, 
            timeinfo->tm_sec
        );
    } else {
        ESP_LOGE(TAG, "DS3231からの時刻取得に失敗しました: %s", esp_err_to_name(ret));
    }
}

// NTPから取得した時刻をDS3231に設定する関数
void set_time_to_ds3231(const struct tm *timeinfo) {
    uint8_t data[7];
    data[0] = dec_to_bcd(timeinfo->tm_sec);
    data[1] = dec_to_bcd(timeinfo->tm_min);
    data[2] = dec_to_bcd(timeinfo->tm_hour);
    data[3] = dec_to_bcd(timeinfo->tm_wday + 1);
    data[4] = dec_to_bcd(timeinfo->tm_mday);
    data[5] = dec_to_bcd(timeinfo->tm_mon + 1);
    data[6] = dec_to_bcd(timeinfo->tm_year - 100);

    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, (DS3231_ADDR << 1) | I2C_MASTER_WRITE, true);
    i2c_master_write_byte(cmd, 0x00, true); 
    i2c_master_write(cmd, data, 7, true);  
    i2c_master_stop(cmd);
    esp_err_t ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);

    if (ret == ESP_OK) {
        ESP_LOGI(TAG, "NTPで取得した時刻をDS3231に設定しました");
    } else {
        ESP_LOGE(TAG, "DS3231への時刻設定に失敗しました: %s", esp_err_to_name(ret));
    }
}

// I2Cデバイスをスキャンする関数
void i2c_scan() {
    ESP_LOGI(TAG, "I2Cデバイスをスキャン中...");
    for (int i = 1; i < 127; i++) {
        i2c_cmd_handle_t cmd = i2c_cmd_link_create();
        i2c_master_start(cmd);
        i2c_master_write_byte(cmd, (i << 1) | I2C_MASTER_WRITE, true);
        i2c_master_stop(cmd);
        esp_err_t ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
        i2c_cmd_link_delete(cmd);
        if (ret == ESP_OK) {
            ESP_LOGI(TAG, "デバイス発見: 0x%02X", i);
        }
    }
    ESP_LOGI(TAG, "I2Cスキャン完了");
}
