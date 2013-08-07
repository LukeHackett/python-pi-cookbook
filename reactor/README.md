Reactor Game
-------

This simple project will demonstrate a how to create a simple reactor game. 

The idea of the game is that a random LED will be illuminated, and the player 
must push the corresponding button in as little time as possible. If the 
correct button is pressed, another random LED will be illuminated.

The game has two modes, "fastest finger" and "maximum". 

The Fastest finger will log the fastest and slowest reaction time in seconds. 
The maximum mode will count the number of times a correct button has been 
pressed.

Both game modes will only run for a user-defined amount of time.


### Ingredients

* 4x LEDs (any colour)
* 4x Resistors (any suitable resistor for your chosen LEDs)
* 4x push-to-make buttons
* 1x Breadboard
* A number of jumper wires


### Recipe

1. Connect GPIO 8 to a resistor and then connect the resistor to one of the 
LEDs.
2. Repeat step one *three times* using GPIO 10, 23 and 14.
3. Connect one side of the push-to-make button to the +3.3V pin and the other 
side to GPIO 7.
4. Repeat step three *three times* using GPIO 9, 24 and 15.

**Note:** A different set of GPIO pins can be used, to which the software will 
need to be updated to the new value(s). These values are stored in the top of 
the main.py file.


#### Circuit Diagram

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/reactor/breadboard_diagram.png) &nbsp;</center>


### Python Library Prerequisite

In order to use the GPIO, an additional library will need to be installed. 
This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).