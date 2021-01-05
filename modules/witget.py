import eel
import os

def start():
    eel.init("web")

    # Приём сообщения с сайта
    @eel.expose
    def call_in_js(msg):
        if msg == 'quit':
            os.system("TASKKILL /F /IM Chrome.exe")
            quit()
        elif msg.isdigit():
            msg = int(msg)*int(msg)

        call_in_python(msg)

    # Отправка сообщения на сайт
    def call_in_python(msg):
        eel.call_in_python(msg)

    eel.start("index.html", mode="chrome", size = (640, 400))