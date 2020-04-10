import os
import sys

#! <------------------------------------------------>
#*                  Logging script
#*
#*      Version: 1.0
#*     
#! <------------------------------------------------>

filepath = ""
sysargvs = sys.argv

def logFolderCreate(name="", filepath="F:/PythonProjectLogs"):
    if len(sysargvs) == 0:
        print("You forgot to pass required arguments!")
        print("If you need help, please enter [scriptname] --help ")
        sys.exit()

    if len(sysargvs) == 1:
        if name == "":
            print("Invalid name. Exiting program...")
            sys.exit()
        '''
        else:
            print("")
            #print("Creating Folder...")
            name = name+"Logs"
            print("Path set to basic.\nPath = F:/PythonProjectLogs")
            opt = str(input("Do you wish to change the path? [Y/N]: "))
            if opt.lower() == "y":
                filepath = str(input("Enter path: "))
        '''
    if len(sysargvs) == 2:
        if name == "":
            sys.exit()
        else:
            #print("Arguments accepted!")
            #print("Proceeding to creation...")
            name = name + "Logs"


    try:
        os.chdir(filepath)
    except Exception as e:
        print("Invalid Path!")
        print("Shutting down.")
        sys.exit()
    try:
        os.mkdir(name)
    except Exception as e:
        print("Folder Already Exists")
        prompt = str(input("Do you want to continue? [Y/N] : "))
        try:
            if prompt.lower() == "y":
                nameTemplate = name+"({index})"
                i = 1
                folders = os.listdir()
                while True:
                    name = nameTemplate.format(index=i)
                    if name in folders:
                        i = i+1
                        continue
                    else:
                        #print("Folder Name: {folder}".format(folder=name))
                        os.mkdir(name)
                        #print("Folder Created")
                        break
        except Exception as n:
            print(n)
    else:
        #print("Folder Name: {folder}".format(folder=name))
        #print("Folder Created")
        a = ""
    out = filepath+"/"+name
    return out
    
if len(sysargvs) == 3:
    name = sysargvs[1]
    filepath = sysargvs[2]
    logFolderCreate(name,filepath)

if len(sysargvs) == 2:
    name = sysargvs[1]
    logFolderCreate(name)
