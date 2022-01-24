from flask import Flask , send_file , render_template ,request
import smtplib

message = "Congrats"
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/subscribe",methods=["POST","GET"])
def subscribe():
    if request.method == "POST":
        email = request.form["Email"]
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("asdevelopers956@gmail.com","AronSerwin@123")
        server.sendmail("asdevelopers956@gmail.com",email,message)
    return render_template("subscribe.html")

@app.route("/download_file")
def download():
    p = "templates/Index.html"
    return send_file(p,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False)
