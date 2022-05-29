from flask import Flask, render_template, request

import AttendanceProject
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub", methods=['POST'])
def submit():
    if request.method == "POST":
        name = AttendanceProject.take_attendance()
    return render_template("sub.html", n=name)


if __name__ == "__main__":
    app.run(debug=True)