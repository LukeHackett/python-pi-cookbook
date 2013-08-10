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

import time, datetime
import RPi.GPIO as GPIO

# LED constants
HOT_LED = 7
OK_LED = 8
COLD_LED = 25

# Temperature sensor serial ID 
SENSOR = "28-000004f86e16"

# Initialise the board
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Initialise the pins
GPIO.setup(HOT_LED, GPIO.OUT)
GPIO.setup(OK_LED, GPIO.OUT)
GPIO.setup(COLD_LED, GPIO.OUT)


def get_temperature():
	# Open the temperature file
	tempLoc = "/sys/bus/w1/devices/%s/w1_slave" % SENSOR
	tempFile = open(tempLoc)
	text = tempFile.read()

	# Parse the temperature
	tempData = text.split()[-1]
	temperature = float(tempData[2:])
	
	# Return the temperature in degrees C
	return temperature / 1000
	
	
try:
	while(True):
		# Make a reading
		temperature = get_temperature()
		
		# Output reading
		now = datetime.datetime.now()
		ts = now.strftime("%d/%m/%y %H:%M:%S")
		print "[%s] The temperature is %s degrees celsius." % (ts, temperature)

		# Turn all LEDs OFF
		GPIO.output(HOT_LED, GPIO.LOW)
		GPIO.output(OK_LED, GPIO.LOW)
		GPIO.output(COLD_LED, GPIO.LOW)

		# Turn the correct LED on
		if temperature >= 30.0:
			# Temperature is HOT
			GPIO.output(HOT_LED, GPIO.HIGH)

		elif temperature <= 20.0:
			# Temperature is COLD
			GPIO.output(COLD_LED, GPIO.HIGH)

		else:
			# Temperature is OK
			GPIO.output(OK_LED, GPIO.HIGH)
		
		# Wait before polling again
		time.sleep(5)


except (KeyboardInterrupt, SystemExit):
	print "CTRL-C pressed: turning all LEDS off, and cleaning up"
	
	# Turn the LEDs off
	GPIO.output(HOT_LED, GPIO.LOW)
	GPIO.output(OK_LED, GPIO.LOW)
	GPIO.output(COLD_LED, GPIO.LOW)
	
	# Reset the PINs
	GPIO.cleanup()

	print "All done."
