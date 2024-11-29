# video_extract
# keytonic
# 18 Aug 24
#
# will loop through the contents of the current directory
# any folder it finds it will enter, look for '.mp4's and move them
# out one folder to the working dir. so i can batch pull downloaded
# movies from folders to the root directory


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


import sys
import os
import os.path

working_dir = sys.path[0]   #C:\Users\keytonic\Documents\video_renamer
current_dir = ""            #C:\Users\keytonic\Documents\video_renamer\poop

def move_it(name):
    #if its not a folder, bail, should not have a period in the name
    #if(name.rfind('.') != -1):
    #    return
    if(os.path.isdir(name) == False):
        return
    
    #working dir plus folder name
    current_dir = "{}\\{}".format(working_dir,name)
    #print(current_dir)
    #print(working_dir)

    #getting contents of current dir
    list = os.listdir(name)

    #looping through contents
    for file in list:

        #movies only
        if(file.rfind('.mp4') == -1 and file.rfind('.mkv') == -1):
            continue

        #calc locations
        old_location = "{}\\{}".format(current_dir,file)
        new_location = "{}\\{}".format(working_dir,file)

        #lets go!
        print(bcolors.OKGREEN + "[Info]" + bcolors.ENDC + " Moving from {} to {}".format(old_location,new_location))
        os.rename(old_location,new_location)


#get the list of all files and directories in the current working directory
file_list = os.listdir()
#looping throught them all
for file in file_list:
    #ignore this script file name
    if(file != os.path.basename(__file__)):
        move_it(file)