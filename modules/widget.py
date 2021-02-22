import eel
import os

def start():
    eel.init("web")

    #Приём сообщения с сайта
    @eel.expose
    def call_in_js(msg_in):
        if msg_in == 'quit':
            os.system("TASKKILL /F /IM Chrome.exe")
            quit()
        elif msg_in == 'calk':
            msg_out = ""
            os.system("C:\Windows\System32\calc1.exe")
            os.system("TASKKILL /F /IM Chrome.exe")
        elif msg_in == 'CT':
            msg_out = ""
            os.system("D:\Documents\Programs\BATch\ClearTemp.bat")
            os.system("TASKKILL /F /IM Chrome.exe")
        elif msg_in == 'CL':
            msg_out = ""
            os.system("C:/Users/Nikita/Desktop/AutoClicker.exe")
            os.system("TASKKILL /F /IM Chrome.exe")
        elif msg_in == 'MCL':
            msg_out = ""
            os.system("D:\Documents\Programs\ProjectsFollowers\AuxProg\dist\AuxProg.exe")
            os.system("TASKKILL /F /IM Chrome.exe")
        elif msg_in == 'Ban':
            msg_out = ""
            os.system("C:/Users/Nikita/AppData/Local/Programs/Opera/launcher.exe")
            os.system("TASKKILL /F /IM Chrome.exe")
        call_in_python(msg_out)

    #Отправка сообщения из пайтон в сайт
    def call_in_python(msg_out):
        eel.call_in_python(msg_out)

    eel.start("index.html", mode="chrome", size=(750, 360))