Buzz-in Game
-------

This simple project will demonstrate a how to create a simple buzz-in game.

The idea of the game is that a number of random questions are presented to 
two players. If a player knows the answer to the question they should press 
their buzzer. 

If a correct answer is given a green LED lit up, however should an incorrect 
answer be given the red LED will be lit up, along with a buzz sound.


### Ingredients

* 2x LEDs (any colour, ideally red and green)
* 2x Resistors (any suitable resistor for your chosen LEDs)
* 2x push-to-make buttons
* 1x buzzer
* 1x Breadboard
* A number of jumper wires


### Recipe

1. Connect one side of the push-to-make button to the +3.3V pin and the other 
side to GPIO 7.
2. Connect one side of the other push-to-make button to the +3.3V pin and the 
other side to GPIO 8.
3. Connect GPIO 15 to a resistor and then connect the resistor to the green 
LED.
4. Connect GPIO 14 to a resistor and then connect the resistor to both the red 
LED and the buzzer.

**Note:** A different set of GPIO pins can be used, to which the software will 
need to be updated to the new value(s). These values are stored in the top of 
the main.py file.


#### Circuit Diagram

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/buzz-in/breadboard_diagram.png) &nbsp; </center>


### Python Library Prerequisite

In order to use the GPIO, an additional library will need to be installed. 
This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).
