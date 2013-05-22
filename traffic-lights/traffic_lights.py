import time
import RPi.GPIO as GPIO

# LED constants
RED_LED = 7
AMB_LED = 8
GRE_LED = 25

# Initialise the board
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Initialise the pins
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(AMB_LED, GPIO.OUT)
GPIO.setup(GRE_LED, GPIO.OUT)

try:
	while(True):
		# Force cars to stop (RED)
		GPIO.output(RED_LED, GPIO.HIGH)
		time.sleep(2)
		
		# Allow cars to start moving (RED/AMBER)
		GPIO.output(AMB_LED, GPIO.HIGH)
		time.sleep(2)
		
		# All cars can go (GREEN) 
		GPIO.output(RED_LED, GPIO.LOW)
		GPIO.output(AMB_LED, GPIO.LOW)
		GPIO.output(GRE_LED, GPIO.HIGH)
		time.sleep(5)
		
		# Traffic should slow (AMBER)
		GPIO.output(GRE_LED, GPIO.LOW)
		GPIO.output(AMB_LED, GPIO.HIGH)
		time.sleep(2)
		
		# Turn off led for the return
		GPIO.output(AMB_LED, GPIO.LOW)
		
except (KeyboardInterrupt, SystemExit):
	print "CTRL-C pressed: turning all LEDS off, and cleaning up"
	
	# Turn the LEDs off
	GPIO.output(RED_LED, GPIO.LOW)
	GPIO.output(AMB_LED, GPIO.LOW)
	GPIO.output(GRE_LED, GPIO.LOW)
	
	# Reset the PINs
	GPIO.cleanup()

	print "All done."
