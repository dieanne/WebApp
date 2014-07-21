from flask import Flask

app = Flask(__name__)

wsgi_app = app


from routes import *

if __name__ == '__main__':
    import os, db

    host = os.environ.get('SERVER_HOST', 'localhost')
    try:
        port = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        port = 5555

    db.init()
    app.run(host, port)
