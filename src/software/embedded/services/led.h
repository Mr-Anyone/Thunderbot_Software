#pragma once

#include "software/embedded/gpio_char_dev.h"

/**
 * Turning on LED on Raspberry PI. Currently Jetson nano is not supported!
 *
 *
 */
class Led
{
   public:
    Led();

    /**
     * Turning on the red LED
     */
    void turnOn();

    /**
     * Turning off the red LED
     */
    void turnOff();

   private:
    GpioCharDev m_gpio;
};
