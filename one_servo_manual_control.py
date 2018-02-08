#!/usr/bin/env python

import sys
import time
import random
import pigpio

MIN_WIDTH=600
MAX_WIDTH=2300
angle_pw_ratio = (MAX_WIDTH - MIN_WIDTH) / 180.0

pi = pigpio.pi()

if not pi.connected:
   exit()

pi.set_servo_pulsewidth(18, 0)
print "Sending servo pulses to GPIO 18, control C to stop."

while True:


   try:
	 a = input("Set angle between 0 and 180: ")
 	 pw = int(a*angle_pw_ratio + MIN_WIDTH)
	 pi.set_servo_pulsewidth(18, pw)

   except KeyboardInterrupt:
      break

print("\nTidying up")

pi.set_servo_pulsewidth(18, 0)

pi.stop()
