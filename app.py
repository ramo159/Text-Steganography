from flask import Flask, request, render_template
from sender import hideFunc
from receiver import revealFunc

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/hide", methods=["POST"])
def hide():
    formInfo = request.form
    result = hideFunc(formInfo["sec_msg"], formInfo["cvr_msg"])
    return render_template("homepage.html", result=result)


@app.route("/reveal", methods=["POST"])
def reveal():
    formInfo = request.form
    result_reveal = revealFunc(formInfo["steg_msg"])
    return render_template("homepage.html", result_reveal=result_reveal)


if __name__ == "__main__":
    app.run(debug=True)
