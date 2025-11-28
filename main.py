from gpiozero import OutputDevice
from time import sleep
# GPIO pin for relay signal
relay_pin = 17
# Create relay object
relay = OutputDevice(relay_pin)
try:
    while True:
        relay.on()
# energize relay – click ON
        print("Relay ON")
        sleep(1)
        relay.off()
# release relay – click OFF
        print("Relay OFF")
        sleep(1)
except KeyboardInterrupt:
    relay.off()
    print("Program stopped safely.")