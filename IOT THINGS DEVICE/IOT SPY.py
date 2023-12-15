import mraa
import os
print(mraa.getVersion())

led=mraa.Gpio(23)
led.dir(mraa.DIR_OUT)
led.write(0)

touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)

while True:
    touchButton=int(touch.read())
    if (touchButton == 1):
        led.write(1)

      os.system("export http_proxy=http://34.73.58.235.:3128;curl  -H \
                Content-Type: application/json\
                -d {press\ : 1} -x POST http://34.73.52.137:8080/alarm")
else:
    led.write(0)
    os.system("export http_proxy=http://34.73.58.235:3128: curl -H \
              'Com")
    led=mraa.Gpio(23)
    os.system("export http_proxy=http://34.73.58.235.:3128;curl \
               ")