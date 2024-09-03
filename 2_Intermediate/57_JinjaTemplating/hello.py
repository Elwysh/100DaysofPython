from flask import Flask, render_template
import random
import datetime
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    ranint = random.randint(1,100)
    currentyear = datetime.date.today().strftime("%Y")
    return render_template("index.html", rnum=ranint, year=currentyear)

@app.route("/guess/<name>")
def guess(name):
    url = f"https://api.genderize.io?name={name}"
    url2 = f"https://api.agify.io?name={name}"
    response = requests.get(url)
    response2 = requests.get(url2)
    currentyear = datetime.date.today().strftime("%Y")
    if response.status_code == 200 and response2.status_code == 200:
        jsondata = json.loads(response.content)
        jsondata2 = json.loads(response2.content)
        return render_template("guess.html", name=name, gender=jsondata["gender"], age=jsondata2["age"], year=currentyear)
    else:
        return "No response from related API."

@app.route("/blog")
def blog(num):
    return f"Variable passed through is {num}"

if __name__ == "__main__":
    app.run(debug=True)

# notes
# shows passing variables into the template
