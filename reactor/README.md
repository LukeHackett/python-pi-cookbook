Reactor Game
-------

This simple project will demostrate a how to create a simple reactor game. The idea of the game is that a random LED will be illuminated, and the player must push the corresponding button in as little time as possible. If the correct button is pressed, another random LED will be illuminated.

This game has two modes, "fastest finger" and "maximum". The Fastest finger will log the fastest and slowest reaction time in seconds. The maximum mode will count the number of times a correct button has been pressed.

Both game modes will only run for a user-defined amount of time.

To create this game, you will need:

* 4x LEDs (any colour)
* 4x Resistors (any suitable resistor for your chosen LEDs)
* 4x push-to-make buttons
* 1x Breadboard
* A number of jumper wires


A example circuit diagram is shown below. I used GPIO pins 7, 8, 9, 10, 14 and 15 however any GPIO pins can be used. If a different set of GPIO pins are to be used then the PIN values should be changed at the top of the main.py file.

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/reactor/circuit_diagram.png) &nbsp;



### Python Library Prerequisite

Inorder to use the GPIO, an additional library will need to be installed. This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).