import eel

def start():
    eel.init("web")

    #Приём сообщения с сайта
    @eel.expose
    def call_in_js(msg):
        print(msg)

    eel.start("index.html", mode="chrome", size=(800, 533))