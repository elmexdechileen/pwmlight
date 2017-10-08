import pwmlight
import time

light = pwmlight.pwmlight(18, 50000, 1000000, 'test')

#light.brightness = 15
light.turnOn()

time.sleep(1)

light.brightness = 10

time.sleep(1)



light.turnOff()


#light.debug(20000)


print(str(light.brightness))

print(str(light.getState()))




