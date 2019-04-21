import sys,os,logging
import Feng_Test_Case

print(sys.path[0])
print(sys.argv[0].split('Python_Unittest/')[1])
a=sys.argv[0]
print(os.getcwd())






def a():
    print(__name__)

a()
def b():
    print(sys._getframe().f_code.co_name)
b()


