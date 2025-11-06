from flask import Flask, render_template, url_for
from dotenv import load_dotenv
import os

app = Flask(__name__)

#this key helps protect the Flask app by securing session data and preventing tampering or forgery of cookies and other sensitive information.
app.config["SECRET_KEY"]= os.getenv('SECRET_KEY') 

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)