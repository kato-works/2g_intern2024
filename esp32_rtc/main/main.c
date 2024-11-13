#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "config.h"
#include "ds3231.h"
#include "sdcard.h"
#include "wifi.h"
#include "ntp.h"

static const char *TAG = "MAIN";

// ログを1秒ごとにSDカードに書き込むタスク
void log_time_to_sdcard(void *pvParameter) {
    while (1) {
        time_t now;
        struct tm timeinfo;
        char time_str[64];
        
        // 現在の時刻を取得
        time(&now);
        localtime_r(&now, &timeinfo);
        strftime(time_str, sizeof(time_str), "%Y-%m-%d %H:%M:%S", &timeinfo);

        // SDカードにログ出力
        sdcard_log(time_str);
        
        vTaskDelay(1000 / portTICK_PERIOD_MS);  // 1秒ごとに実行
    }
}

// 時刻設定関連
void set_esp32_rtc(config_t *config) {
    struct tm timeinfo = {0};
    if (config->use_wifi) {
        // Wi-Fi経由でNTPから時刻を取得
        wifi_connect(&config);
        // Wi-Fi接続完了を待機 (タイムアウトを30秒に設定)
        if (wait_for_wifi_connection(30)) {
            // NTPから時刻を取得
            if (!obtain_time_from_ntp(&config, &timeinfo)) {
                // NTP取得失敗時にDS3231から時刻を取得してESP32に設定
                get_time_from_ds3231(&timeinfo);
            }
        } else {
            // Wi-Fi接続に失敗した場合にDS3231から時刻を取得して設定
            get_time_from_ds3231(&timeinfo);
        }
        wifi_disconnect();
    } else {
        // DS3231に設定された時刻を使用
        get_time_from_ds3231(&timeinfo);
    }
    // ESP32に時刻を設定
    set_time_to_esp32(&timeinfo);
}


void app_main() {
    // ESP32のNVPの初期化
    nvs_flash_init();
    // IC2の初期化
    i2c_master_init();
    // i2c_scan();
    // SDカードのマウント
    sdcard_mount();

    // 設定ファイルの読み込み
    config_t config = {};
    if (read_config(&config)) {
        
        // 時刻の設定
        set_esp32_rtc(&config);

        // ログ書き込みタスクの開始
        xTaskCreate(&log_time_to_sdcard, "log_time_to_sdcard", 4096, NULL, 5, NULL);

    } else {
        ESP_LOGE(TAG, "設定の読み込みに失敗しました");
    }
}
