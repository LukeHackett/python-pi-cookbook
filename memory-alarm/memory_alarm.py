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

import RPi.GPIO as GPIO
import subprocess
import time


RED_LED = 7
AMBER_LED = 8
GREEN_LED = 25


def initialise_leds():
	"""This method will initialise the LEDs and setup the pins"""
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RED_LED, GPIO.OUT)
	GPIO.setup(AMBER_LED, GPIO.OUT)
	GPIO.setup(GREEN_LED, GPIO.OUT)

def get_total_memory():
	"""This method will return the total amount of RAM in the system"""
	cmd = "free | grep Mem | tr -s ' ' | cut -d ' ' -f 2"
	value = subprocess.check_output(cmd, shell=True).strip()
	return int(value)

def get_free_memory():
	"""This mthod will return the free memory available in the system"""
	cmd = "free | grep Mem | tr -s ' ' | cut -d ' ' -f 4"
	value = subprocess.check_output(cmd, shell=True).strip()
	return int(value)


# Setup the Board and LEDs
initialise_leds()

# Calculate the available memory
total = get_total_memory()
free = get_free_memory()
available = (free * 100) / total

# Check for DANGEROUS memory levels
if available <= 10:
	print "Memory usage is DANGEROUS (%d%% free)" % available
	GPIO.output(RED_LED, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(RED_LED, GPIO.LOW)

# Check for HIGH memory levels
elif available <= 30:
	print "Memory usage is HIGH (%d%% free)" % available
	GPIO.output(AMBER_LED, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(AMBER_LED, GPIO.LOW)

# Check for ACCEPTABLE memory levels
elif available > 30:
	print "Memory usage is ACCEPTABLE (%d%% free)" % available
	GPIO.output(GREEN_LED, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(GREEN_LED, GPIO.LOW)

# Some unknown error
else:
	print "An error has occured"

# Clean up and reset the PINs
GPIO.cleanup()
