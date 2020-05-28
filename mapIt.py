#! python3
#mapIt.py - Launches a map in the browser using an address from command line

import webbrowser, sys, pyperclip
if len(sys.argv) >1:
    #get address from command line
    address = ' '.join(sys.argv[1:])
#webbrowser to launch web, sys to read command line stuff
#ensuring the command line arguments (>1) are all accounted for
else:
    #get address from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
#



