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
import time
import player
import questions

class Game(object):

        def __init__(self, player1, buzz1, player2, buzz2, green, red, max):
		# Initialise the board
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		
		# Initialise Inputs
		self.buzzer1 = buzz1
		self.buzzer2 = buzz2
		GPIO.setup(buzz1, GPIO.IN)
		GPIO.setup(buzz2, GPIO.IN)

		# Initialise Outputs
		self.green_led = green
		self.red_led = red
		GPIO.setup(green, GPIO.OUT)
		GPIO.setup(red, GPIO.OUT)
		
		# Initialise Players and Questions
		self.player1 = player.Player(player1, buzz1)
		self.player2 = player.Player(player2, buzz2)
		self.questions = questions.Questions()
		self.max_score = max

	
	def __get_buzzer(self):
		while(True):
			# Obtain both inputs
			if(GPIO.input(self.buzzer1) == GPIO.HIGH):
				time.sleep(0.5)
				return self.buzzer1
			
			if(GPIO.input(self.buzzer2) == GPIO.HIGH):
				time.sleep(0.5)
				return self.buzzer2
	

	def __show_correct_light(self, length):
		GPIO.output(self.green_led, GPIO.HIGH)
		time.sleep(length)
		GPIO.output(self.green_led, GPIO.LOW)

	
	def __show_incorrect_light(self, length):
		GPIO.output(self.red_led, GPIO.HIGH)
		time.sleep(length)
		GPIO.output(self.red_led, GPIO.LOW)		

	
	def __print_score_board(self):
		# Print the current score
                print ""
                print "*** SCORES ***"
                print "%s: %d" % (self.player1.name, self.player1.score)
                print "%s: %d" % (self.player2.name, self.player2.score)
                print "**************"
                print ""

	
	def __print_winner(self):
		player = self.player1 if (self.player1.score > self.player2.score) else self.player2
		print ""
		print "%s WINS." % player.name
		self.__print_score_board()
	

	def start(self):
		max_score = 0

		while(max_score < self.max_score):
			# Print the current score
			self.__print_score_board()

            	 	# Get a random question
                	(question, answer) = self.questions.get_random_question()
                	print question

                	# Get the buzzer input
                	buzzer = self.__get_buzzer()
	
			# Show that an input has been detected
			player = self.player1 if self.player1.buzzer == buzzer else self.player2
			print "%s, what is your answer?" % player.name

			# Obtain the answer
			input = raw_input("> ").strip().lower()
			answer = answer.strip().lower()

			# Validate the answer
			if(input == answer):
				print "Correct Answer"
				self.__show_correct_light(3)
				player.add_points(1)
				
				# Update the maximum score				
				max_score = self.player1.score if self.player1.score > self.player2.score else self.player2.score	
			else:
				print "Incorrect Answer"
				self.__show_incorrect_light(3)
		
		# Winner
		self.__print_winner()

		# Clean up
		GPIO.cleanup()
