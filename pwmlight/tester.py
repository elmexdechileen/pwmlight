import pwmlight

light = pwmlight.pwmlight(18, 5000, 20000, 'test')

light.brightness = 200


print(str(light.brightness))

print(str(light.State()))
