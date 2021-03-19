from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
app = Flask(__name__)

app.secret_key = "abcdefghijk"


@app.route("/")
def index():
    state = session.get("account")
    # print(user)
    if state != None:
        return redirect("/member")
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        session["account"] = account
        # session.get('account')
        session.permanent = True
        return redirect("/member")
    else:
        return redirect("/error")


@app.route("/member")
def member():
    # session["user"] = "loginSuccess"
    # session.permanent = True
    state = session.get("account")
    if state == None:
        return redirect("/")
        # return redirect("/member")
        # if state == "loginSuccess":
    return render_template("member.html")
    # else:


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/signout")
def signout():
    session.clear()
    # session.pop('account')
    # session["username"] = None
    return redirect("/")


app.run(port="3000")
