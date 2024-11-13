#include <time.h>
#include "esp_sntp.h"
#include "esp_log.h"
#include "config.h"

#include "freertos/task.h"

static const char *TAG = "NTP";

// NTPから時刻を取得し、成功時はtrue、失敗時はfalseを返す関数
bool obtain_time_from_ntp(const config_t *config, struct tm *timeinfo) {
    ESP_LOGI(TAG, "NTP同期を開始します");

    setenv("TZ", config->timezone, 1);  // タイムゾーン設定
    tzset();

    esp_sntp_setoperatingmode(SNTP_OPMODE_POLL);
    esp_sntp_setservername(0, config->ntp_server);
    esp_sntp_init();

    time_t now = 0;
    int retry = 0;
    const int retry_count = 20;
    const int retry_delay_ms = 5000;

    while (timeinfo->tm_year < (2024 - 1900) && ++retry < retry_count) {
        ESP_LOGI(TAG, "時刻を待機中 (%d/%d)...", retry, retry_count);
        vTaskDelay(retry_delay_ms / portTICK_PERIOD_MS);
        time(&now);
        localtime_r(&now, timeinfo);
    }

    if (timeinfo->tm_year < (2024 - 1900)) {
        ESP_LOGE(TAG, "NTPサーバからの時刻取得に失敗しました");
        return false;
    }

    ESP_LOGI(TAG, "NTPで取得した時刻: %04d-%02d-%02d %02d:%02d:%02d",
             timeinfo->tm_year + 1900, timeinfo->tm_mon + 1, timeinfo->tm_mday,
             timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec);

    return true;
}


// ESP32のシステム時刻を設定
void set_time_to_esp32(const struct tm *timeinfo) {
    time_t time = mktime((struct tm *)timeinfo);  // 変更不可なポインタキャスト
    struct timeval now_tv = {.tv_sec = time};
    settimeofday(&now_tv, NULL);

    char strftime_buf[64];
    strftime(strftime_buf, sizeof(strftime_buf), "%c", timeinfo);
    ESP_LOGI(TAG, "ESP32のシステム時刻を設定しました: %s", strftime_buf);
}
