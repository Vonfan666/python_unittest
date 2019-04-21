from  Feng_Test_Conf.Feng_Test_confing import *
from Feng_Test_Method.Long_Used_Method import *
from Feng_Test_Method.Start_Appium_Method import RunServer
from multiprocessing import Process
import requests

def read_android1():
    '''读取多有设备名称'''
    cmd = os.popen('adb  devices')
    I = cmd.readlines()
    devices_list = []
    for i in I:  # os.popen('adb  devices').readlines()打印出输入adb devices 所有的list，格式
        # ['List of devices attached\n', '2905bdb6\tdevice\n', 'MKJNW17C13050588\tdevice\n', '\n']
        devices = {}
        if 'List of devices' in i or 'adb' in i or 'daemon' in i or 'offline' in i or 'unauthorized' in i or len(i) < 5:
            pass
        else:
            deviceNameCode = re.findall('(.+?)\t', i)[0]  # 读取循环第一个设备
            devices['deviceName'] = deviceNameCode
            sys=os.popen('adb -s %s shell getprop ro.build.version.release' % deviceNameCode)
            sysCode=sys.readlines()[0]
            sysCode_1=re.findall('(.+?)',sysCode)
            platformVersionCode = ''.join(sysCode_1)  # 读取循环第一个设备的版本号
            devices['platformVersion'] = platformVersionCode
            devices_list.append(devices)
    # 返回demo：[{'platformVersion': '8.0.0', 'deviceName': 'MKJNW17C13050588'}, {'platformVersion': '7.1.2', 'deviceName': '2905bdb6'}]
    return devices_list

def start_appium_one():
    '''start the appium server'''

    if len(read_android1())==1:
        cmd = "appium -a 127.0.0.1  -p  %s  -bp %s --chromedriver-port %s -U %s --session-override" % (
        conFIng['port'], conFIng['bport'], conFIng['chromedriverport'],read_android1()[0]['deviceName'])
        if 'Windows' in platform.platform():
            t1 = RunServer(cmd)  # 添加线程组
            p = Process(target=t1.start())
            p.start()  # 启动进程
            while 1:
                print("********************start_server**************************")
                try:

                    requests.get("http://127.0.0.1:" + str(conFIng['port']) + "/wd/hub" + "/status")
                    print('************************start_server_success')
                    break
                except:
                    continue
        else:
            print('****************其他操作系统环境暂未适配***********************')
    else:
        pass



def devicessCode():  #单设备调试
    a=read_android1()
    devices_caps_List = []
    L=0
    for i in range(0, len(a)):
        List_desired_caps = {}
        List_desired_caps['udid'] = a[i]["deviceName"]
        List_desired_caps['deviceName'] = a[i]['deviceName']
        List_desired_caps['app'] = conFIng['app']
        List_desired_caps['platformName'] = conFIng['platformName']
        List_desired_caps['platformVersion'] = a[i]['platformVersion']
        List_desired_caps['automationName'] = conFIng['automationName']

        List_desired_caps['appPackage'] = aPackage()
        List_desired_caps['appActivity'] = apActivity()
        List_desired_caps['noReset'] = conFIng['noReset']
        List_desired_caps['unicodeKeyboard'] = conFIng['unicodeKeyboard']
        List_desired_caps['resetKeyboard'] = conFIng['resetKeyboard']

        List_desired_caps['newCommandTimeout'] = conFIng['newCommandTimeout']
        List_desired_caps["systemPort"] = str(conFIng['systemPort']+L)
        List_desired_caps['port'] = str(conFIng['port']+L)
        devices_caps_List.append(List_desired_caps)
        L=L+1
    return devices_caps_List

