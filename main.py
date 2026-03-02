from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def get_contact_form():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def get_login():


if __name__ == "__main__":
    app.run(debug=True)
