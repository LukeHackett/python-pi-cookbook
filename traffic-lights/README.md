Traffic Lights
-------

This simple project will demostrate a UK traffic light setup.
You will need:

* 3x LEDs (any colour, ideally red, amber and green)
* 3x Resistors (any suitable resistor for your chosen LEDs)
* 4x Jumper wires
* 1x Breadboard

** Note: ** it is possible to use more jumper wires to substitute not having a breadboard.


A example circuit diagram is shown below. I used GPIO pins 7, 8 and 24 however any GPIO pins can be used. If a different set of GPIO pins are to be used then the PIN values should be changed at the top of the file.

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/traffic-lights/breadboard_diagram.png) &nbsp;



### Python Library Prerequisite

Inorder to use the GPIO, an additional library will need to be installed. This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).
