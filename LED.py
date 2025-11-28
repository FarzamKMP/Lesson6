from gpiozero import DistanceSensor, RGBLED
from time import sleep

# Sensor on new pins to avoid conflicts
sensor = DistanceSensor(echo=27, trigger=17)  # meters

# RGB LED (common cathode):  R=26, G=19, B=13
led = RGBLED(red=26, green=19, blue=13)


def set_band_color(cm: float):
    """
    >= 20 cm  -> GREEN
    10–19.99  -> YELLOW
    < 10 cm   -> RED
    """
    if cm >= 20:
        led.color = (0, 1, 0)  # Green
    elif cm >= 10:
        led.color = (1, 1, 0)  # Yellow
    else:
        led.color = (1, 0, 0)  # Red


try:
    while True:
        cm = sensor.distance * 100.0  # meters -> cm
        print(f"{cm:5.1f} cm")
        set_band_color(cm)
        sleep(0.1)
except KeyboardInterrupt:
    led.off()
    print("Stopped by user.")