import time
import board
import adafruit_dht
# Initialize the DHT11 sensor on GPIO17
dhtDevice = adafruit_dht.DHT11(board.D17)
while True:
    try:
# Read temperature and humidity
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
# Convert temperature to Fahrenheit
        temperature_f = temperature_c * (9 / 5) + 32
# Display formatted output
        print(f"Temp: {temperature_f:.1f} F / {temperature_c:.1f} C  |  Humidity: {humidity}%")
    except RuntimeError as error:
# Common read errors; retry after short delay
        print(f"Reading error: {error.args[0]}")
        time.sleep(2.0)
        continue
    except Exception as error:
# Graceful exit if unexpected error occurs
        dhtDevice.exit()
        raise error
    time.sleep(2.0)