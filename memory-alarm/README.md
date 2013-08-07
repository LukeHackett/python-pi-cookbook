Memory Alarm
-------

This simple project will demostrate a how to create an LED based alarm for 
memory usage of a given system.


### Ingredients

* 3x LEDs (any colour, ideally red, amber and green)
* 3x Resistors (any suitable resistor for your chosen LEDs)
* 4x Jumper wires
* 1x Breadboard

**Note:** it is possible to use more jumper wires to substitute not having a 
breadboard.


### Recipe

1. Connect GPIO 7 to a resistor, and then connect the resistor to the red LED.
2. Connect GPIO 8 to a resistor, and then connect the resistor to the amber/yellow LED.
3. Connect GPIO 25 to a resistor, and then connect the resistor to the green LED.

**Note:** A different set of GPIO pins can be used, to which the software will 
need to be updated to the new value(s).


#### Circuit Diagram

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/memory-alarm/breadboard_diagram.png) &nbsp; </center>


### Python Library Prerequisite

Inorder to use the GPIO, an additional library will need to be installed.
This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).
