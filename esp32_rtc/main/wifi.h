#ifndef WIFI_H
#define WIFI_H

#include "config.h"

// Wi-Fi接続を初期化して接続
void wifi_connect(const config_t *config);

// Wi-Fi接続完了を待機する関数 (タイムアウト付き)
bool wait_for_wifi_connection(int timeout_sec);

// Wi-Fi接続を切断する関数
void wifi_disconnect();

#endif // WIFI_H