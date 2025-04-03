from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()

# notes
# Flask uses decorators (line 5)
# the "/" determines the home "folder"/page of the website
# returns the text of the function bellow
# run this either in the directory with "flask --app hello run" 
# or you need to set the ENV variables with '$Env:FLASK_APP="hello.py"' (to retrieve a ENV variable use $Env:FLASK_APP)
# and then run "flask run" and it will work

# lines 9 and 10 were added to be able to run this as a script with vsc without having to use the inline cmds

# extra note
# the <p> and </p> in line 7 are not required for text to be displayed
# since flask accepts html attributes in return you can use these to format the page
