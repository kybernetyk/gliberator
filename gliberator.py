#!/usr/bin/env python
# A little script to make G+ posts readable again
# It will remove the sluggish JavaScript interface and extract the HTML-only posts
# Then it will invoke 'open' on the extracted HTML to open it in the standard browser
#
# Note: I tested this only under OS X. 'open' is probably not present under Linux. Hack it!
# (c) Leon Szpilewski, Licensed under GPL3

import urllib2
import os
import sys

if len(sys.argv) != 2:
	print "G+ Post liberator.\n\tRemoves all the sluggish JS nonsense from posts.\nby Leon Szpilewski Licensed under GPL3"
	print "syntax: %s <url>" % (sys.argv[0])
	sys.exit(23)

url = sys.argv[1] 

data = str(urllib2.urlopen(url).read())

start = data.find('class="wm VC">') + len('class="wv VC">')
end = data.find("</div>", start)

f = open("output.html", "wt")
f.write(str(data[start:end]))
f.close()

os.system('open output.html')

os.system('rm output.html')
