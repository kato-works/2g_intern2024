#include <stdio.h>
#include <driver/twai.h>
#include <driver/gpio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/queue.h>

#define CAN_TX_GPIO GPIO_NUM_27 // TX pin (27)
#define CAN_RX_GPIO GPIO_NUM_26 // RX pin (26)
#define LED_GPIO GPIO_NUM_2    // Onboard LED GPIO pin (modify if necessary)
#define QUEUE_SIZE 10          // Queue size for storing CAN messages
#define LED_ON_DURATION 50     // LED on duration threshold in milliseconds

QueueHandle_t message_queue;
volatile uint32_t last_received_time = 0; // Last message receive timestamp

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

void receive_can_message()
{
    twai_message_t message;
    while (1) {
        // Wait indefinitely for a CAN message
        if (twai_receive(&message, portMAX_DELAY) == ESP_OK) {
            printf("Message received. ID: 0x%lx, DLC: %d\n", (unsigned long)message.identifier, message.data_length_code);
            printf("Data: ");
            for (int i = 0; i < message.data_length_code; i++) {
                printf("0x%02x ", message.data[i]);
            }
            printf("\n");

            // Update the last received timestamp and queue the message
            last_received_time = xTaskGetTickCount() * portTICK_PERIOD_MS;
            xQueueSend(message_queue, &message, 0);
        }
    }
}

void led_task()
{
    twai_message_t message;
    uint32_t current_time;

    while (1) {
        // Get the current time
        current_time = xTaskGetTickCount() * portTICK_PERIOD_MS;

        // Check if the last message was received within the threshold duration
        if ((current_time - last_received_time) <= LED_ON_DURATION) {
            gpio_set_level(LED_GPIO, 1); // Keep LED on
        } else {
            gpio_set_level(LED_GPIO, 0); // Turn off LED
        }

        // Small delay to avoid high CPU usage
        vTaskDelay(pdMS_TO_TICKS(10));
    }
}

void app_main()
{
    // Initialize CAN and LED
    init_can();
    init_led();

    // Create a queue to hold CAN messages
    message_queue = xQueueCreate(QUEUE_SIZE, sizeof(twai_message_t));
    if (message_queue == NULL) {
        printf("Failed to create message queue\n");
        return;
    }

    // Start the receive and LED tasks
    xTaskCreate(receive_can_message, "CAN Receive Task", 4096, NULL, 5, NULL);
    xTaskCreate(led_task, "LED Task", 2048, NULL, 5, NULL);
}
