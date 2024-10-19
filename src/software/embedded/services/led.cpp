#include "led.h"

#include "software/embedded/gpio.h"
#include "software/logger/logger.h"

Led::Led() : m_gpio(24, GpioDirection::OUTPUT, GpioState::LOW) {}

void Led::turnOn()
{
    LOG(DEBUG) << "RED LED Turn On";
    m_gpio.setValue(GpioState::HIGH);
}

void Led::turnOff()
{
    LOG(DEBUG) << "RED Led Turn Off";
    m_gpio.setValue(GpioState::LOW);
}
