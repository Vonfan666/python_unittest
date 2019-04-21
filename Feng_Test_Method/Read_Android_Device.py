#driver反射
import platform,os,unittest,time,HTMLTestRunner,threading,logging,sys
from  appium import webdriver
from datetime import datetime
from Feng_Test_Conf.Feng_Test_confing import *
from Feng_Test_Method.Start_App_One import devicessCode,start_appium_one
from Feng_Test_Method.Start_Appium_Method import AppiumServer
from Feng_Test_Log.Log_Method import Log

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def read_android():
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
class start_App(object):
    @classmethod
    def PrintLog(self):
        Log()
        self.logger=logging.getLogger()
        return self.logger

    @staticmethod
    def appium_testcase(devices):
        desired_caps = {}
        # desired_caps['appPackage'] = devices["appPackage"]
        # desired_caps['appActivity'] = devices["appActivity"]
        desired_caps['udid'] = devices["deviceName"]
        desired_caps['app'] = devices['app']
        # desired_caps["recreateChromeDriverSessions"] = "True"
        # 解决多次切换到webview报错问题，每次切换到非chrome-Driver时kill掉session 注意这个设置在appium 1.5版本上才做了处理
        # desired_caps['automationName'] = devices["automationName"] # Xcode8.2以上无UIAutomation,需使用XCUITest
        # desired_caps['newCommandTimeout'] = 3600  # 1 hour
        desired_caps['platformVersion'] = devices["platformVersion"]
        desired_caps['platformName'] = devices["platformName"]
        desired_caps["automationName"] = devices['automationName']
        desired_caps['deviceName'] = devices["deviceName"]
        desired_caps["noReset"] = "True"
        desired_caps['noSign'] = "True"
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps["systemPort"] = devices["systemPort"]

        # desired_caps['app'] = devices["app"]
        remote = "http://127.0.0.1:" + str(devices["port"]) + "/wd/hub"
        # remote = "http://127.0.0.1:" + "4723" + "/wd/hub"
        driver = webdriver.Remote(remote, desired_caps)
        return driver




class TestCaseMethod(unittest.TestCase):   #让爸爸可以使用儿子的实例
    def __init__(self, methodName='runTest',param=None):
        super(TestCaseMethod, self).__init__(methodName)


    # @staticmethod
    # def methodlog():
    #     if len(read_android()) > 1:
    #         devicesName = devicess["deviceName"]
    #         logger = logging.getLogger(devicesName)
    #         return logger
    #     else:
    #         devicesName = devicessCode()[0]["deviceName"]
    #         logger = logging.getLogger(devicesName)
    #         return logger
    @staticmethod
    def Read_TestLoader_all(devices):
        global devicess
        devicess = devices
        case_dir = os.path.dirname(os.path.dirname(__file__)) + '/Feng_Test_Case/'
        allTest = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
        return allTest

    # @classmethod
    # def setUp(cls):
    #     cls.driver = appium_testcase(devicess)
    #     return cls.driver
    # @classmethod
    # def tearDown(cls):
    #     cls.driver = appium_testcase(devicess)
    #     cls.driver.quit()

    @classmethod
    def startDriver(cls):

        if len(read_android())>1:

            cls.driver = start_App.appium_testcase(devicess)
            return cls.driver
        else:  #执行一个模块用例需要用到这个
            cls.driver = start_App.appium_testcase(devicessCode()[0])
            return cls.driver

    @classmethod
    def FileDeviceName(cls):

        if len(read_android())>1:

            cls.name=devicess["deviceName"]
            return cls.name
        else:  #执行一个模块用例需要用到这个
            cls.name = devicessCode()[0]["deviceName"]
            return cls.name








            # @staticmethod
    # def read_file_test(TestFileName, param=None):
    #     # print("---parametrize-----")
    #     # print(param)
    #     testloader = unittest.TestLoader()
    #     testnames = testloader.getTestCaseNames(TestFileName)
    #     print(testnames)
    #     suite = unittest.TestSuite()
    #     for name in testnames:
    #         suite.addTest(TestFileName(name, param=param))
    #     print(suite)
    #     return suite

