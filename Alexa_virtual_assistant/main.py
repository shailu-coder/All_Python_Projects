from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import wikipedia
import wolframalpha
# from gtts import gTTS
# import pygame
import speech_recognition as sr #pip install SpeechRecognition
import sys
import os


# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

"""Please Watch my video to clear your all doubts - https://www.youtube.com/watch?v=XuApxUknTH4"""



app= QApplication(sys.argv)
win=QMainWindow()
win.setFixedSize(710,410)
win.setWindowTitle("My_Personal_Virtual_Assistant - @python_coderz_")

##############################################################################

def saysomething():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("You said: " + r.recognize_google(audio))
        myline.setText(r.recognize_google(audio))
        myacction()
    except:
        print("Google Speech Recognition Could not understand auido")

def myacction():
    print(myline.text())
    x=myline.text()
    if len(x)>=1:
        try:
            myappid= wolframalpha.Client('QHR7WJ-52AL3EQWU4')
            res=myappid.query(x)
            ans=next(res.results).text
            l1.setText("The Answer is: "+ ans)


            y=('The Answer is'+ ans)
            os.system('espeak "{}"'.format(y))

        ########################### your wish

            # mytext=str(ans)
            # z=str(mytext[:5]+".mp3")

            # output = gTTS(text=mytext, lang='en', slow=False)

            # output.save(z)
            # try:
            #     pygame.mixer.init()
            #     pygame.mixer.music.load(z)
            #     pygame.mixer.music.play()
                
            # except Exception as e:
            #     print(e)
        except:
            print(wikipedia.summary(x))
            l1.setText("The Answer is: "+ wikipedia.summary(x))

            y=('The Answer is'+ wikipedia.summary(x))
            os.system('espeak "{}"'.format(y))

            #######################################

            # mytext=str(wikipedia.summary(x))
            # z=str(mytext[:5]+".mp3")

            # output = gTTS(text=mytext, lang='en', slow=False)

            # output.save(z)
            # try:
            #     pygame.mixer.init()
            #     pygame.mixer.music.load(z)
            #     pygame.mixer.music.play()
                
            # except Exception as e:
            #     print(e)
    else:
        print("not working")

##############################################################################

myline=QtWidgets.QLineEdit(win)
myline.setPlaceholderText('Ask Me Anything...')
myline.returnPressed.connect(myacction)
myline.resize(600,25)
myline.move(30,20)

b1=QtWidgets.QPushButton(win)
b1.setText("Speak")
b1.clicked.connect(saysomething)
b1.setFixedSize(60,25)
b1.move(640,20)

l1=QtWidgets.QTextEdit(win)
l1.move(30,50)
l1.setFixedSize(600,300)

l2=QtWidgets.QLabel(win)
l2.setText("              Developed By: Shailendra Singh \n Follow Me On: www.facebook.com/shailendrakr007 \n Youtube: https://www.youtube.com/channel/UC_7NLLEcj-EJUAjBZdlmsfQ")
l2.move(320,335)
l2.resize(550,100)


os.system('espeak "Hi Guyz"')
win.show()
sys.exit(app.exec_())



