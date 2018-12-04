"""
python script to open google map 
in a browser for an address 
input from command line or copy from clipboard
"""

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])


else:
	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://maps.google.com/maps/place/' + address)


