from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/zubair")
def hello_zubair():
    return "<b><p>HELLO ZUBAIR JI!!!!!</p></b>"


if __name__ == "__main__":
    app.run()