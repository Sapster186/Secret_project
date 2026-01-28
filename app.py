from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/question1")
def question1():
    return render_template("question1.html")

@app.route("/question2")
def question2():
    return render_template("question2.html")

@app.route("/question3")
def question3():
    return render_template("question3.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/secret-segue")
def secret_segue():
    return render_template("secret-segue.html")

if __name__ == "__main__":
    app.run(debug=True)


