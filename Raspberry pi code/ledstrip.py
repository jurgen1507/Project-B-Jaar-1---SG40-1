import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

print("neopixels walk")

clock_pin = 5
data_pin = 6

GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(data_pin, GPIO.OUT)


def apa102_send_bytes(clock_pin, data_pin, bytes):
    """
    zend de bytes naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin
    """

    # implementeer deze functie:
    for byte in bytes:
        for bit in byte:
            if bit == '1':
                GPIO.output(data_pin, GPIO.HIGH)
            else:
                GPIO.output(data_pin, GPIO.LOW)
            GPIO.output(clock_pin, GPIO.HIGH)
            GPIO.output(clock_pin, GPIO.LOW)
    # zend iedere byte in bytes:
    #    zend ieder bit in byte:
    #       maak de data pin hoog als het bit 1 is, laag als het 0 is
    #       maak de clock pin hoog
    #       maak de clock pin laag


def apa102(clock_pin, data_pin, colors):
    """
    zend de colors naar de APA102 LED strip die is aangesloten op de clock_pin en data_pin

    De colors moet een list zijn, met ieder list element een list van 3 integers,
    in de volgorde [ blauw, groen, rood ].
    Iedere kleur moet in de range 0..255 zijn, 0 voor uit, 255 voor vol aan.

    bv: colors = [ [ 0, 0, 0 ], [ 255, 255, 255 ], [ 128, 0, 0 ] ]
    zet de eerste LED uit, de tweede vol aan (wit) en de derde op blauw, halve strekte.
    """

    # implementeer deze functie, maak gebruik van de apa102_send_bytes functie
    apa102_send_bytes(clock_pin, data_pin, [str(format(0,'08b')), str(format(0,'08b')), str(format(0,'08b')), str(format(0,'08b'))])
    # zend eerst 4 bytes met nullen
    for pixel in range(0,8):
        apa102_send_bytes(clock_pin, data_pin, [str(format(255,'08b')),str(format(colors[pixel][0],'08b')), str(format(colors[pixel][1],'08b')), str(format(colors[pixel][2],'08b'))])
    apa102_send_bytes(clock_pin, data_pin, [str(format(255,'08b')), str(format(255,'08b')), str(format(255,'08b')), str(format(255,'08b'))])
    # zend dan voor iedere pixel:
    #    eerste een byte met allemaal enen
    #    dan de 3 bytes met de kleurwaarden
    # zend nog 4 bytes, maar nu met allemaal enen


away = [0, 33, 51]
online = [0, 30, 0]
dontdisturb = [0, 0, 30]
offline = [0, 0, 0]


def colors(n, onlinelist):
    result = []
    onlinelist
    for offlinestate in range(0,onlinelist[0]):
        result.append(offline)
    for nodisturb in range(0, onlinelist[1]):
        result.append(dontdisturb)
    for awaystate in range(0, onlinelist[2]):
        result.append(away)
    for onlinestate in range(0, onlinelist[3]):
        result.append(online)
    print(result)
    return result



