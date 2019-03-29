#!/usr/bin/env python

import re
import sys
from io import StringIO
from lxml import etree
from urllib.parse import unquote


if len(sys.argv) != 2:
	print("please provide a filename of a Kinsky dpl/xml playlist")
	print("on a Mac these can be found in ~/Library/Kinsky/Playlists/")
	sys,exit(1)

fd = open(sys.argv[1],"r")
content = fd.read()

# replace item with linn:item to make lxml recognize it
content = content.replace("<item ","<linn:item ")
content = content.replace("</item>","</linn:item>")

# remove DIDL-Lite lines for lxml
content = re.sub(r'\s*</?DIDL-Lite.*?>', "", content)


namespaces={'l': 'urn:linn-co-uk/playlist', 'd': 'urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/', 'dc': 'http://purl.org/dc/elements/1.1/', 'upnp': 'urn:schemas-upnp-org:metadata-1-0/upnp/'}
tree = etree.parse(StringIO(content))
r = tree.xpath('/l:Playlist/l:Track/l:item/res', namespaces=namespaces)

# print(r[2].text)

for i in range(len(r)):
	fname = r[i].text
	fname = fname.replace("*","%")
	fname = unquote(fname)
	matchobj = re.match(r'.*DLNA-PNMP3-OP01-FLAGS.*', fname, re.I)
	if matchobj:
		continue
	fname = re.sub(r'^http.*(Musicshare/|Syn3/|Musik/|minimserver/%/)', "", fname)
	print(fname)
	# print(str(i) + " :: " + fname)




# print(content)

