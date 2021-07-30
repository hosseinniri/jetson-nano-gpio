
from Jetson.GPIO.gpio import cleanup, gpio_function
import RPi.GPIO as GPIO

from playsound import playsound

import jetson.inference
import jetson.utils


# Handles time
import time 

# Pin Definitions:
led_pin = 7
pir_pin = 12
mic_pin = 13


net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.3)
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file
def sound():
    playsound('/home/hossein/code/Hawk.mp3') 
    
def ledon():
    GPIO.output(led_pin, GPIO.HIGH) 
    
def ledoff():
    GPIO.output(led_pin, GPIO.LOW)
    
      
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
    
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH) 
    
    
    GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=pir, bouncetime=10)
    #GPIO.add_event_detect(mic_pin, GPIO.RISING, callback=microwave, bouncetime=1)
    index=0
    while 1:
        img=camera.Capture()
        detections = net.Detect(img)
        display.Render(img)
        display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        microwave_flag = GPIO.input(mic_pin)
        pir_flag = GPIO.input(pir_pin)
        
        if (detections != []) or microwave_flag or pir_flag :
            if (index % 3) == 0:
                sound()
            elif (index % 3) == 1:
                ledon()
            elif (index % 3) == 2:
                ledon()
            microwave_flag = 0
            pir_flag = 0
            index = index +1
        else:
            ledoff()
    else:
        GPIO.cleanup()
if __name__ == '__main__':
    main()
