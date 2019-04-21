#文件读取方法
import os
import pymysql,xlrd,wlrd
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from Feng_Test_Method.Start_App_Method import start_App



class ReadFile(object):
    def __init__(self,driver):
        self.driver=driver
        self.logger=start_App.PrintLog()

    def scrollAction(self, id, n, m):  # n滑动次数，m是控件高度内，存在的多少个数字间隔
        a = self.driver.find_element_by_id(id)
        actionPosition = a.location  # 控件初始坐标坐标，得到dict{x:宽，y：高}
        actionSize = a.size  # 获取控件的宽度和高度，得到dict{height:高度，width：宽度}，这个是控件的
        px = self.driver.get_window_size()['width']  # 获取屏幕宽度
        py = self.driver.get_window_size()['height']  # 获取屏幕高度
        start1 = actionPosition['x'] / px  # 定位控件相对x坐标
        start2 = actionPosition['y'] / py  # 定位控件相对y坐标
        jj = actionSize['height'] // m / py  # 获取每次滑动的间隔相对坐标
        for i in range(n):
            action = TouchAction(self.driver)
            action.press(x=start1, y=start2).wait(ms=1000).move_to(x=start1, y=(start2 - jj)).release()
            action.perform()

    def duQu_Excel(self, Sheet, a, b):
        '''读取excel文件'''
        exlce_Name = xlrd.open_workbook(
            r'C:\Users\Administrator\Desktop\python01\fengfan_unittest\feng_exlce_case\denglu_excel.xls')  # 打开excel文件格式为xlsx有的是xls
        table = exlce_Name.sheet_by_name(Sheet)
        cell_a1 = table.cell(a, b).value  # a代表行——从零开始   b代表列 从零开始
        self.logger.info(u'>>>获取excel表格内容：{}'.format(cell_a1))
        return cell_a1

    '''复制表格写入excel'''
    @staticmethod
    def xieRu_Excel(self, a, b, sheet_name, value, filePath):  # excel 写入
        excel_Name = xlrd.open_workbook(r'C:\Users\Administrator/Desktop/excel_case/denglu_excel.xls',
                                        formatting_info=True)  # 打开excel表格
        table = excel_Name.sheet_by_name(sheet_name)  # 选择sheet页
        exlce_NameCode = copy(excel_Name)  # 复制一个excel
        tableCode = exlce_NameCode.get_sheet(
            0)  # 找到复制后的 sheet页 ——备注：excel_Name.sheet_by_name无法write！get——sheet可以write
        tableCode.write(a, b, value)  # 写入
        exlce_NameCode.save(filePath)  # 保存新的excel

    @staticmethod
    def selectSQL(sql):
        db = pymysql.connect(host="192.168.12.17", port=3116, user="mysql_yzbtest", password="jH7E6Y2zb3WX",
                             db="yzb_app", charset='utf8')
        cursor = db.cursor()
        # cursor.execute("select *  from  yzb_user WHERE NAME like '%s'"%('冯%'))
        cursor.execute(sql)  # 执行sql语句,并返回一个
        return cursor.fetchall()  # 取出的所有的值

    '''封装一个传入服务器地址host，port端口号,db第几个表,redisPassword密码'''
    @staticmethod
    def redisCode(host, port, db, redisPassword, Usernamecode):
        pool = redis.ConnectionPool(host=host, port=port, db=db, password=redisPassword)
        r = redis.StrictRedis(connection_pool=pool)
        a = Usernamecode
        b = 'register_user_code_'
        return r.get(b + a).decode('utf-8')

    @staticmethod
    def smtp_mail(choocemail, sendmail, receivemail):  # choocemail选择163还是qq,sendmail发件人，receivemail收件人
        path = "C:\\Users\\Administrator\\Desktop\python01\\fengfan_unittest\\feng_test_result\\"
        lists = os.listdir(path)
        filepath = path + lists[-1]
        with open(filepath, "rb") as fp:
            mail_body = fp.read()
        if choocemail == '163':  # 选择是163之后，所有的参数都是163的
            smtpserver = "smtp.163.com"  # 163邮箱服务器地址
            port = 0  # 端口号163邮箱为0，腾讯邮箱为 465 或者587
            mailtext = "您好:</br><p>　　　　请下载附件之后，由谷歌打开查看测试报告详情！</p>"  # 邮件内容
            mailCode = MIMEMultipart()
            # 使用MUMEText构造文本邮件字典
            mailCode['from'] = sendmail  # 添加发件人键值对
            mailCode['to'] = receivemail  # 添加收件人键值对
            mailCode['subject'] = '冯凡—自动化测试报告'  # 添加文本主题键值对

            body = MIMEText(mailtext, "html", "utf-8")
            mailCode.attach(body)
            # 添加附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="test_report.html"'
            mailCode.attach(att)

            smtp = smtplib.SMTP()  # 使用该方法发送邮件
            smtp.connect(smtpserver)  # 链接服务器
            smtp.login(sendmail, 'ff123456789')  # 登录
            smtp.sendmail(sendmail, receivemail, mailCode.as_string())  # 发送
            smtp.quit()  # 关闭
        if choocemail == 'qq':
            smtpserver = "smtp.qq.com"  # qq邮箱服务器地址
            port = 465
            mailtext = "您好:</br><p>　　　　请下载附件之后，由谷歌打开查看测试报告详情！</p>"  # 邮件内容
            mailCode = MIMEMultipart()

            mailCode['from'] = sendmail
            mailCode['to'] = receivemail
            mailCode['subject'] = '冯凡—自动化测试报告'

            text = MIMEText(mailtext, 'html', 'utf-8')  # 构造邮件
            mailCode.attach(text)

            # 添加附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename="test_report.html"'
            mailCode.attach(att)

        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sendmail, "fhezvfffbbvvbfgb")  # 登录
        smtp.sendmail(sendmail, receivemail, mailCode.as_string())  # 发送
        smtp.quit()  # 关闭



    def ReadFileClass():  #读取TestCase所有的test用例
        listClass=[]
        pathCode = os.path.dirname(os.path.dirname(__file__)) + '\\Feng_Test_Case'
        TestFile = os.listdir(pathCode)
        TestFile.pop()
        for file in TestFile:
            fileName = pathCode + '\\' + file

            f = open(fileName, 'r')
            a = f.readlines()
            b = ''.join(a)
            TestFileName = re.findall("class (.+?)\(", b)[0]
            listClass.append(TestFileName)
            f.close()
        return listClass




