#ifndef CONFIG_H
#define CONFIG_H

#include <stdbool.h>

// 定義情報の構造体
typedef struct {
    bool use_wifi;        // Wi-Fiを使用するかどうかを示すフラグ
    char ssid[32];        // Wi-FiのSSID
    char password[64];    // Wi-Fiのパスワード
    char timezone[32];    // タイムゾーン
    char ntp_server[64];  // NTPサーバーのアドレス
} config_t;

// 定義情報の読み込み関数プロトタイプ
bool read_config(config_t *config);

#endif // CONFIG_H
