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

import datetime, time, shiftpi
#from shiftpi import HIGH, LOW, digitalWrite, delay
#import RPi.GPIO

# Set the number of registers
shiftpi.shiftRegisters(3)

"""Return an int

This method will convert a given decimal number to binary, with the given 
number of leading 0's before the binary number.

"""
def decimalToBinary(num, leading):
	if num >= 0:
		return str(bin(num))[2:].zfill(leading)
	else:
		return "-" + str(bin(num)[3:].zfill(leading))


"""Returns a map of ints

This method will convert a given binary number to a map of indiviual digits

"""
def decimalToBinaryMap(num, leading):
	bin_num = decimalToBinary(num, leading)
	return map(int, str(bin_num))


"""Returns a tuple of ints

This method will split a given positive, non-zero number into each of the 
individual comprising integers.

"""
# Splits a number into an n-length tuple
def splitNumber(number):
	strnum = str(number)
	length = len(strnum)
	integers = ()

	# Return the number as a tuple if on it's own
	if length == 1:
		return (0, number)
	
	# Loop over all integers in the number
	for i in xrange(0, length):
		integers += (int(strnum[i]),)

	return integers


try:
	while True:
		# Clear LEDs
		shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

		# Obtain the current date and time
		now = datetime.datetime.now()

		# Split the time value
		(sec1, sec2) = splitNumber(now.second)
		(min1, min2) = splitNumber(now.minute)
		(hrs1, hrs2) = splitNumber(now.hour)

		# Convert decimal to binary maps
		bin_hrs1 = decimalToBinaryMap(hrs1, 2)
		bin_hrs2 = decimalToBinaryMap(hrs2, 4)
		bin_min1 = decimalToBinaryMap(min1, 3)
		bin_min2 = decimalToBinaryMap(min2, 4)
		bin_sec1 = decimalToBinaryMap(sec1, 3)
		bin_sec2 = decimalToBinaryMap(sec2, 4)
		
		# Print hours - TENs
		shiftpi.digitalWrite(1, bin_hrs1[0])
		shiftpi.digitalWrite(2, bin_hrs1[1])

		# Print hours - UNITs
		shiftpi.digitalWrite(7, bin_hrs2[0])
		shiftpi.digitalWrite(6, bin_hrs2[1])
		shiftpi.digitalWrite(5, bin_hrs2[2])
		shiftpi.digitalWrite(4, bin_hrs2[3])

		# Print minutes - TENs
		shiftpi.digitalWrite(9, bin_min1[0])
		shiftpi.digitalWrite(10, bin_min1[1])
		shiftpi.digitalWrite(11, bin_min1[2])

		# Print minutes - UNITs		
		shiftpi.digitalWrite(15, bin_min2[0])
		shiftpi.digitalWrite(14, bin_min2[1])
		shiftpi.digitalWrite(13, bin_min2[2])
		shiftpi.digitalWrite(12, bin_min2[3])

		# Print seconds - TENs
		shiftpi.digitalWrite(17, bin_sec1[0])
		shiftpi.digitalWrite(18, bin_sec1[1])
		shiftpi.digitalWrite(19, bin_sec1[2])
		
		# Print seconds - UNITs
		shiftpi.digitalWrite(23, bin_sec2[0])
		shiftpi.digitalWrite(22, bin_sec2[1])
		shiftpi.digitalWrite(21, bin_sec2[2])
		shiftpi.digitalWrite(20, bin_sec2[3])
		
		# Wait for one second - slightly hacky!
		time.sleep(1)


except (KeyboardInterrupt, SystemExit):
	print "CTRL-C pressed: turning all LEDS off, and cleaning up"

	# Clear all LEDs
	shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)

	print "All done."
