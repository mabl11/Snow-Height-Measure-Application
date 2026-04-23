import time
import busio
import board
import digitalio
import adafruit_lidarlite
import adafruit_bme680

MEASURE_ACCURACY = 100

i2c = busio.I2C(board.SCL, board.SDA)

bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x76)

# # # change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

sensor = adafruit_lidarlite.LIDARLite(i2c, sensor_type=adafruit_lidarlite.TYPE_V3HP)
led = digitalio.DigitalInOut(board.LED_RED)
led.direction = digitalio.Direction.OUTPUT

def measure_temperature():
    temp = bme680.temperature
    print("temperature: ", temp)

def measure_distance():
    distance_list = []
    for x in range(MEASURE_ACCURACY):
        distance = sensor.read_distance_v3hp()
        led.value = True
        time.sleep(0.02)
        led.value = False
        distance_list.append(distance)
    
    mean_dist = sum(distance_list)/len(distance_list)
    return mean_dist

cycle = 0
default_distance = measure_distance()
while True: 
    cycle = cycle + 1
    measure_temperature()
    distance = measure_distance()
    distance_change = default_distance - distance
    if distance_change > 1.5:
        print("snow_depth: ", distance_change)
    time.sleep(5)
    



