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
    Energy_Tracker_PDF_URL = f"{S3_BASE_URL}/media/files/EIA Energy Tracker Report.pdf"
    CV_URL = f"{S3_BASE_URL}/media/files/Jose Amilcar Mata Calidonio - CV.pdf"
    resume_URL = f"{S3_BASE_URL}/media/files/Jose Amilcar Mata Calidonio - Full Stack Software Developer and CS Lecturer.pdf"
    PGS_Web_App_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/PGS+Web+App+DEMO.mp4"
    PGS_Hardware_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/PGS+Device+DEMO.mp4"
    PGS_Email_Alerts_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/PGS+Email+Alert+DEMO.mp4"
    Dish_Data_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/DishData DEMO.mp4"
    EIA_Energy_Tracker_DEMO_Video_URL = f"{S3_BASE_URL}/media/videos/EIA Energy Tracker DEMO.mp4"
    skills=[{"href": "https://www.python.org/", "filename": "Python-logo.png", "alt":"Python Logo", "label":"Python"},
            {"href": "https://flask.palletsprojects.com/en/stable/", "filename": "Flask_logo.png", "alt":"Flask Logo", "label":"Flask"},
            {"href": "https://sqlite.org/", "filename": "Sql_data_base_with_logo.png", "alt":"SQL Logo", "label":"SQL"},
            {"href": "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "filename": "JavaScript-logo.png", "alt": "JavaScript Logo", "label":"JavaScript"},
            {"href": "https://docs.aws.amazon.com/", "filename": "AWS logo.png", "alt":"AWS Logo", "label":"AWS App Deployment"},
            {"href": "https://docs.docker.com/", "filename": "docker logo.png", "alt":"Docker Logo", "label":"Docker"},
            {"href": "https://docs.github.com/en", "filename": "github.png", "alt":"GitHub Logo", "label":"GitHub"},
            {"href": "https://learn.microsoft.com/en-us/azure/azure-portal/", "filename": "azure_logo.png", "alt":"Azure Logo", "label":"Azure Console & Services"},
            {"href": "https://docs.azure.cn/en-us/azure-functions/functions-overview", "filename": "azure_functions.png", "alt":"Azure Functions Logo", "label":"Azure Functions"},
            {"href": "https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql", "filename": "Azure_sql_db_logo.png", "alt":"Azure SQL Database Logo", "label":"Azure SQL Server Database"},
            {"href": "https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops&toc=%2Fazure%2Fdevops%2Fget-started%2Ftoc.json", "filename": "devops_logo.png", "alt":"Azure DevOps Logo", "label":"Azure DevOps"},
            {"href": "https://learn.microsoft.com/en-us/power-bi/", "filename": "power_bi_logo.png", "alt":"Power BI Logo", "label":"Power BI"},
            {"href": "https://developer.mozilla.org/en-US/docs/Glossary/HTML5", "filename": "HTML5.png", "alt":"HTML5 Logo", "label":"HTML5"},
            {"href": "https://getbootstrap.com/", "filename": "Bootstrap logo.png", "alt":"Bootstrap Logo", "label":"Bootstrap"},
            {"href": "https://isocpp.org/std/the-standard", "filename": "C++Logo.png", "alt":"C++ Logo", "label":"C++"},
            {"href": "https://go.dev/doc/", "filename": "Go_Logo_Blue.png", "alt":"Golang Logo", "label":"Golang"},
            {"href": "https://aws.amazon.com/what-is/restful-api/", "filename": "rest_api_logo.png", "alt":"REST API Logo", "label":"REST API"},
            {"href": "https://nodejs.org/en", "filename": "Node.js-logo.png", "alt":"Node.js Logo", "label":"Node.js"},
            {"href": "https://expressjs.com/", "filename": "express-logo.png", "alt":"Express.js Logo", "label":"Express.js"},
            {"href": "https://postman.com/", "filename": "postman-logo.png", "alt":"Postman Logo", "label":"Postman"},
            ]

    return render_template("home.html",
                           Energy_Tracker_PDF_URL=Energy_Tracker_PDF_URL,
                           CV_URL = CV_URL,
                           resume_URL = resume_URL,
                           PGS_Web_App_DEMO_Video_URL=PGS_Web_App_DEMO_Video_URL,
                           PGS_Hardware_DEMO_Video_URL=PGS_Hardware_DEMO_Video_URL,
                           PGS_Email_Alerts_DEMO_Video_URL=PGS_Email_Alerts_DEMO_Video_URL, 
                           Dish_Data_DEMO_Video_URL = Dish_Data_DEMO_Video_URL,
                           EIA_Energy_Tracker_DEMO_Video_URL = EIA_Energy_Tracker_DEMO_Video_URL,
                           skills = skills)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)