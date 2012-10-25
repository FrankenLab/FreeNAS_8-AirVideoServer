#!/bin/sh

AVS_HOME=/usr/pbi/avs-`uname -m`

mkdir -p ${AVS_HOME}/www
mkdir -p ${AVS_HOME}/mnt

# New strategy, put syncdb first to see if it works here
env -i ${AVS_HOME}/bin/python ${AVS_HOME}/avsUI/manage.py syncdb --migrate --noinput

echo libz.so.4 libz.so.5 > /etc/libmap.conf
echo libz.so.4 libz.so.5 > ${AVS_HOME}/etc/libmap.conf

mv ${AVS_HOME}/AirVideoServerLinux_246-Beta3.jar ${AVS_HOME}/sbin/AirVideoServer.jar
mv ${AVS_HOME}/test.properties ${AVS_HOME}/sbin/

mkdir -p ${AVS_HOME}/etc/avs/home
#mkdir /var/avs /var/music /var/playlists

#chown -R www:www /var/avs
#chown -R www:www /var/music
#chown -R www:www /var/playlists
#chown www:www ${AVS_HOME}/apache-tomcat-6.0/webapps/avs.war

# Script seems to break at this line, commenting out for now. (See typo now, unequal double-quotes)
#echo "tomcat60_java_opts="-Djava.awt.headless=true -Djava.net.preferIPv4Stack=true" >> /etc/rc.conf

#cp ${AVS_HOME}/etc/rc.d/ffserver /usr/local/etc/rc.d/
#cp ${AVS_HOME}/etc/rc.d/ffserver /etc/rc.d/
#cp ${AVS_HOME}/etc/rc.d/tomcat6 /usr/local/etc/rc.d/
#ln -sf ${AVS_HOME}/etc/rc.d/tomcat6 /usr/local/etc/rc.d/
#/usr/pbi/avs-amd64/etc/rc.d
#mv ${AVS_HOME}/avs_47.war ${AVS_HOME}/apache-tomcat-6.0/webapps/avs.war

#mkdir -p /var/avs/transcode
#ln -sf ${AVS_HOME}/bin/lame /var/avs/transcode/lame
#ln -sf ${AVS_HOME}/bin/lame /var/avs/transcode/
#ln -sf ${AVS_HOME}/bin/ffmpeg /var/avs/transcode/ffmpeg
#ln -sf ${AVS_HOME}/bin/ffmpeg /var/avs/transcode/
#ln -sf ${AVS_HOME}/bin/rtmpdump /var/avs/transcode/rtmpdump
#ln -sf ${AVS_HOME}/bin/rtmpdump /var/avs/transcode/
ldconfig -m ${AVS_HOME}/lib

mkdir -p ${AVS_HOME}/_MEDIA
chown www:www ${AVS_HOME}/_MEDIA
chmod 775 ${AVS_HOME}/_MEDIA


# The following 2 sed commands let AirVideo determine the Jail IP address and add it to the JAVA_OPTS used to start AirVideo

# William suggests just using 0.0.0.0
JAIL_IP=`ifconfig | grep -E 'inet.[0-9]' | grep -v '127.0.0.1' | awk '{ print $2}'` 

# Check if our hostname or ip address changed. Also make sure another plugin hasn't added it.
#if [ `grep -c $JAIL_IP /etc/hosts` -eq 0 ]
    echo $JAIL_IP"	"`hostname` >> /etc/hosts
#fi

echo 'avs_flags=""' >> ${AVS_HOME}/etc/rc.conf
echo 'avs_flags=""' >> /etc/rc.conf
