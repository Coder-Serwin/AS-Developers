from flask import Flask , send_file , render_template ,request

app = Flask(__name__)
p = ""
Gamename = ""

@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/games/<GameName>")
def Game(GameName):
    global Gamename
    Gamename = GameName
    check_path(Gamename)
    return render_template("Game.html",game_name=GameName)

def check_path(Gamename):
    global p
    if Gamename.startswith("Catch"):
        p = "templates/Game.html"
    elif Gamename == "":
        p = "main.py"
    else:
        p = ".env"


@app.route("/download_file")
def download_file():
    return render_template("download.html")


@app.route("/download")
def download():
    return send_file(p,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
