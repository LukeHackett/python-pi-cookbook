#/usr/bin/python
#
# Copyright 2013 Luke Hackett
# https://github.com/LukeHackett

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import RPi.GPIO as GPIO

# LED constants
RED_LED = 18
AMB_LED = 23
GRE_LED = 24

# Initialise the board
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Initialise the pins
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(AMB_LED, GPIO.OUT)
GPIO.setup(GRE_LED, GPIO.OUT)

try:
	while(True):
		# Force cars to stop (RED)
		GPIO.output(RED_LED, GPIO.HIGH)
		time.sleep(2)
		
		# Allow cars to start moving (RED/AMBER)
		GPIO.output(AMB_LED, GPIO.HIGH)
		time.sleep(2)
		
		# All cars can go (GREEN) 
		GPIO.output(RED_LED, GPIO.LOW)
		GPIO.output(AMB_LED, GPIO.LOW)
		GPIO.output(GRE_LED, GPIO.HIGH)
		time.sleep(5)
		
		# Traffic should slow (AMBER)
		GPIO.output(GRE_LED, GPIO.LOW)
		GPIO.output(AMB_LED, GPIO.HIGH)
		time.sleep(2)
		
		# Turn off led for the return
		GPIO.output(AMB_LED, GPIO.LOW)
		
except (KeyboardInterrupt, SystemExit):
	print "CTRL-C pressed: turning all LEDS off, and cleaning up"
	
	# Turn the LEDs off
	GPIO.output(RED_LED, GPIO.LOW)
	GPIO.output(AMB_LED, GPIO.LOW)
	GPIO.output(GRE_LED, GPIO.LOW)
	
	# Reset the PINs
	GPIO.cleanup()

	print "All done."
