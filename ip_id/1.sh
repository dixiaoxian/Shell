#!/bin/bash
if [ $? -eq 0 ];then
	echo "服务器网络正常！"
else
	echo "服务器网络存在问题！"
fi 
