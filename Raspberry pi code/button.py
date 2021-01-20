import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("sr04 print")
AFK = False
sr04_trig = 24
sr04_echo = 23
distance = 0
GPIO.setup(sr04_trig, GPIO.OUT)
GPIO.setup(sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def sr04(trig_pin, echo_pin):
    """
    Return the distance in cm as measured by an SR04
    that is connected to the trig_pin and the echo_pin.
    These pins must have been configured as output and input.s
    """
    while True:
        # send trigger pulse
        # inplement this step
        GPIO.output(trig_pin, GPIO.HIGH)
        time.sleep(0.000001)
        GPIO.output(trig_pin, GPIO.LOW)
        # wait for echo high and remember its start time
        # inplement this step


        while GPIO.input(echo_pin) == 0:
            start_time = time.time()

        # wait for echo low and remember its end time
        # inplement this step
        while GPIO.input(echo_pin) == 1:
            end_time = time.time()

        # calculate and return distance
        # inplement this step
        global distance
        distance = 34330 * (end_time - start_time) / 2

        
        time.sleep(0.5)
    