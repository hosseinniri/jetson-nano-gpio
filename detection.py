
import RPi.GPIO as GPIO
import time

# Pin Definitions:
pir_pin = 12
mic_pin = 13


# blink LED 2 quickly 5 times when button pressed
def pir(channel):
    print("pir detected")
    pir_flag=1


def microwave(channel):
    print("microwave detected")
    microwave_flag=1
 
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(pir_pin, GPIO.IN)
    GPIO.setup(mic_pin, GPIO.IN)
    GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=pir, bouncetime=10)
    #GPIO.add_event_detect(mic_pin, GPIO.RISING, callback=microwave, bouncetime=1)

    print("Starting now! Press CTRL+C to exit")
    try:
        while True:
            print(">>>>>>>>>>>>>>>>>>>>........>>>>>>>>>>>>>>>>>>\n")
            microwave_flag = GPIO.input(mic_pin)
            if microwave_flag==GPIO.HIGH:
                print("microwave detected") 
            else: 
                print("                  ")
            time.sleep(1)
    finally:
        GPIO.cleanup()
if __name__ == '__main__':
    main()
