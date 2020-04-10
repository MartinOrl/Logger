import os
import sys
import datetime
import time


def log(projectName, string, path="F:/PythonProjectLogs"):


    timestamp = datetime.datetime.now()
    timestamp = "\n"+timestamp.strftime("%Y-%m-%d %X")
    output = "{timestamp} : {text}".format(timestamp=timestamp, text=string)
    if path is log.__defaults__[0]:
        os.chdir(path)
    else:
        try:
            os.chdir(path)
        except Exception as e:
            os.chdir("F:/PythonProjectLogs")
    projectName = projectName + "_Log.log"
    file = open(projectName,"a")
    file.write(output)
    file.close()
    
def listLogs(projectName, path="F:/PythonProjectLogs"):
    os.chdir(path+"/"+projectName)
    print(os.listdir())

