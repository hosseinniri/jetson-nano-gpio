#!/usr/bin/env python

# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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
