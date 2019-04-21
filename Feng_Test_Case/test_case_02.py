import unittest,os,random,subprocess,HTMLTestRunner,logging
from Feng_Test_Method.Read_Android_Device import TestCaseMethod
from Feng_Test_Method.Read_Android_Device import start_App
from Feng_Test_Method.Start_Appium_Method import *
from Feng_Test_Conf.Feng_Test_confing import *
from Feng_Test_Method.Start_App_One import start_appium_one

class Test_login2(TestCaseMethod):
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


    def test_08(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_index_login').click()
        self.logger.info('testcase0211111111111111111111111111111111')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_login_username').set_text('13590283182')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_loing_password').set_text('123456')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_submit').click()
    def test_09(self):
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_index_login').click()
        self.logger.info('testcase0222222222222222222222222222222221')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_login_username').set_text('13590283182')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/ulet_loing_password').set_text('123456')
        time.sleep(5)
        self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/tv_login_submit').click()

if __name__=='__main__':
    unittest.main()