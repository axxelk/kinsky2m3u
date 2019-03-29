>>> from lxml import etree
>>> tree = etree.parse('pl.xml')
>>> namespaces={'l': 'urn:linn-co-uk/playlist', 'd': 'urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/', 'dc': 'http://purl.org/dc/elements/1.1/', 'upnp': 'urn:schemas-upnp-org:metadata-1-0/upnp/'}

>>> tree.xpath('/l:Playlist/l:Track/DIDL-Lite/item/dc:title', namespaces=namespaces)
[]



Nach verändern des xml files geht es dann..


axelk@hopl ~/Documents/src/python/lxml_test:$ cat pl.xml |grep -v DIDL-Lite > pl1.xml
axelk@hopl ~/Documents/src/python/lxml_test:$ vi pl1.xml
1,$s/item/linn:item/g

<linn:Playlist version="3" xmlns:linn="urn:linn-co-uk/playlist">
  <linn:Track>
      <linn:item id="/Users/axelk/Library/Kinsky/Playlists/20181128_193156.dpl/0" parentID="/Users/axelk/Library/Kinsky/Playlists/20181128_193156.dpl" restricted="False">
        <dc:title xmlns:dc="http://purl.org/dc/elements/1.1/">Sunn O))) - My Wall</dc:title>
        <dc:creator xmlns:dc="http://purl.org/dc/elements/1.1/">Sunn O)))</dc:creator>
        <upnp:class xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">object.linn:item.audioItem.musicTrack</upnp:class>
        <res size="117355002" duration="0:26:00.349" bitrate="176400" sampleFrequency="44100" bitsPerSample="16" nrAudioChannels="2" protocolInfo="http-get:*:audio/x-flac:DLNA.ORG_OP=01;DLNA.ORG_FLAGS=01700000000000000000000000000000">http://192.168.0.8:9790/minimserver/*/Syn3/45NEW/Sunn*20O)))*20-*202018*20-*20White1*20*5bRemastered*20Edition*5d/01.*20My*20Wall.flac</res>
        <upnp:albumArtURI xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">http://192.168.0.8:9790/minimserver/*/Syn3/45NEW/Sunn*20O)))*20-*202018*20-*20White1*20*5bRemastered*20Edition*5d/01.*20My*20Wall.flac/$!picture-3303-318190.jpg</upnp:albumArtURI>
        <upnp:genre xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">experimental</upnp:genre>
        <upnp:artist role="AlbumArtist" xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">Sunn O)))</upnp:artist>
        <upnp:artist xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">Sunn O)))</upnp:artist>
        <upnp:album xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">White1</upnp:album>
        <upnp:originalTrackNumber xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/">1</upnp:originalTrackNumber>
        <dc:date xmlns:dc="http://purl.org/dc/elements/1.1/">2018-01-01</dc:date>
      </linn:item>
  </linn:Track>


>>> tree = etree.parse('pl1.xml')
>>> tree.xpath('/l:Playlist/l:Track/l:item/dc:title', namespaces=namespaces)
>>> type(r)
<class 'list'>
>>> r[2]
<Element {http://purl.org/dc/elements/1.1/}title at 0x10600dd88>
>>> len(r)
965
>>> r[2].tag
'{http://purl.org/dc/elements/1.1/}title'
>>> dir(r[0])
['__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '_init', 'addnext', 'addprevious', 'append', 'attrib', 'base', 'clear', 'cssselect', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'getnext', 'getparent', 'getprevious', 'getroottree', 'index', 'insert', 'items', 'iter', 'iterancestors', 'iterchildren', 'iterdescendants', 'iterfind', 'itersiblings', 'itertext', 'keys', 'makeelement', 'nsmap', 'prefix', 'remove', 'replace', 'set', 'sourceline', 'tag', 'tail', 'text', 'values', 'xpath']
>>> r[2].text
'The Liminanas - The Mirror (feat. Kirk Lake)'
>>> r=tree.xpath('/l:Playlist/l:Track/l:item/@id', namespaces=namespaces)
>>> len(r)
965
>>> r[2]
'/Users/axelk/Library/Kinsky/Playlists/20181128_193156.dpl/2'

>>> r=tree.xpath('/l:Playlist/l:Track/l:item/res/@sampleFrequency', namespaces=namespaces)
>>> len(r)
965
>>> r[3]
'44100'


(venv) axelk@hopl ~/Documents/src/python/lxml_test:$ for file in ./Playlists/*; do ./kinsky2m3u.py $file > ./m3us/$(basename $file).m3u; done

