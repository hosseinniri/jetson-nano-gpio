#!/usr/bin/env python

# Copyright (c) 2019-2020, NVIDIA CORPORATION. All rights reserved.
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

pwm_pin=33




def main():
    pwm_freq = 30000
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH

    GPIO.setup(pwm_pin, GPIO.OUT, initial=GPIO.HIGH)
    pwm = GPIO.PWM(pwm_pin, pwm_freq)
    val = 50
    pwm.start(val)

    
    try:
        while True:
            print("PWM running. Press CTRL+C to exit.",pwm_freq)
            pwm_freq=int(input("Enter frequency:"))
            #val=int(input("Enter duty cycle in Percent:"))
            pwm.ChangeFrequency(pwm_freq)
            #pwm.ChangeDutyCycle(val)
            time.sleep(0.25)

    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
