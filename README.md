FreeNAS_8-AirVideo
==================

AirVideo Plugin for FreeNAS 8

NOTES:

Will probably need to copy wrapper & rc script from Serviio to use for this plugin.

The version b25_1 is incorrect, it is the version from openjdk6 since I used that as my base port since airvideoserver
doesn't have a FreeBSD port.

Might also need to use scripts/pre-portmake.sh

(Needs updated libav build) 

FFMpeg configure command line: 
(Some of these can be set using "make config" in the /usr/ports/multimedia/ffmpeg
./configure --enable-pthreads --disable-shared --enable-static --enable-gpl --enable-libx264 --enable-libmp3lame 

(Libav doesn't have a separate port, it's built with ffmpeg)
libav configure command line (for 2.4.6-beta3): 
./configure --enable-pthreads --disable-shared --enable-static --enable-gpl --enable-libx264 --enable-libmp3lame --enable-nonfree --enable-encoder=libfaac 
