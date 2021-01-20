import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )
stop = False


scp1 = 14 #(16, 14)
lcp1 = 15 #(20, 15)
dp1 = 18 #(21, 18)
scp2 = 16 #(16, 14)
lcp2 = 20 #(20, 15)
dp2 = 21
GPIO.setup( scp1, GPIO.OUT )
GPIO.setup( lcp1, GPIO.OUT )
GPIO.setup( dp1, GPIO.OUT )
GPIO.setup( scp2, GPIO.OUT )
GPIO.setup( lcp2, GPIO.OUT )
GPIO.setup( dp2, GPIO.OUT )
def hc595( scp1, lcp1, dp1, value, delay ):
    # implementeer deze functie
    for x in range(0,8):
        if value % 2 == 1:
            GPIO.output(dp1, GPIO.HIGH)
        else:
            GPIO.output(dp1, GPIO.LOW)
        GPIO.output(scp1, GPIO.HIGH)
        GPIO.output(scp1, GPIO.LOW)
        value = value // 2
    GPIO.output(lcp1, GPIO.HIGH)
    GPIO.output(lcp1, GPIO.LOW)
    time.sleep(delay)


def achievementleds(achievements):
    lamps_list = [{'sr': 2, 'value': 1},
                  {'sr': 2, 'value': 2},
                  {'sr': 2, 'value': 4},
                  {'sr': 2, 'value': 8},
                  {'sr': 2, 'value': 16},
                  {'sr': 2, 'value': 32},
                  {'sr': 2, 'value': 64},
                  {'sr': 2, 'value': 128},
                  {'sr': 2, 'value': 256},
                  {'sr': 1, 'value' : 64},
                  {'sr': 1, 'value': 128},
                  {'sr': 1, 'value': 1},
                  ]

    for i in lamps_list:
        if i['sr'] == 1:
            if i['value'] == 1:
                hc595(scp1, lcp1, dp1, i['value'], 0)
            else:
                hc595(scp1, lcp1, dp1, i['value'], 0.1)

        else:
            if i['value'] == 256:
                hc595(scp2, lcp2, dp2, i['value'], 0)
            else:
                hc595(scp2, lcp2, dp2, i['value'], 0.1)

    if achievements > 8:
        achievements+=1
    if achievements == 11:
        achievements +=1
    global stop
    while True:
        for x in range(0,achievements):
            if lamps_list[x]['sr'] == 1:
                if lamps_list[x]['value'] == 1:
                    hc595(scp1, lcp1, dp1, lamps_list[x]['value'], 0)
                else:
                    hc595(scp1, lcp1, dp1, lamps_list[x]['value'], 0.000001)

            else:
                if lamps_list[x]['value'] == 256:
                    hc595(scp2, lcp2, dp2, lamps_list[x]['value'], 0)
                else:
                    hc595(scp2, lcp2, dp2, lamps_list[x]['value'], 0.000001)
        if stop:
            break