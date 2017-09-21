from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1><a href="/f">F</a> <a href="/u">U</a> <a href="/n">N</a>!</h1>'

@app.route("/f")
def f_is_for():
    return "F is for friends who do stuff together."

@app.route("/u")
def u_is_for():
    return "u is for you and me!!!"

@app.route("/n")
def n_is_for():
    return "n is for anywhere and anytime at all down here in the deep blue sea"

if __name__ == "__main__":
    app.debug = True
    app.run()
