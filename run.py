import os
from flask import Flask
from config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def hello():
    return "Hello from configured app!"


if __name__ == "__main__":
    debug_mode = app.config["DEBUG"]
    port = app.config["PORT"]
    app.run(debug=debug_mode, port=port)
