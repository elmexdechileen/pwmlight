import pigpio as pg

class pwmlight():
    def __init__(self, pin, min_cycle, max_cycle, name = None, frequency = 2000):
        self._pin = pin
        self._min_cycle = min_cycle
        self._max_cycle = max_cycle
        self._name = name
        self._state = None
        self._brightness = None
        self._gpio = pg.pi()
        self._convfactor = (max_cycle - min_cycle) / 255
        self._freq = frequency

        if name is None:
            self._name = 'P' + str(pin)

    @property
    def brightness(self):
        return self._gpio.get_PWM_frequency(self._pin)

    @brightness.setter
    def brightness(self, value):
        self._gpio.hardware_PWM(self._pin, self._freq,
                                (value * self._convfactor + self._min_cycle))

    def turnOn(self):
        self._gpio.hardware_PWM(self._pin, self._freq,
                                (self._max_cycle))

    def turnOff(self):
        self._gpio.hardware_PWM(self._pin, self._freq, self._min_cycle)

    def getState(self):
        if self._brightness > self._min_cycle:
            return True
        else:
            return False
