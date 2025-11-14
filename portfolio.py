from flask import Flask, render_template, url_for
from dotenv import load_dotenv
import os

app = Flask(__name__)

#this key helps protect the Flask app by securing session data and preventing tampering or forgery of cookies and other sensitive information.
app.config["SECRET_KEY"]= os.getenv("SECRET_KEY")
S3_BASE_URL = os.getenv("S3_BASE_URL")

@app.route("/")
@app.route("/home")
def home_page():
    resume_URL = f"{S3_BASE_URL}/media/files/Jose+Amilcar+Mata+Calidonio+-+Software+Engineer.pdf"
    PGS_Web_App_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/PGS+Web+App+DEMO.mp4"
    PGS_Hardware_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/PGS+Device+DEMO.mp4"
    PGS_Email_Alerts_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/PGS+Email+Alert+DEMO.mp4"
    print(PGS_Web_App_DEMO_Video_URL)
    return render_template("home.html",
                           resume_URL = resume_URL,
                           PGS_Web_App_DEMO_Video_URL=PGS_Web_App_DEMO_Video_URL,
                           PGS_Hardware_DEMO_Video_URL=PGS_Hardware_DEMO_Video_URL,
                           PGS_Email_Alerts_DEMO_Video_URL=PGS_Email_Alerts_DEMO_Video_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)