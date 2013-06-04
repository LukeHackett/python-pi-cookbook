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

import RPi.GPIO as GPIO
from led import LED
from tactile_switch import TactileSwitch
import random, threading, time, datetime

class Game(object):

	def __init__(self):
		self.reactors = []
		self.times = []
		self.limit = 10
		self.finished = False
		GPIO.setmode(GPIO.BCM)


	def add_reactor(self, button, led):	
		# Setup the button
		GPIO.setup(button, GPIO.IN)
		button_obj = TactileSwitch(button)

		# Setup the LED
		GPIO.setup(led, GPIO.OUT)
		led_obj = LED(led)
		
		self.reactors.append((button_obj, led_obj))
	
	
	def __get_reactor(self, index = None):
		if(index == None):
			return random.sample(self.reactors, 1)[0]
		else:
			return self.reactors[index]

		
	def start_game(self):
		# Print Instructions
		print "The game will start in 3 seconds..."
		time.sleep(3)

		# Start the countdown timer
		cd = CountDown(self)
		cd.start()
		
		# main game while loop
		while(not self.finished):
			# get a random reactor
			(button, led) = self.__get_reactor()
			
			# turn the LED on
			start = datetime.datetime.now()
			led.turn_on()
			
			# Wait for the correct button press
			while(button.is_pressed_off()):
				pass
			
			# turn the LED off
			end = datetime.datetime.now()
			led.turn_off()
			
			# calculate the difference
			diff = end - start
			self.times.append(diff)
		
	def start_quickest(self):
		# start the game
		self.start_game()
		
		# print the game stats
		print "Slowest response was: %s" % max(self.times)
		print "Quickest response was: %s" % min(self.times)


	def start_maximum(self):
		# start the same
		self.start_game()
		
		buttons = len(self.times)
		average = buttons / int(self.limit)

		# print the game stats
		print "You managed to press %s buttons correctly." % buttons
		print "That's an average of %s per second." % average

     
class CountDown(threading.Thread):
	
	def __init__(self, game):
		threading.Thread.__init__(self)
		self.game = game


	def run(self):
		limit = self.game.limit
		
		# Hacky atm - better way required
		while(limit != 0):
			time.sleep(1)
			limit = limit - 1		

		# Countdown done
		self.game.finished = True
