#ifndef SDCARD_LOGGER_H
#define SDCARD_LOGGER_H

#include "esp_err.h"

esp_err_t sdcard_mount(void);
void sdcard_unmount(void);
void sdcard_log(const char *message);

#endif // SDCARD_LOGGER_H
