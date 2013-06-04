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

from game import Game
import time

# Reaction Button GPIO pins
BUTTON_1 = 7
BUTTON_2 = 9
BUTTON_3 = 24
BUTTON_4 = 15

# LED GPIO pins
LED_1 = 8
LED_2 = 10
LED_3 = 23
LED_4 = 14

# Setup the game
game = Game()
game.add_reactor(BUTTON_1, LED_1)
game.add_reactor(BUTTON_2, LED_2)
game.add_reactor(BUTTON_3, LED_3)
game.add_reactor(BUTTON_4, LED_4)

# Game Instructions
print "*******************************"
print "***   The Pi-Reactor Game   ***"
print "*******************************"

print "Press the button when the LED lights up."
print "Which mode would you like to use?"
print "\t (1) Fastest Finger"
print "\t (2) Maximum Presses"

print "\nPlease enter your choice:"
option = raw_input("> ")

print "Please enter the time limit for the game in seconds:"
game.limit = int(raw_input("> "))

# Start the desired game
if(option == "1"):
	game.start_quickest()
elif(option == "2"):
	game.start_maximum()
else:
	print "INPUT ERROR: Invalid option"
	
