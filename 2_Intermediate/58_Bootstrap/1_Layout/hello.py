from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# notes
# render_template expects for the file to be in the "/templates" folder
# flask expects static files to be inside the "/static" folder