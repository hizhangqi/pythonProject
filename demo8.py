#!/usr/bin/python3

import time;  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)


localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
