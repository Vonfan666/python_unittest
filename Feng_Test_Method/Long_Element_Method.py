#定位元素二次封装
from Feng_Test_Method.Read_Android_Device import start_App
import  redis
#from selenium import webdriver
import time,re
import random
import  os
from appium.webdriver.common.touch_action import TouchAction #导入Touch Action类   这个是支持手势操作
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd#读取
from xlutils.copy import copy#复制写入
from selenium.webdriver.support import *
from pyocr import pyocr
from PIL import Image
import traceback
import pymysql,unittest,HTMLTestRunner


class StartMethod(object):

    def __init__(self,driver):
        self.driver=driver
        self.logger=start_App.PrintLog()

    def action_Id(self, id, text):
        '''封装ID获取元素'''
        if text == 'obtain':
            pro = '获取元素：'
            self.logger.info(u'>>>%s%s' % (pro, id))
            return self.driver.find_element_by_id(id)
        else:
            if text == 'click':
                pro = '点击控件：'
                self.logger.info(u'>>>%s%s' % (pro, id))
                return self.driver.find_element_by_id(id).click()
            else:
                pro = '输入内容为：'
                self.logger.info(u'>>>定位控件%s,%s%s' % (id, pro, text))
                return self.driver.find_element_by_id(id).set_text(text)

    def longClear(self, element, time):
        '''element长按元素 time长按时间'''
        action = TouchAction(self.driver)
        action.press(element).wait(time).release()
        action.perform()

    def dianJi_ClassText_ShuRu(self, driver, className, text, txtUsername):
        '''方法包装_通过当前页面:classname+text定位控件并完成输入'''
        allClassNames = driver.find_elements_by_class_name(className)  # 定义所有该className下所有控件为 allclassname
        for allClassName in allClassNames:
            print(allClassName.text)
            if text in allClassName.text:  # 当text的值属于  遍历出来当中的一个text值时，则为我们需要的值
                allClassName.set_text(txtUsername)
                break

    def dianJi_classText(self, driver, className, text):
        '''封装一个根据clsaa+text的方法点击控件 '''
        clickClassName = self.driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                clickclassNameOne.click()
                break

    def huoQu_classText(self, className, text):
        '''封装一个根据class+text的方法获取元素'''
        clickClassName = self.driver.find_elements_by_class_name(className)
        for clickclassNameOne in clickClassName:
            if text in clickclassNameOne.text:
                print(text)
                print(clickclassNameOne)
                self.logger.info(text)
                break
            else:
                self.logger.info('未获取到元素')


    def huoQu_className(self, className):
        '''封装一个获取className的方法（className唯一）'''
        return self.driver.find_element_by_class_name(className)



    def scroll_resourceId(self, id, textCode):
        '''封装一个滑动当前页面查找元素方法'''
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().resourceId("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
                id, textCode))



    def scroll_classText(self, classNameCode, textCode):
        '''封装一个滑动当前页面class+text查看元素方法'''
        self.driver.find_element_by_android_uiautomator((
            'new UiScrollable(new UiSelector().className("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
                classNameCode, textCode)))



    def scroll_my(self, x1, y1, x2, y2, element, type, timeOut):
        '''无限各方为滑动加载获取指定元素'''
        timeStart = time.strftime('%d%H%M%S', time.localtime())
        while 1:
            try:
                if type == 'id':
                    self.driver.find_element_by_id(element)
                else:
                    self.driver.find_element_by_xpath(element)
                self.logger.info('获取到指定元素')
                break
            except:
                action = TouchAction(self.driver)
                action.press(x=x1, y=y1).wait(ms=1000).move_to(x=x2, y=y2).release()
                action.perform()
                timeOver = time.strftime('%d%H%M%S', time.localtime())
                if int(timeOver) - int(timeStart) >= int(timeOut):
                    self.logger.debug('抓取指定元素超时，抓取时间为：%s' % (int(timeOver) - int(timeStart)))
                    break
                else:
                    continue
        if type == 'id':
            return self.driver.find_element_by_id(element)
        else:
            return self.driver.find_element_by_xpath(element)



    def toachSweip(self, x, y, x1, y1):
        '''封装一个滑动toach的方法'''
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(ms=1000).move_to(x=x1, y=y1).release()
        action.perform()
    def find_toast(self, message):
        '''封装获取toast方法'''
        toast_Code = ('xpath', './/*[contains(@text,"%s")]' % message)
        t = WebDriverWait(self.driver.driver, 5, 0.1).until(EC.presence_of_element_located(toast_Code))
        self.logger.info('获取到toast:{}'.format(t))


    def clickXY(self, x, y):
        '''封装点击坐标的方法'''
        x1 = x / 720  # 获取宽度比例
        y1 = y / 1280  # 获取高度比例
        a1 = self.driver.get_window_size()['width']  # 获取当前屏幕宽度
        b1 = self.driver.get_window_size()['height']  # 获取当前屏幕高度
        x2 = int(a1 * x1)  # 计算当前屏幕点击横坐标
        y2 = int(b1 * y1)  # 计算当前屏幕点击纵坐标
        self.driver.tap([(x2, y2)])  # 点击


    '''封装手机屏幕适配'''

    def androidSize(self, a, b):
        a1 = a / 720
        b1 = b / 1280
        x1 = self.driver.get_window_size()['width']
        y1 = self.driver.get_window_size()['height']
        m = x1 * a1
        n = y1 * b1
        return self.driver.tap([(m, n)])



    '''等待定位元素'''
    def wait_time(self, resourceid, waitTime=None):
        try:
            if waitTime == None:
                waitTime = 10
            WebDriverWait(self.driver,waitTime).until(lambda driver: self.driver.find_element_by_id(resourceid))
            self.logger.info(u'>>>检测到{},页面未跳转成功'.format(resourceid))
        except Exception as f:
            print(f)
            self.logger.info(u'>>>未检测到{},页面跳转成功'.format(resourceid))

    '''封装一个切换WebView和native方法'''
    def ChangeWebView(self, n):
        contexts = self.driver.contexts
        self.logger.info('页面类型：{}'.format(contexts))
        self.driver.switch_to.context(n)
        self.logger.info('已切换为：{}'.format(self.driver.current_context))

class ElementMethod(object):
    def __init__(self,driver):
        self.driver=driver
        self.logger=start_App.PrintLog()

    # '''封装登录易直帮app方法'''
    # def loginYiZhiBang(self, a, b):
    #     StartMethod(self).action_Id(login['账号id'], 'obtain').clear()  # 清除账号输入框
    #     StartMethod(self).action_Id(login['密码id'], 'obtain').clear()  # 清除密码输入框
    #     self.logger.info('初始化登录框完成')
    #     self.driver.find_element_by_id(login['账号id']).set_text(a)
    #     self.logger.info('输入账号为{}'.format(a))
    #     self.driver.find_element_by_id(login['密码id']).set_text(b)
    #     self.logger.info('输入密码为{}'.format(b))
    #     self.driver.find_element_by_id(login['登录id']).click()
    #     self.logger.info('点击登录按钮')
    #     try:
    #         WebDriverWait(self, 20).until(
    #             lambda driver: StartMethod(self).action_Id(bottom['我的id'], 'obtain'))  # 验证页面是否正常跳转成功
    #         self.logger.info('登录成功')
    #     except:
    #         self.logger.info('登录失败')

    # '''封装退出易直帮APP方法'''
    # def backCode(self):
    #     while True:
    #         try:
    #             WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_id(flash['取消id']))
    #             self.driver.find_element_by_id(flash['取消id']).click()
    #             self.logger.info('获取到取消按钮，点击取消')
    #         except:
    #             pass
    #         try:
    #             WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_id(flash['确定id']))
    #             StartMethod(self.driver).action_Id(flash['确定id'], 'click')
    #             self.logger.info('获取到确定按钮，点击确定')
    #         except:
    #             pass
    #         try:
    #             WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_id(flash['页面返回id']))
    #             self.driver.find_element_by_id(flash['页面返回id']).click()
    #             time.sleep(1)
    #             self.logger.info('获取到返回按钮，点击返回')
    #         except:
    #             break
    #     try:
    #         WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(bottom['我的id']))
    #         try:
    #             StartMethod(self.driver).action_Id(bottom['我的id'], 'click')
    #             WebDriverWait(self, 10).until(
    #                 lambda driver: self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]'))
    #         except:
    #             self.assertEqual(1, 2, msg='网络异常')
    #         try:
    #             self.driver.find_element_by_xpath('//android.widget.TextView[@text=\"设置\"]').click()
    #             WebDriverWait(self, 10).until(
    #                 lambda driver: self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit'))
    #             self.driver.find_element_by_id('com.henji.yunyi.yizhibang:id/btn_setting_exit').click()
    #         except:
    #             self.assertEqual(1, 2, msg='网络异常')
    #     except:
    #         WebDriverWait(self, 10).until(lambda driver: self.driver.find_element_by_id(login['登录id']))
    #         self.logger.info('已退出')





