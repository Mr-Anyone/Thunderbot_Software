#pragma once

#include <string>

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


    GpioState getState();

    /**
      technically shouldn't be a member function be whatever
      */
    std::string getCsvContent();

    void switchState();

   private:
    GpioCharDev m_gpio;
    GpioState m_state;
};
