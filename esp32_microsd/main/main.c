#include "esp_log.h"
#include "sdcard_logger.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

void app_main(void) {
    if (sdcard_mount() != ESP_OK) {
        ESP_LOGE("APP_MAIN", "Failed to mount SD card at startup.");
    }

    // ログを5秒おきに出力するループ
    while (1) {
        sdcard_log("This is a test log message.");
        vTaskDelay(5000 / portTICK_PERIOD_MS);
    }

    // SDカードのアンマウント
    sdcard_unmount();
}
