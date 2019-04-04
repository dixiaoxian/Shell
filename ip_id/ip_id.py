#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
numip = []
num = [191,192,193,194,195,203,207,208,209,210,211,212,252,59,60]
for i in num:
    ipname = "192.168.1.%s" %i
    numip.append(ipname)

print("网络状态检查：".center(92,"-"))
for i in numip:
    if (i != "192.168.1.195"):
        print("当前服务器ip：%s".center(80,"-") %i)
        ipname = "ssh hadoop@%s ping 180.97.33.107 -c 1 -w 2 | grep 64" %i
        # print(ipname)
        if(i != "192.168.1.60"):
            os.system(ipname)
        else:
            print("这个是60服务器！")
    else:
        print("这是195服务器！")

print("网络-DNS-状态检查：".center(92,"-"))
for i in numip:
    if (i != "192.168.1.195"):
        print("当前服务器ip：%s".center(80,"-") %i)
        ipname = "ssh hadoop@%s ping www.baidu.com -c 1 -w 2 | grep 64" %i
        # print(ipname)
        if(i != "192.168.1.60"):
            os.system(ipname)
        else:
            print("这个是60服务器！")
    else:
        print("这是195服务器！")


