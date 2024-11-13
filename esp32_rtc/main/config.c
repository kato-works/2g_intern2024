#include <stdio.h>
#include <string.h>
#include "esp_log.h"
#include "config.h"

#define CONFIG_FILE_PATH "/sdcard/config.ini"

static const char *TAG = "CONFIG";

// config.iniファイルから設定を読み取る関数
bool read_config(config_t *config) {
    FILE *file = fopen(CONFIG_FILE_PATH, "r");
    if (file == NULL) {
        ESP_LOGE(TAG, "設定ファイルを開けませんでした");
        return false;
    }

    char line[128];
    while (fgets(line, sizeof(line), file) != NULL) {
        if (strncmp(line, "use_wifi=", 9) == 0) {
            config->use_wifi = (line[9] == '1');  // "use_wifi=1" なら true、"use_wifi=0" なら false
        } else if (strncmp(line, "ssid=", 5) == 0) {
            strcpy(config->ssid, line + 5);
            config->ssid[strcspn(config->ssid, "\r\n")] = 0;
        } else if (strncmp(line, "password=", 9) == 0) {
            strcpy(config->password, line + 9);
            config->password[strcspn(config->password, "\r\n")] = 0;
        } else if (strncmp(line, "timezone=", 9) == 0) {
            strcpy(config->timezone, line + 9);
            config->timezone[strcspn(config->timezone, "\r\n")] = 0;
        } else if (strncmp(line, "ntp_server=", 11) == 0) {
            strcpy(config->ntp_server, line + 11);
            config->ntp_server[strcspn(config->ntp_server, "\r\n")] = 0;
        }
    }

    fclose(file);
    ESP_LOGI(TAG, "設定が読み込まれました: use_wifi=%d, SSID=%s, Timezone=%s, NTP Server=%s",
             config->use_wifi, config->ssid, config->timezone, config->ntp_server);
    return true;
}
