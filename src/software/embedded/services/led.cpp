#include "led.h"

#include <sys/wait.h>

#include "software/embedded/gpio.h"
#include "software/logger/logger.h"

Led::Led() : m_gpio(24, GpioDirection::OUTPUT, GpioState::LOW), m_state(GpioState::LOW) {}

void Led::turnOn()
{
    LOG(DEBUG) << "RED LED Turn On";
    m_gpio.setValue(GpioState::HIGH);
    m_state = GpioState::HIGH;
}
void Led::turnOff()
{
    LOG(DEBUG) << "RED Led Turn Off";
    m_gpio.setValue(GpioState::LOW);
    m_state = GpioState::LOW;
}

GpioState Led::getState()
{
    return m_state;
}

std::string Led::getCsvContent()
{
    switch (m_state)
    {
        case GpioState::HIGH:
            return "1";
        case GpioState::LOW:
            return "0";
        default:
            LOG(WARNING)
                << "we have entered an impossible that that is neither high or low";
            return "?";
    }

    return "?";
}

void Led::switchState()
{
    switch (m_state)
    {
        case GpioState::HIGH:
            turnOff();
            return;  // Exit the function after turning off
        case GpioState::LOW:
            turnOn();
            return;  // Exit the function after turning on
        default:
            LOG(WARNING)
                << "we have entered an impossible that that is neither high or low";
            // Optionally handle unexpected states
            return;
    }
}
