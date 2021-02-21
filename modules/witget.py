import eel
import os

def start():
    eel.init("web")

    # Приём сообщения с сайта
    @eel.expose
    def call_in_js(msg_in):
        if msg_in == 'quit':
            os.system("TASKKILL /F /IM Chrome.exe")
            quit()
        elif msg_in.isdigit():
            msg_out = int(msg_in)*int(msg_in)
        elif msg_in == "calc":
            msg_out = "Запуск калькулятора"
            os.system('F:/SOFT/Office/Калькулятор.exe')
        elif msg_in == "paint":
            msg_out = "Запуск Paint"
            os.system('C:/Windows/system32/mspaint.exe')#pLan_openvpn.exe
        elif msg_in == "opera":
            msg_out = "Запуск Opera"
            os.system('C:/Users/Администратор/AppData/Local/Programs/Opera/launcher.exe')
        elif msg_in == "band":
            msg_out = "Запуск бандикана"
            os.system('D:/Games/Bandicam/bdcam.exe')
        elif msg_in == "dis":
            msg_out = "Запуск Discord"
            os.system('C:/Users/Администратор/AppData/Local/Discord/app-0.0.309/Discord.exe')
        elif msg_in == "dis":
            msg_out = "Запуск pLan_openvpn"
            os.system('C:/Users/Администратор/AppData/Local/Discord/app-0.0.309/pLan_openvpn.exe')

        else:
            msg_out = msg_in[::-1]
        call_in_python(msg_out)

    # Отправка сообщения на сайт
    def call_in_python(msg_out):
        eel.call_in_python(msg_out)

    eel.start("index.html", mode="chrome", size = (640, 400))