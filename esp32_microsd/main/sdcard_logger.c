#include <stdio.h>
#include <string.h>
#include <time.h>
#include "esp_log.h"
#include "esp_vfs_fat.h"
#include "driver/sdspi_host.h"
#include "driver/spi_common.h"
#include "driver/spi_master.h"
#include "sdmmc_cmd.h"
#include "sdcard_logger.h"

#define MOUNT_POINT "/sdcard"

// SPIピンの設定
#define PIN_NUM_MISO 19
#define PIN_NUM_MOSI 23
#define PIN_NUM_CLK  18
#define PIN_NUM_CS   4  // CSピンをGPIO4に設定

static const char *TAG = "SD_CARD";
static sdmmc_card_t *card = NULL;  // SDカードの状態を保持

// SDカードのマウント関数
esp_err_t sdcard_mount(void) {
    esp_err_t ret;

    // 既存のバスを解放
    spi_bus_free(SPI2_HOST);

    spi_bus_config_t bus_cfg = {
        .mosi_io_num = PIN_NUM_MOSI,
        .miso_io_num = PIN_NUM_MISO,
        .sclk_io_num = PIN_NUM_CLK,
        .quadwp_io_num = -1,
        .quadhd_io_num = -1,
        .max_transfer_sz = 4000
    };

    // SPIバスの初期化
    ret = spi_bus_initialize(SPI2_HOST, &bus_cfg, SPI_DMA_CH_AUTO);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "Failed to initialize SPI bus");
        return ret;
    }

    sdmmc_host_t host = SDSPI_HOST_DEFAULT();
    host.slot = SPI2_HOST;

    sdspi_device_config_t slot_config = SDSPI_DEVICE_CONFIG_DEFAULT();
    slot_config.host_id = host.slot;
    slot_config.gpio_cs = PIN_NUM_CS;

    esp_vfs_fat_sdmmc_mount_config_t mount_config = {
        .format_if_mount_failed = false,
        .max_files = 5
    };

    // SDカードのマウント
    ret = esp_vfs_fat_sdspi_mount(MOUNT_POINT, &host, &slot_config, &mount_config, &card);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "Failed to mount filesystem.");
        spi_bus_free(SPI2_HOST);  // バスを解放して再試行の準備
        card = NULL;
    } else {
        ESP_LOGI(TAG, "SD card mounted successfully");
    }
    return ret;
}

// SDカードのアンマウント関数
void sdcard_unmount(void) {
    if (card != NULL) {
        esp_vfs_fat_sdcard_unmount(MOUNT_POINT, card);
        spi_bus_free(SPI2_HOST);
        card = NULL;
        ESP_LOGI(TAG, "SD card unmounted and SPI bus freed");
    }
}

// SDカードにログを出力する関数
void sdcard_log(const char *message) {
    if (card == NULL) {
        ESP_LOGW(TAG, "SD card not mounted. Attempting to remount...");
        if (sdcard_mount() != ESP_OK) {
            ESP_LOGE(TAG, "Failed to remount SD card.");
            return;
        }
    }

    // ログファイルを開く
    FILE *file = fopen(MOUNT_POINT"/log.txt", "a");
    if (file == NULL) {
        ESP_LOGE(TAG, "Failed to open log file for writing. Unmounting SD card.");
        sdcard_unmount();
        vTaskDelay(2000 / portTICK_PERIOD_MS);  // 再マウントまでの待機時間
        sdcard_mount();  // 再マウント試行
        return;
    }

    // タイムスタンプの取得
    time_t now;
    time(&now);
    struct tm *timeinfo = localtime(&now);
    char time_str[64];
    strftime(time_str, sizeof(time_str), "%Y-%m-%d %H:%M:%S", timeinfo);

    // ログを書き込む
    if (fprintf(file, "%s - %s\n", time_str, message) < 0) {
        ESP_LOGE(TAG, "Failed to write log message to file. Unmounting SD card.");
        fclose(file);
        sdcard_unmount();
        vTaskDelay(2000 / portTICK_PERIOD_MS);  // 再マウントまでの待機時間
        sdcard_mount();  // 再マウント試行
        return;
    }

    // ファイルを閉じる
    if (fclose(file) != 0) {
        ESP_LOGE(TAG, "Failed to close log file. Unmounting SD card.");
        sdcard_unmount();
        vTaskDelay(2000 / portTICK_PERIOD_MS);  // 再マウントまでの待機時間
        sdcard_mount();  // 再マウント試行
        return;
    }

    ESP_LOGI(TAG, "Logged: %s", message);
}
