
from Jetson.GPIO.gpio import cleanup, gpio_function
import RPi.GPIO as GPIO

from playsound import playsound

import jetson.inference
import jetson.utils


# Handles time
import time 

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.3)
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

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

def sound():
    playsound('/home/hossein/code/Hawk.mp3')
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(pir_pin, GPIO.IN)
    GPIO.setup(mic_pin, GPIO.IN)
    GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=pir, bouncetime=10)
    #GPIO.add_event_detect(mic_pin, GPIO.RISING, callback=microwave, bouncetime=1)
    while 1:
        img=camera.Capture()
        detections = net.Detect(img)
        display.Render(img)
        display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        if detections != []:
            playsound('/home/hossein/code/Hawk.mp3')
           
    else:
        GPIO.cleanup()
if __name__ == '__main__':
    main()
