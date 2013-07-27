#/usr/bin/python
#
# Copyright 2013 Luke Hackett
# https://github.com/LukeHackett
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import RPi.GPIO as GPIO

# Traffic LED constants
RED_LED = 18
AMB_LED = 23
GRE_LED = 24

# Pedestrian LED constants
PED_RED_LED = 25
PED_GRE_LED = 8

# Pedestrian button constants
PED_BUTTON = 7
PED_WAITING = False

# Initialise the board
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Initialise the output pins
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(AMB_LED, GPIO.OUT)
GPIO.setup(GRE_LED, GPIO.OUT)
GPIO.setup(PED_RED_LED, GPIO.OUT)
GPIO.setup(PED_GRE_LED, GPIO.OUT)

# Initialise the input pins
GPIO.setup(PED_BUTTON, GPIO.IN)

# Crssing request function
def cross_request(channel):
	global PED_WAITING
	PED_WAITING = True

# Detects a button press, executing the callback upon a new thread
GPIO.add_event_detect(PED_BUTTON, GPIO.RISING, callback=cross_request, bouncetime=200)


try:
	while(True):
		# Force cars and pedestrians to stop (RED)
		GPIO.output(RED_LED, GPIO.HIGH)
		GPIO.output(PED_RED_LED, GPIO.HIGH)
		time.sleep(2)
		
		if PED_WAITING:
			# Allows the pedestrian to cross for 5 seconds
			GPIO.output(PED_RED_LED, GPIO.LOW)
			GPIO.output(PED_GRE_LED, GPIO.HIGH)
			time.sleep(5)
			
			# Prevent all pedestrians from crossing
			GPIO.output(PED_GRE_LED, GPIO.LOW)
			GPIO.output(PED_RED_LED, GPIO.HIGH)
			
			# Turn off the traffic RED light
			GPIO.output(RED_LED, GPIO.LOW)			

			# Flash the amber light
			for i in range(0, 4):
				GPIO.output(AMB_LED, GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(AMB_LED, GPIO.LOW)
				time.sleep(0.5)

			# Clear the waiting flag
			PED_WAITING = False 

		else:
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
	GPIO.output(PED_RED_LED, GPIO.LOW)
	GPIO.output(PED_GRE_LED, GPIO.LOW)
	
	# Reset the PINs
	GPIO.cleanup()

	print "All done."
