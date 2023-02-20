from flask import Flask
import bot
import threading
import socket

if socket.gethostname() == "DESKTOP-S0FLL2V":
    bot.run()
else:
    app = Flask(__name__)


    @app.route('/')
    def index():
        return 'Hello from Flask!'


    def web_ping():
        print("starting the web")
        app.run(host='0.0.0.0', port=81)


    def bot_ping():
        print("starting the bot")
        bot.run()


    print("inicializing treads")
    t1 = threading.Thread(target=web_ping)
    t2 = threading.Thread(target=bot_ping)
    print("starting the threading procces")
    t2.start()
    print("thread 1 started succesfully")
    t1.start()
    print("thread 2 started succesfully")
