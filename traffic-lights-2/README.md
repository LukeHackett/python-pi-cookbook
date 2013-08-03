Traffic Lights V2
-------

This simple project will demonstrate a UK traffic light setup, that handles pedestrians crossing the road.

You will need:

* 5x LEDs (any colour, ideally 2x red, 1x amber and 2x green)
* 5x Resistors (any suitable resistor for your chosen LEDs)
* 1x push-to-make button
* 1x Breadboard
* A selection of jumper wires

A example circuit diagram is shown below. I used GPIO pins 18, 23 and 24 for the traffic lights, GPIO pins 25 and 8 for the pedestrian lights, and GPIO pin 7 for the pedestrian button.

This simple project will highlight the use of callback functions, as well as handling user input via a button.

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/traffic-lights-2/breadboard_diagram.png) &nbsp;
</center>


### Python Library Prerequisite

In order to use the GPIO functionality, an additional library will need to be installed. This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).
