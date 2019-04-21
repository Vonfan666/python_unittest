__author__='fengfan'
import logging,time,os
import logging.config
import logging.handlers

def Log():
    logging.config.fileConfig(os.path.dirname(os.path.dirname(__file__)) + '/Feng_Test_Conf/confing.conf')  # 该路径是调用env下面的mylog日志配置文件
    logger = logging.getLogger(__name__)
    curTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    logFile = os.path.dirname(os.path.dirname(__file__)) + r'/Feng_Test_Log/Driver_Log/' + curTime + '.log'

    fmt = '[%(asctime)s](%(levelname)s)%(name)s : %(message)s\n'
    formartter = logging.Formatter(fmt)

    # handler = logging.handlers.RotatingFileHandler(logFile, maxBytes=4096000000, backupCount=9)
    # handler.setFormatter(formartter) #本地文件
    # logger.setLevel(logging.INFO) #本地文件
    # logger.addHandler(handler)  #本地文件

    consoleLog = logging.StreamHandler()  # 控制台
    consoleLog.setFormatter(formartter)  # 控制台
    consoleLog.setLevel(logging.INFO)  # 控制台
    logger.addHandler(consoleLog)  # 控制台
# logger.removeHandler(formartter)#控制台重复去掉一
if  __name__ == '__main__':
    Log()