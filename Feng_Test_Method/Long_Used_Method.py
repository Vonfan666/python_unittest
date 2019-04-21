#常用方法
import os,platform,re,sys,random
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def installUT(devices):
    # 每次都重新安装uiautomator2都两个应用
    try:
        os.popen("adb -s %s uninstall io.appium.uiautomator2.server.test" % devices)
        print(1)
        os.popen("adb -s %s uninstall io.appium.uiautomator2.server" % devices)
        print(2)
        os.popen("adb -s %s install %s" % (devices,os.path.dirname(os.path.dirname(__file__)))+"/Feng_Test_Conf/Feng_Test_Apk/appium-uiautomator2-server-v0.1.9.apk")
        print(3)
        os.popen("adb -s %s install %s" % (devices,os.path.dirname(os.path.dirname(__file__)))+"/Feng_Test_Conf/Feng_Test_Apk/appium-uiautomator2-server-debug-androidTest.apk")
        print(4)
    except:
        os.popen("adb -s %s install %s" % (devices,os.path.dirname(os.path.dirname(__file__)))+"/Feng_Test_Conf/Feng_Test_Apk/appium-uiautomator2-server-v0.1.9.apk")
        print(5)
        os.popen("adb -s %s install %s" % (devices,os.path.dirname(os.path.dirname(__file__)))+"/Feng_Test_Conf/Feng_Test_Apk/appium-uiautomator2-server-debug-androidTest.apk")
        print(6)



def kill_adb():
    '''验证端口5037是否被占用'''
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")

def appPath():
    '''获取apk所在路径'''
    apkPathCode=os.path.dirname(os.path.dirname(__file__))+'/Feng_Test_Conf/Feng_Test_Apk/'
    lists = os.listdir(apkPathCode) #查询该文件下的文文件名称
    apkPath = apkPathCode+lists[-1]
    return apkPath
def aPackage():
    '''获取包名'''
    path=os.path.dirname(os.path.dirname(__file__))+'/Feng_Test_Conf/Feng_Test_Apk/app2.3.4_beta20180525.apk'
    appPackage = re.findall('name=\'(.+?)\'', os.popen('aapt dump badging ' + path).readline())[0]
    return appPackage

def apActivity():
    '''获取获取appActivity'''
    path = os.path.dirname(os.path.dirname(__file__)) + '/Feng_Test_Conf/Feng_Test_Apk/app2.3.4_beta20180525.apk'
    appActivity=re.findall('launchable-activity: name=\'(.+?)\'',os.popen('aapt dump badging '+path+'| findstr "activity"').readline())[0]
    return appActivity

def GetMethodName():  #获取当前执行的函数名
    return sys._getframe().f_code.co_name



def randomTel(self):
    '''封装一个随机生成电话号码的方法,默认方法首位字母为1，其余十位随机'''
    i = 1
    listUsername = ['1']
    while i <= 10:
        Usernamecode = str(random.choice(range(10)))
        listUsername.append(Usernamecode)
        i += 1
    return ''.join(listUsername)


