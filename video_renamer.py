# video_renamer
# keytonic
# 18 Aug 24
#
# attempts to itterate current directory and renames all videos correctly
# from:
# Ant-Man.And.The.Wasp.Quantumania.2023.720p.BluRay.x264.AAC-[YTS.MX].mp4
# The.Iron.Claw.2023.720p.BluRay.x264.AAC-[YTS.MX].mp4
# to:
# Ant-Man And The Wasp Quantumania (2023).mp4
# Iron Claw, The (2023).mp4
# 
# Will also take one file name via command line
# eg: python video_renamer.py Ant-Man.And.The.Wasp.Quantumania.2023.720p.BluRay.x264.AAC-[YTS.MX].mp4

import sys
import os
#import webbrowser
import requests

from imdb import Cinemagoer

ia = Cinemagoer()



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

    

def get_poster(name,year):

    filename = "{} ({}).{}".format(name,year,'jpg')

    try:
        movies = ia.search_movie("{} {}".format(name,year))
        movie = ia.get_movie(movies[0].movieID)
        img_data = ""
        
        if(movie.has_key('cover url') == True and movie['cover url'] != ""):
            img_data = requests.get(movie['cover url']).content

        if(img_data != ""):
            with open(filename, 'wb') as handler:
                handler.write(img_data)
                print(bcolors.OKGREEN + "[Info]" + bcolors.ENDC + " Creating '" + bcolors.OKCYAN + filename + bcolors.ENDC + "'")
        else:
            print(bcolors.FAIL + "[Fail]" + bcolors.ENDC + " could not save: '" + filename + "'")
    except:
        print(bcolors.FAIL + "[Fail]" + bcolors.ENDC + " could not save: '" + filename + "'")

    #input("Press Enter to continue...")

def rename(name):

    #looking at extention first because if it aint a movie 
    #then there aint no point in doing anything else
    ext = (name[name.rfind('.') + 1:]).strip()

    if(ext != "mp4" and ext != "mkv"):
        #return quietly if its a script or folder
        #if(ext != "py" and name.rfind('.') != -1):
        if(os.path.isdir(name) == False and ext != "py"):
            #return loudly if it is a file with a no shit wrong extention
            print(bcolors.FAIL + "[Fail]" + bcolors.ENDC + " extention: '{}' name: '{}'".format(ext,name))
        return
    
    

    #searching for year, looking for first occurance of year_prefix 
    #hoping year is something like 20xx or 19xx what ever year_prefix is set to
    year_prefix = "20"
    year = (name[name.find(year_prefix):name.find(year_prefix) + 4]).strip()

    if((year.isnumeric() == False) or (year == "")):

        year_prefix = "19"
        year = (name[name.find(year_prefix):name.find(year_prefix) + 4]).strip()

        if((year.isnumeric() == False) or (year == "")):
            print(bcolors.FAIL + "[Fail]" + bcolors.ENDC + " year: '{}' name: '{}'".format(year,name))
            #sys.exit()
            return

    #getting the title, doing alot of .srip'n just making sure theres no spaces
    #also checking for 'the' in the title. if its in the begining the rename accordingly
    title = (name[0:name.find(year_prefix)].replace('.', ' ')).strip()

    #removing '(' and ')' incase this file has been processed previously
    title = title.replace('(', '').strip()
    title = title.replace(')', '').strip()

    #need to fix this... triggers on 'they' etc
    if((title.find("The ") != -1) and (title.find("The ") == 0)):
        title = "{}, The".format(title[4:])

    #putting it all together
    new_name = "{} ({}).{}".format(title,year,ext)

    #let's go!
    print(bcolors.OKGREEN + "[Info]" + bcolors.ENDC + " Renaming '" + bcolors.OKCYAN + new_name + bcolors.ENDC + "'")
    os.rename(name,new_name)
    get_poster(title,year)


#if filename given on commandline then go with it
if(len(sys.argv) > 1):
    rename(sys.argv[1])
#otherwise loop through files in directory and process them
else:
    #get the list of all files and directories in the current working directory
    file_list = os.listdir()
    #looping throught them all
    for file in file_list:
        #ignore this script file name
        if(file != os.path.basename(__file__)):
            rename(file)