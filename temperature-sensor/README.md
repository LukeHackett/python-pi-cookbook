Temperature Sensor (Version 1)
-------

This project will demonstrate a simple use of a temperature sensor. The 
project has been based upon an example project that has been provided 
by Cambridge University.

This project could be thought of as an "early warning system". The hardware
and software setup will continuously monitor the temperature, and indicate 
whether or not the temperature is correct for the given environment. 

An LED corresponding to whether or not the room is too hot, too cold or just
right will light up after each reading is made. The LED will remain illuminated 
until the temperature within the room has changed, and hence an alternative 
LED will light up.


### Ingredients

* 1x DS18B20 temperature sensor
* 3x LEDs (any colour, ideally red, green and blue)
* 4x Resistors (any suitable resistor for your chosen LEDs, plus 1x 4.7K ohm for the sensor)
* 1x Breadboard
* A number of jumper wires

**Note:** it is possible to use more jumper wires to substitute not having a 
breadboard.


### Recipe

1. Connect GPIO 7 to a resistor, and then connect the resistor to the red LED.
2. Connect GPIO 8 to a resistor, and then connect the resistor to the green LED.
3. Connect GPIO 25 to a resistor, and then connect the resistor to the blue LED.
4. Connect PIN 1 of the DS18B20 to 0V/Ground
5. Connect PIN 2 of the DS18B20 to GPIO 4
6. Connect PIN 3 of the DS18B20 to +3.3V.
7. A 4.7K ohm resistor must be placed between PIN 2 and PIN 3 in order to for 
the sensor to work.

The digram below is provided by Cambridge University's Computer Laboratory, 
and may help to understand the pin layout of the DS18B20:

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/temperature-sensor/sensor_connection.png) &nbsp; </center>

**Note:** A different set of GPIO pins can be used, to which the software will 
need to be updated to the new value(s).


#### Circuit Diagram

<center>![Hi](https://raw.github.com/LukeHackett/python-pi-cookbook/master/temperature-sensor/breadboard_diagram.png) &nbsp; </center>

**Note:** In the circuit digram above, I have substituted the DS18B20 for a 
thyristor. This is obviously an incorrect use of a thyristor, but has been 
used for diagrammatic purposes due to my software not supporting the DS18B20 
component.


### Python Library Prerequisite

In order to use the GPIO, an additional library will need to be installed.
This library can be obtained here: [https://code.google.com/p/raspberry-gpio-python/](https://code.google.com/p/raspberry-gpio-python/).


### Sources

* [Matthew Kirk, Cambridge University Computer Laboratory](http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/).
