#include <stdio.h>
#include <driver/twai.h>
#include <driver/gpio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include "esp_err.h"

#define CAN_TX_GPIO GPIO_NUM_27 // TX pin (D4)
#define CAN_RX_GPIO GPIO_NUM_26 // RX pin (D5)
#define LED_GPIO GPIO_NUM_2    // Onboard LED GPIO pin (modify if necessary)

void init_can()
{
    twai_general_config_t g_config = TWAI_GENERAL_CONFIG_DEFAULT(CAN_TX_GPIO, CAN_RX_GPIO, TWAI_MODE_NORMAL);
    twai_timing_config_t t_config = TWAI_TIMING_CONFIG_500KBITS();
    twai_filter_config_t f_config = TWAI_FILTER_CONFIG_ACCEPT_ALL();

    if (twai_driver_install(&g_config, &t_config, &f_config) != ESP_OK) {
        printf("Failed to install TWAI driver\n");
        return;
    }
    if (twai_start() != ESP_OK) {
        printf("Failed to start TWAI driver\n");
    } else {
        printf("TWAI driver started\n");
    }
}

void init_led()
{
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT); // Set LED pin as output
}

void send_can_message()
{
    twai_message_t message;
    message.identifier = 0x123; // Set CAN ID
    message.flags = TWAI_MSG_FLAG_EXTD;
    message.data_length_code = 8;
    for (int i = 0; i < message.data_length_code; i++) {
        message.data[i] = i;
    }

    esp_err_t result = twai_transmit(&message, pdMS_TO_TICKS(1000));
    if (result == ESP_OK) {
        printf("Message sent\n");
        
        // Turn on LED
        gpio_set_level(LED_GPIO, 1);
        vTaskDelay(pdMS_TO_TICKS(1000)); // Keep LED on for 1 second

        // Turn off LED
        gpio_set_level(LED_GPIO, 0);
    } else {
        printf("Failed to send message, error code: 0x%x\n", result);
    }
}

void app_main()
{
    init_can();
    init_led();

    // Send a CAN message every 2 seconds
    while (1) {
        send_can_message();
        vTaskDelay(pdMS_TO_TICKS(2000));
    }
}
