#hello world

from flask import Flask, redirect, url_for, request
from flask import render_template



apphello = Flask(__name__)

@apphello.route("/")
def hello_world():
    return "<h1>HELLO WORLD</h1>"

@apphello.route("/ayam/")
def helloalpro():
    return "<h2>ALPRO SO EASY</h2>"

@apphello.route("/home/")
def home ():
    return render_template("beranda.html")

@apphello.route("/more/")
def more ():
    return render_template("more.html")

@apphello.route("/resume/")
def resume ():
    return render_template("resume.html")

@apphello.route("/foods/")
def socials ():
    return render_template("foods.html")

@apphello.route("/films/")
def films ():
    return render_template("films.html")

@apphello.route("/convert2json")
def convert2json () :
    return render_template("convert2json.html")


@apphello.route("/fibonaci/")
def fibonaci ():
    return render_template("fibonaci.html")

@apphello.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@apphello.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__ == '__main__':
    apphello.run(debug=True)



