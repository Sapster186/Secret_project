from flask import Flask, render_template, session, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Use environment variable for secret key (best practice)
app.secret_key = os.environ.get("SECRET_KEY", "fallback-secret")



@app.route("/")
def home():
    # reset score when starting fresh
    session["score"] = 0
    return render_template("main.html")

@app.route("/question1")
def question1():
    return render_template("question1.html", score=session.get("score", 0))

@app.route("/question2")
def question2():
    return render_template("question2.html", score=session.get("score", 0))

@app.route("/question3")
def question3():
    return render_template("question3.html", score=session.get("score", 0))

@app.route("/error")
def error():
    return render_template("error.html", score=session.get("score", 0))

@app.route("/secret")
def secret():
    return render_template("secret.html", score=session.get("score", 0))

@app.route("/secret-segue")
def secret_segue():
    return render_template("secret-segue.html", score=session.get("score", 0))

@app.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon.html')

# Hangman game page
@app.route('/hangman')
def hangman():
    return render_template('hangman.html')


@app.route("/connect4")
def connect4():
    return render_template("connect4.html")




# --- Answer routes for correct options ---

@app.route("/answer_quokka")
def answer_quokka():
    session["score"] = session.get("score", 0) + 1
    return redirect(url_for("question2"))

@app.route("/answer_cruella")
def answer_cruella():
    session["score"] = session.get("score", 0) + 1
    return redirect(url_for("question3"))

@app.route("/answer_byzantine")
def answer_byzantine():
    session["score"] = session.get("score", 0) + 1
    return redirect(url_for("secret_segue"))

@app.route("/reset")
def reset():
    session["score"] = 0
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)

