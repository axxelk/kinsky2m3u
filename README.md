# kinsky2m3u
convert Linn Kinsky Playlists to m3u

Using Linn DS devices to listen to music, controlled by the Kinsky (the old one, not Kazoo) software on a Mac laptop left me with many painful created playlists in a xml format. Now with using Roon I wanted/needed these playlists converted to m3u files. So I hacked this python script to do the job.

There may be simpler ways using grep/awk/.. but I did it this way. Too anxious to get the job done I altered the xml files in two parts because I wasn't able to get to the result without the changes.. there sure will be a pure lxml/xpath way :)

- on a Mac you can find your the local created Kinsky Playlists are in ~/Library/Kinsky/Playlists/
- there are some notes to myself in notes.py


