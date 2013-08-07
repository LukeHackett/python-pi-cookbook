Traffic Lights (Version 2)
-------

This project will demonstrate a UK traffic light setup, that allows pedestrians 
the ability to cross the road safely.

Within the software element of this project will be a simple demonstration of 
callbacks, and how they can be applied. Handling user input 
via a button will also be covered.


### Ingredients

* 5x LEDs (any colour, ideally 2x red, 1x amber and 2x green)
* 5x Resistors (any suitable resistor for your chosen LEDs)
* 1x push-to-make button
* 1x Breadboard
* A selection of jumper wires


### Recipe

1. Connect one side of the push-to-make button to the +3.3V pin and the other 
side to GPIO 7.
2. Connect GPIO 25 to a resistor, and then connect the resistor to the red LED. 
This will simulate the "red man", indicating to pedestrians that it is not safe 
to cross the road.
3. Connect GPIO 8 to a resistor, and then connect the resistor to the green LED. 
This will simulate the "green man", indicating to pedestrians that it is safe 
to cross the road.
4. Connect GPIO 18 to a resistor and then connect the resistor to the red LED.
5. Connect GPIO 23 to a resistor and then connect the resistor to the amber/yellow LED.
6. Connect GPIO 24 to a resistor and then connect the resistor to the green LED.

**Note:** A different set of GPIO pins can be used, to which the software will 
need to be updated to the new value(s).


#### Circuit Diagram

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/traffic-lights-2/breadboard_diagram.png) &nbsp;
</center>


### Python Library Prerequisite

In order to use the GPIO functionality, an additional library will need to be 
installed. This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).
