# IMPORT MODULES.
import msvcrt

# DECLARE/INITIALIZE LOCAL VARIABLES.
special_char_indicator = 'e0'
button_key_00          = '52'
button_key_01          = '53'
key_prev               = ''

# INFINITE LOOP FOR APPLICATION.
while True:
	
	# Check to see if key was pressed.
	if msvcrt.kbhit():
		
		# Read in key value [in hex].
		key = msvcrt.getch().encode("hex")
		
		# Verify special key was observed.
		if(key_prev == special_char_indicator):
			
			# See if current key matches any acceptable values.
			if(key == button_key_00 or key == button_key_01):
				print "MATCH 00 " + key
		
		# Store current keypress for reference later.
		key_prev = key




