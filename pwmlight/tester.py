
import pwmlight

light = pwmlight.pwmlight(18, 50000, 1000000, 'test')

light.brightness = 20
light.turnOn()

light.debug(200000)

print(str(light.brightness))

print(str(light.getState()))
