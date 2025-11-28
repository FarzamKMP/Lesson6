#!/usr/bin/env python3
from gpiozero import DistanceSensor
from time import sleep
    # Trigger -> 17, Echo -> 27 (BCM)
sensor = DistanceSensor(echo=27, trigger=17)
try:
    while True:
        cm = sensor.distance * 100.0   # .distance is in METERS → convert to cm
        print(f"Distance: {cm:.2f} cm")
        sleep(0.3)
except KeyboardInterrupt:
    print("Stopped by user.")