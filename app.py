import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()
sql = "create table tb_gdp (country varchar(128), year integer, gdp real);"
cursor.execute(sql)
conn.commit()

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)
