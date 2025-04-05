from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url)
    if response.status_code == 200:
        jsondata = json.loads(response.content)
        return render_template("index.html", data=jsondata)

@app.route("/post/<int:id>")
def post(id):
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url)
    if response.status_code == 200:
        jsondata = json.loads(response.content)
        for entry in jsondata:
            if id == entry['id']:
                post = entry
        return render_template("post.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

# notes
# render_template expects for the file to be in the "/templates" folder
# flask expects static files to be inside the "/static" folder