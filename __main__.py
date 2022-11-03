import eel
import beliapp

eel.init("web")

@eel.expose
def submit(config):
    beliapp.scrape(username=config["username"])


eel.start('index.html', size=(275, 275))
