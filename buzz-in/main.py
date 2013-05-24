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

import game

PLAYER1_PIN = 7
PLAYER2_PIN = 8
GREEN_LED = 15
RED_LED = 14

def main():
	print "The Buzz-in Game"
	print ""
	
	# Player 1 input
	print "Player 1, please enter your name:"
	player1 = raw_input("> ").strip()

	print ""
	
	# Player 2 input
	print "Player 2, please enter your name:"
	player2 = raw_input("> ").strip()

	print ""

	# rounds input
	print "Please enter the number of rounds to play:"
	rounds = int(raw_input("> "))
	
	# start the game
	buzz = game.Game(player1, PLAYER1_PIN, player2, PLAYER2_PIN, GREEN_LED, RED_LED, rounds)
	buzz.start()

if __name__ == '__main__':
	main()
