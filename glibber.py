#!/usr/bin/env python
# A little script to make G+ posts readable again
# It will remove the sluggish JavaScript interface and extract the HTML-only posts
# Then it will open the extracted HTML in your default web browser
#
# (c) Leon Szpilewski, Licensed under GPL3
#
# this script prints the article to stdout
# it's intended to be used with pandoc
#

import urllib2
import os
import platform
import sys

if len(sys.argv) != 2:
	print "G+ Post liberator.\n\tRemoves all the sluggish JS nonsense from posts.\nby Leon Szpilewski Licensed under GPL3"
	print "syntax: %s <url>" % (sys.argv[0])
	sys.exit(23)

url = sys.argv[1]

data = str(urllib2.urlopen(url).read())

start = data.find('class="wm VC">') + len('class="wv VC">')
end = data.find("</div>", start)

print data[start:end]
