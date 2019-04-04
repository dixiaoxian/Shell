#!/bin/bash
. /etc/profile
#. ~/.bash_profile

jps | grep Maxwell > /dev/null
if [ $? -gt 0 ];then
	/home/hadoop/maxwell-1.19.1/bin/maxwell --user='maxwell' --password='123asd123asd' --host='localhost' --producer=kafka --kafka.bootstrap.servers=192.168.1.208:9092,192.168.1.211:9092,192.168.1.212:9092 >> /home/hadoop/Maxwell_log.txt 2>&1 &
fi
