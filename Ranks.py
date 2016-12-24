#!/usr/bin/env python2
# Ranks.py - Launches ranklist of NIT Kurukshetra in any competition on CodeChef in the browser using a contest code from command line or clipboard

import webbrowser
import sys
import pyperclip
if len(sys.argv) > 1:
    # Get contest code from command line.
    code = sys.argv[1]	
else:
    # Get contest code from clipboard.
    code = pyperclip.paste()

webbrowser.open('https://www.codechef.com/rankings/' + code + '?filterBy=Institution%3DNational%20Institute%20of%20Technology%2C%20Kurukshetra&order=asc&sortBy=rank')