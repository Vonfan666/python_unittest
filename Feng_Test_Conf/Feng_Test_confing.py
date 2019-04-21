import os,re
# #pc电脑路径
# apkPath=r'D:\bao1\JiuMiaoDai-debug.apk'
# #直接获取设备名称
# deviceName=re.findall('(.+?)\t',os.popen('adb devices').readlines()[1])[0]
# #获取安卓版本号
# platformVersion=''.join(re.findall('(.+?)',os.popen('adb shell getprop ro.build.version.release').readlines()[0]))
# #获取安卓包名
# appPackage=re.findall('name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath).readline())[0]
# #获取appActivity
# appActivity=re.findall('launchable-activity: name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath+'|findstr "activity"').readline())[0]
global conFIng
conFIng = {}
conFIng['port']=4723
conFIng['bport']=4773
conFIng['seldnroidPort']=''
conFIng['chromedriverport']=4873
conFIng['platformName'] = 'Android'
conFIng['systemPort']=4823
# conFIng['platformVersion'] = platformVersion
# conFIng['deviceName'] = deviceName
# conFIng['appPackage'] = appPackage
# conFIng['appActivity']=appActivity
conFIng['noReset'] = True
conFIng['unicodeKeyboard'] = True
conFIng['resetKeyboard'] = True
conFIng['automationName']= 'Uiautomator2'
# conFIng['app'] = apkPath
conFIng['newCommandTimeout'] = '400'
conFIng['app']=os.path.dirname(os.path.dirname(__file__))+'/Feng_Test_Conf/Feng_Test_Apk/app2.3.4_beta20180525.apk'
