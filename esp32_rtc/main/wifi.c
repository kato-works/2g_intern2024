#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "esp_sntp.h"
#include "esp_wifi.h"
#include "esp_log.h"
#include "wifi.h"

static const char *TAG = "WIFI";


// Wi-Fi接続を初期化して接続
void wifi_connect(const config_t *config) {
    esp_netif_init();
    esp_event_loop_create_default();
    esp_netif_create_default_wifi_sta();

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&cfg);

    wifi_config_t wifi_sta_config = {};
    strncpy((char *)wifi_sta_config.sta.ssid, config->ssid, sizeof(wifi_sta_config.sta.ssid));
    strncpy((char *)wifi_sta_config.sta.password, config->password, sizeof(wifi_sta_config.sta.password));

    esp_wifi_set_mode(WIFI_MODE_STA);
    esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_sta_config);
    esp_wifi_start();

    ESP_LOGI(TAG, "Wi-Fi接続中...");
    esp_wifi_connect();
}


// Wi-Fi接続完了を待機する関数 (タイムアウト付き)
bool wait_for_wifi_connection(int timeout_sec) {
    ESP_LOGI(TAG, "Wi-Fi接続待機中...");

    int elapsed = 0;
    esp_err_t ret;
    esp_netif_ip_info_t ip_info;
    while (elapsed < timeout_sec) {
        ret = esp_netif_get_ip_info(esp_netif_get_handle_from_ifkey("WIFI_STA_DEF"), &ip_info);
        if (ret == ESP_OK && ip_info.ip.addr != IPADDR_ANY) {
            ESP_LOGI(TAG, "Wi-Fi接続完了: IPアドレス取得: %s", ip4addr_ntoa(&ip_info.ip));
            return true;
        }
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        elapsed++;
    }
    ESP_LOGW(TAG, "Wi-Fi接続がタイムアウトしました");
    return false;
}

// Wi-Fi接続を切断する関数
void wifi_disconnect() {
    esp_err_t ret;

    // Wi-Fi接続を切断
    ret = esp_wifi_disconnect();
    if (ret == ESP_OK) {
        ESP_LOGI(TAG, "Wi-Fiが切断されました");
    } else {
        ESP_LOGE(TAG, "Wi-Fi切断に失敗しました: %s", esp_err_to_name(ret));
    }

    // Wi-Fiの停止
    ret = esp_wifi_stop();
    if (ret == ESP_OK) {
        ESP_LOGI(TAG, "Wi-Fiモジュールが停止しました");
    } else {
        ESP_LOGE(TAG, "Wi-Fi停止に失敗しました: %s", esp_err_to_name(ret));
    }
}