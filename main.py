import RPi.GPIO as GPIO
import time

# Pin Definitions:
pir_pin = 12
mic_pin = 13
led_pin = 7
pwm_pin=33


pwm_freq = 5000




def pir(channel):
    toggle_led()
    print("pir detected")
    pir_flag=1


def microwave(channel):
    print("microwave detected")
    microwave_flag=1

def toggle_led():
  GPIO.output(led_pin, GPIO.HIGH) 
  print("LED is ON")
  time.sleep(1) 
  GPIO.output(led_pin, GPIO.LOW)
  print("LED is OFF")
  time.sleep(1)

def pwm():
    val = 50
    pwm.start(val)
    time.sleep(2)
    pwm.stop(val)
 
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(pir_pin, GPIO.IN)
    GPIO.setup(mic_pin, GPIO.IN)
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH) 
    GPIO.setup(pwm_pin, GPIO.OUT, initial=GPIO.HIGH)
    pwm = GPIO.PWM(pwm_pin, pwm_freq)

    GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=pir, bouncetime=10)
    #GPIO.add_event_detect(mic_pin, GPIO.RISING, callback=microwave, bouncetime=1)

    print("Starting now! Press CTRL+C to exit")
    try:
        while True:
            print(">>>>>>>>>>>>>>>>>>>>........>>>>>>>>>>>>>>>>>>\n")
            microwave_flag = GPIO.input(mic_pin)
            if microwave_flag==GPIO.HIGH:
                toggle_led()
                print("microwave detected") 
            else: 
                print("                  ")
            time.sleep(1)
    finally:
        GPIO.cleanup()
if __name__ == '__main__':
    main()
