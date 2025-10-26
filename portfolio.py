from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/portfolio_website")
def portfolio_website_page():
    return "<h1> Portfolio Website </h1>"


if __name__ == "__main__":
    app.run(debug=True)