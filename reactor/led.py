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

class LED(object):

	def __init__(self, pin):
		self.pin = pin
		self.on = False
		

	def turn_on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	
	def turn_off(self):
		GPIO.output(self.pin, GPIO.LOW)

	
	def is_on(self):
		return self.on


	def is_off(self):
		return not self.on
