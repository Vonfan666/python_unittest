#多进程启动appium# -*- coding: utf-8 -*-
import os
import socket

from multiprocessing import Process
import time
import platform,requests
import subprocess,threading
from Feng_Test_Method.Start_App_One import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppiumServer(object):
    def __init__(self,kwargs=None): #self自动添加形参
        self.kwargs=kwargs

    def start_appium(self):
        '''start the appium server'''
        '''cmd = 'appium -a 127.0.0.1  -p  %s  -bp %s --chromedriver-port %s -U %s --session-override'''
        for i in  range(0,len(self.kwargs)):
            cmd ="appium -a 127.0.0.1  -p  %s  -bp %s --chromedriver-port %s -U %s --session-override" % (
            self.kwargs[i]["port"], self.kwargs[i]["bport"], self.kwargs[i]['chromedriverport'],self.kwargs[i]["deviceName"])  #[port:port,bart:bport,devices}]
            if 'Windows' in  platform.platform():
                t1=RunServer(cmd) #添加线程组
                p = Process(target=t1.start())
                p.start()  #启动进程

                print('Process (%s) start...' % os.getpid())
                while 1:
                    print("********************start_server**************************")
                    try:

                        requests.get("http://127.0.0.1:" + self.kwargs[i]["port"] + "/wd/hub" + "/status")
                        print('************************start_server_success')
                        break
                    except:
                        continue
            else:
                print('****************其他操作系统环境暂未适配***********************')

    def stop_appium(self):
        os.popen("taskkill /f /im node.exe")



    def stop_server(self, devices):
        sysstr = platform.system()

        if sysstr == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            for device in devices:
                # mac
                cmd = "lsof -i :{0}".format(device["port"])
                plist = os.popen(cmd).readlines()
                plisttmp = plist[1].split("    ")
                plists = plisttmp[1].split(" ")
                # print plists[0]
                os.popen("kill -9 {0}".format(plists[0]))
class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)



if __name__=='__main__':
    pass


