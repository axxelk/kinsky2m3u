# kinsky2m3u
convert Linn Kinsky Playlists to m3u

Using Linn DS devices to listen to music, controlled by Kinsky (the old one, not Kazoo) software on a Mac laptop left me with many painful created playlists in a xml format. Now using Roon I wanted/needed these playlists converted to m3u files. So I hacked this python script to do the job.

There may be simpler ways using grep/awk/.. but I did it this way. Too anxious to get the job done I altered the xml files in two parts because I wasn't able to get to the result without the changes.. there sure will be a pure lxml/xpath way :)

- on a Mac you can find your the local created Kinsky Playlists are in ~/Library/Kinsky/Playlists/
- there are some notes to myself in notes.py

Usage:

    axelk@hopl ~/Documents/src/python/lxml_test:$ ./kinky2m3u.py Playlists/20131013_234941.dpl.6T.dpl > x.m3u
    converting all Playlists to m3u playlists:
    axelk@hopl ~/Documents/src/python/lxml_test:$ for file in ./Playlists/*; do ./kinky2m3u.py $file > ./m3us/$(basename $file).m3u; done
    make one large playlist out of all playlist with no duplicates:
    axelk@hopl ~/Documents/src/python/lxml_test/m3us:$ cat * > all.m3u
    axelk@hopl ~/Documents/src/python/lxml_test/m3us:$ cat all.m3u | awk '!x[$0]++'  > kinsky_all3.m3u
