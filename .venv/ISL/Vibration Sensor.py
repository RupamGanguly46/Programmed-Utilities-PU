import RPi.GPIO as GPIO
import time

# Pin configuration
SENSOR_PIN = 17  # GPIO pin connected to the sensor's D0
LED_PIN = 18  # GPIO pin connected to the LED

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

tap_count = 0  # Initialize tap count
tap_threshold = 10  # Number of taps required to turn on the LED


def detect_tap(channel):
    global tap_count
    tap_count += 1
    print(f'Tap detected! Count: {tap_count}')

    if tap_count >= tap_threshold:
        # GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        # print("LED turned ON!")
        emergency()
        time.sleep(5)  # Keep the LED on for 5 seconds
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        tap_count = 0  # Reset tap count

def emergency():
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        print("LED turned ON!")

# Add event detection for the vibration sensor
GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=detect_tap, bouncetime=200)

try:
    print("Waiting for taps...")
    while True:
        time.sleep(1)  # Keep the program running

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()  # Clean up GPIO settings