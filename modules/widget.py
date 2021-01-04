import eel

def start():
    eel.init("web")

    #Приём сообщения с сайта
    @eel.expose
    def call_in_js(msg):
        call_in_python(msg)

    #Отправка сообщения из пайтон в сайт
    def call_in_python(msg):
        eel.call_in_python(msg)

    eel.start("index.html", mode="chrome", size=(1300, 1000))