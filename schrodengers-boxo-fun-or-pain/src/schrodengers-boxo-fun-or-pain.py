## IMPORT MODULES REQURED FOR FILE ##
import os, sys								# OS/System info.
import tty, termios							# Used for polling keyboard.
import random, time							# Used for fun or pain randomness && timing.




## DEFINE GLOBAL VARIABLES ##
last_key_press_time	= time.time()			# Time since last key press.




## 
## FUNCTION DEFINTION => DO NOTHING
## 
## PURPOSE:	Mainly a placeholder function. Called when 'nothing' occurs due to button press.
## 
## INPUTS:	NONE.
## 
## RETURNS:	NONE.
## 
def do_nothing():
	
	# Print notification message that nothing important happened.
	print "Nothing To See Here.\r"
	
	# :: EXIT ::
	return




## 
## FUNCTION DEFINTION => DO NOTHING
## 
## PURPOSE:	Mainly a placeholder function. Called when 'nothing' occurs due to button press.
## 
## INPUTS:	NONE.
## 
## RETURNS:	NONE.
## 
def pain():
    
	# Print notification message that the pain is beginning.
	print "Entering The House Of Pain.\r"
	
	## TO DO => TOGGLE STATUS OF INSERT [LED] ##
	
	# :: EXIT ::
	return




## 
## FUNCTION DEFINTION => DO NOTHING
## 
## PURPOSE:	Mainly a placeholder function. Called when 'nothing' occurs due to button press.
## 
## INPUTS:	NONE.
## 
## RETURNS:	NONE.
## 
def fun():
	 
	# Print notification message that the fun is going to be attempted.
	print "Attempting Fun Times.\r"
	
	## TO DO => TOGGLE STATUS OF NUMLOCK [LED] ##
	
	# :: EXIT ::
	return




## 
## FUNCTION DEFINTION => FUN OR PAIN
## 
## PURPOSE:	Randomly determine if time for fun or pain.
## 
## INPUTS:	NONE.
## 
## RETURNS:	NONE.
## 
def fun_or_pain():
	
	# Declare global variables used in function.
	global last_key_press_time
	
	# Declare/Initialize Local Vars.
	required_wait_time	= 1						# Required time (in seconds) to wait between button presses.
	
	# Get current timestamp.
	timestamp = time.time()
	
	# Map functions from random number results to function calls.
	#  NOTE:  to skew/alter probabilities, simply add extra items to list [unique numbers (indexes) with duplicate functions (vars)].
	fun_or_pain_chance	= {
		1 : fun,
		2 : pain,
		3 : fun,
		4 : do_nothing
	}
	
	# :: CHECK :: Verify enough time has elapsed between button presses. ::
	if (timestamp - last_key_press_time) < required_wait_time:
		
		# Invoke the PAIN.
		pain()
		
	else:
		
		# Get random integer value to determine what should be done:
		fp = random.randint(fun_or_pain_chance.keys()[0], len(fun_or_pain_chance))
		
		# Execute Fun or Pain.
		fun_or_pain_chance[fp]()
	
	# Record current timestamp for reference on next function call.
	last_key_press_time = timestamp
	
	# :: EXIT ::
	return




## 
## FUNCTION DEFINTION => POLL KEYBOARD
## 
## PURPOSE:	Poll keyboard and return value for every keypress.
## 
## INPUTS:	'mode_hex' => When True returns HEX value for character found.
## 
## RETURNS:	Character as ascii || hex [based on flag].
## 
def poll_kbd(mode_hex=False):
	
	# Define file descriptor.
	fd = sys.stdin.fileno()
	
	# Recurrent current file descriptor settings for future reference.
	fd_settings_old = termios.tcgetattr(fd)
	
	# Use try-catch-finally method for grabbing data from keypress.
	try:
		
		# Change mode of file descriptor to raw.
		tty.setraw(sys.stdin.fileno())
		
		# Read in character from standard input.
		ch = sys.stdin.read(1)
	
	finally:
		
		# Character read successfully.
		# Return file descriptor to original settings.
		termios.tcsetattr(fd, termios.TCSADRAIN, fd_settings_old)
		
		# Return value read in.
		if mode_hex is True:
			return ch.encode('hex')
		else:
			return ch
	
	# :: EXIT ::
	return ""




## 
## FUNCTION DEFINTION => MAIN APPLICATION
## 
## PURPOSE:	Continually poll keyboard and invoke 'fun_or_pain' when a valid key is pressed.
## 
## INPUTS:	'mode_hex' => When True returns HEX value for character found.
## 
## RETURNS:	Character as ascii || hex [based on flag].
## 
def main():
	
	# Declare variables used in this function.
	escape_key				= '03'
	button_key_sequence_00	= ['1b', '5b', '32', '7e']  # KEY-LIST => INSERT
	button_key_sequence_01	= ['1b', '5b', '33', '7e']	# KEY-LIST => DELETE
	button_key_index        = 0x00						# INDEX INTO KEY-LIST
	
	# Infinite loop for application.
	while True:
		
		# Poll for keypress.
		key = poll_kbd(True)
		
		# Check to see if 'CTRL+c' [escape] was requested.
		if key == escape_key:
			break
		
		# :: CHECK :: See if current keypress corresponds to return value from button 00. ::
		if button_key_sequence_00[button_key_index] == key:
			
			# :: CHECK :: See if full sequence has been reached for keypress. ::
			if (len(button_key_sequence_00) - 1)  == button_key_index:
				
				# Key has been found; Reset index.
				button_key_index = 0x00
				
				# Time to see if fun time or pain time.
				fun_or_pain()
			
			# More remains in key list -> increment index.
			else:
				button_key_index += 1
		
		# :: CHECK :: See if current keypress corresponds to return value from button 01. ::
		elif button_key_sequence_01[button_key_index] == key:
			
			# :: CHECK :: See if full sequence has been reached for keypress. ::
			if (len(button_key_sequence_01) - 1)  == button_key_index:
				
				# Key has been found; Reset index.
				button_key_index = 0x00
				
				# Time to see if fun time or pain time.
				fun_or_pain()
			
			# More remains in key list -> increment index.
			else:
				button_key_index += 1
		
		# Incorrect key pressed -> reset index.
		else:
			button_key_index = 0x00
	
	# :: EXIT ::
	return




## INVOKE MAIN FUNCTION ##
main()




