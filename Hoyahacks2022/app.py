from distutils.log import debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("iss.py")

@app.route("/result")
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("iss.py")


if __name__ == '__main__':
    app.run(debug = True, port=5001)