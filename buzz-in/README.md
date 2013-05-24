Buzz-in Game
-------

This simple project will demostrate a how to create a simpl buzz-in game. The idea of the game is that a number of random questions are presented to two players. If a player knows the answer to the question they should press their buzzer. If a correct answer is given a green LED lit up, however should an incorrect answer be given the red LED will be lit up, along with a buzz sound.

To create this game, you will need:

* 1x LEDs (any colour, ideally red, and green)
* 2x Resistors (any suitable resistor for your chosen LEDs)
* 2x push-to-make buttons
* 1x buzzer
* 1x Breadboard
* A number of jumper wires


A example circuit diagram is shown below. I used GPIO pins 7, 8, 14 and 15 however any GPIO pins can be used. If a different set of GPIO pins are to be used then the PIN values should be changed at the top of the main.py file.

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/buzz-in/breadboard_diagram.png) &nbsp;



### Python Library Prerequisite

Inorder to use the GPIO, an additional library will need to be installed. This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).
