import eel

def start():
    eel.init("web")
    eel.start("index.html", mode = "chrome")