# 读取安卓设备信息
import os, re, unittest, random,HTMLTestRunner
from multiprocessing import Pool
from  platform import platform
from datetime import datetime
from  Feng_Test_Conf.Feng_Test_confing import *
from appium import webdriver
from Feng_Test_Method.Long_Used_Method import *
from Feng_Test_Method.Read_Android_Device import *
from Feng_Test_Method.Start_Appium_Method import AppiumServer
from Feng_Test_Method.Read_Android_Device import read_android

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def caps_list(deviceName):
    '''获取所有手机的信息以及所需要的端口支持生成独立的字典加入一个list'''
    devices_caps_List = []
    for i in range(0, len(deviceName)):
        List_desired_caps = {}
        List_desired_caps['platformName'] = conFIng['platformName']
        List_desired_caps['platformVersion'] = read_android()[i]['platformVersion']
        List_desired_caps['deviceName'] = read_android()[i]['deviceName']
        List_desired_caps['app'] = conFIng['app']
        List_desired_caps['appPackage'] = aPackage()
        List_desired_caps['appActivity'] = apActivity()
        List_desired_caps['noReset'] = conFIng['noReset']
        List_desired_caps['unicodeKeyboard'] = conFIng['unicodeKeyboard']
        List_desired_caps['resetKeyboard'] = conFIng['resetKeyboard']
        List_desired_caps['automationName'] = conFIng['automationName']
        List_desired_caps['newCommandTimeout'] = conFIng['newCommandTimeout']
        List_desired_caps["systemPort"] = deviceName[i]["systemPort"]
        List_desired_caps['port'] = deviceName[i]["port"]
        devices_caps_List.append(List_desired_caps)
    pool = Pool(len(devices_caps_List))
    pool.map(runnerCaseApp, devices_caps_List)
    pool.close()
    pool.join()




def runnerCaseApp(devices):
    #***********************************************************************
    # suite = unittest.TestSuite()
    # suite.addTest(TestCaseMethod.read_file_test(Test_login1, param=devices))
    # suite.addTest(TestCaseMethod.read_file_test(Test_login2, param=devices))
    # pathCode = os.path.dirname(os.path.dirname(__file__))+'/Feng_Test_Resut/'
    # curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # report_path = pathCode +devices['deviceName']+'-'+curtime + '.html'
    # report_set = open(report_path, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,
    #                                        title=u'自动化测试报告',
    #                                        description=u'用例执行情况：')
    # runner.run(suite)
    # report_set.close()
    # ***********************************************************************

    pathCode = os.path.dirname(os.path.dirname(__file__))+'/Feng_Test_Resut/'
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    report_path = pathCode +devices['deviceName']+'-'+curtime + '.html'
    report_set = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_set,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况：')
    runner.run(TestCaseMethod.Read_TestLoader_all(devices))
    report_set.close()


if __name__ == '__main__':
    kill_adb()
    deviceList = read_android()  # 获取设备list
    i = 0
    L=0
    if len(deviceList) > 0:
        l_devices = []
        for dev in deviceList:  # 获取设备相关参数用以启动appiumserver
            app = {}
            app["deviceName"] = deviceList[i]["deviceName"]
            installUT(deviceList[i]["deviceName"])
            app["port"] = str(conFIng['port']+L)
            app["bport"] = str(conFIng['bport']+L)
            app["systemPort"] = str(conFIng['systemPort']+L)
            app['chromedriverport'] = str(conFIng['chromedriverport']+L)
            l_devices.append(app)
            i = i + 1
            L=L+2
        appium_server = AppiumServer(l_devices)   #实例化AppiumServer
        appium_server.start_appium()  #启动appium服务
        caps_list(l_devices)           #执行用例并生成driver
        appium_server.stop_server(l_devices)
    else:
        print("没有可用的安卓设备")







