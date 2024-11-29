# video_organize
# keytonic
# 18 Aug 24
#
# a simple script that loops through all the movies in a folder 
# and organizes them into folders named A through Z based on the title, 
# folder named # for non alphabetic first character


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

def move_it(name):

    #skip over python scripts
    if (name.find(".py") != -1) :
        return

    #movies only
    if(name.rfind('.mp4') == -1 and name.rfind('.mkv') == -1):
        return

    #get first character, # is its not in alphabet
    first_char = name[:1].upper()
    first_char = first_char if first_char.isalpha() else "#"

    #calc paths
    src_location = os.path.abspath(name)
    new_location = "Z:\\Movies\\" + first_char + "\\" + name

    try:
        os.rename(src_location,new_location)
        print(bcolors.OKGREEN + "[Info]" + bcolors.ENDC + " Moving: '" + src_location + "' to '" + new_location + "'")
    except:
        print(bcolors.FAIL + "[Fail]" + bcolors.ENDC + " Moving: '" + src_location + "' to '" + new_location + "'")

#get the list of all files and directories in the current working directory
file_list = os.listdir()
#looping throught them all
for file in file_list:
    #ignore this script file name
    if(file != os.path.basename(__file__) and os.path.isdir(file) == False):
        move_it(file)