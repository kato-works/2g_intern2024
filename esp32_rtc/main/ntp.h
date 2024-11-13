#ifndef NTP_H
#define NTP_H

#include "config.h"

bool obtain_time_from_ntp(const config_t *config, struct tm *timeinfo);

void set_time_to_esp32(const struct tm *timeinfo);

#endif // NTP_H