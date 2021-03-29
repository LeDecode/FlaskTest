from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/eik_tu")
def eik_tu():
    return render_template("eik_tu.html")
@app.route("/template")
def template():
    return render_template("html_css.html")

@app.route("/<name>")
def not_existing(name):
    return render_template("do_not_exist.html", content=name)

@app.route("/admin")
def admin():
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)