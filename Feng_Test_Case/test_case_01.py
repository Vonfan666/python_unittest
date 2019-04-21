import unittest,os,random,subprocess,HTMLTestRunner,logging
from Feng_Test_Method.Read_Android_Device import TestCaseMethod
from Feng_Test_Method.Read_Android_Device import start_App
from Feng_Test_Method.Start_Appium_Method import *
from Feng_Test_Conf.Feng_Test_confing import *
from Feng_Test_Method.Start_App_One import start_appium_one
from Feng_Test_Method.Long_Element_Method import StartMethod

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
# cmd = "appium -a 127.0.0.1  -p  %s  -bp %s --chromedriver-port %s -U %s --session-override" % (
#                 conFIng['port'], conFIng['bport'], conFIng['chromedriverport'],
#                 read_android()[0]['deviceName'])  # [port:port,bart:bport,


class Test_login1(TestCaseMethod):

    @classmethod
    def setUpClass(cls):

        start_appium_one() #用于单设备执行,单设备或多设备全部执行注释这行
        pass
    def setUp(self):
        self.logger = start_App.PrintLog()
        self.driver=TestCaseMethod.startDriver()
    def tearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls):
        # AppiumServer().stop_appium()  #单设备执行单用例加上这个关闭appium
        pass

    def test_01(self):
        time.sleep(5)
        StartMethod(self.driver).action_Id('com.henji.yunyi.yizhibang:id/tv_login_index_login','click')
        self.logger.info('11111111111111111111111111111111111111111111')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_login_username').set_text('13590283182')
        self.logger.info('22222222222222222222222222222222222222222222222')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_loing_password').set_text('123456')
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_submit').click()
    def test_03(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_index_login').click()
        self.logger.info('11111111111111111111111111111111111111111111')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_login_username').set_text('13590283182')
        self.logger.info('2222222222222222222222222222222222222222222222222222')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_loing_password').set_text('123456')
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_submit').click()


if __name__=='__main__':
    unittest.main()






