from flask import Flask
import challenge

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!" \
        "<p> Summer is hot paragraph</p>" \
        "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWJ3b28zNXh4cnVhcHU1aGNqazZuZTlrYmhxZGVwenM3NnhkcWJkNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LNisSS34qHwcg/giphy.gif'>" \
        '<div class="tenor-gif-embed" data-postid="18168507837226940661" data-share-method="host" data-aspect-ratio="1.76596" data-width="100%"><a href="https://tenor.com/view/ayaya-gif-18168507837226940661">Ayaya GIF</a>from <a href="https://tenor.com/search/ayaya-gifs">Ayaya GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>'

@app.route("/bye")
@challenge.make_bold
def bye():
    return "<u><em>Bye, World!</em></u>"

@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hello there {name}!</p>"

@app.route("/greetlong/<path:name>")
def greetlong(name):
    return f"<p>Hello there {name}!</p>"

@app.route("/greetage/<name>/<int:number>")
def greetage(name, number):
    return f"<p>Hello there {name}, your age is {number}!</p>"

if __name__ == "__main__":
    app.run(debug=True)


# notes
# showcase of how to create "subfolders" for the website
# greet function shows how to create a variable in the link and then use it in text (syntax in link required "<VarName>")

# the greetlong function shows how to use the full path of the link but use it as a variable including the "/" 
# so the name would include the text before and after / inlcluding the /

# greetage function shows the int variable in text

# careful with the gifs, some websites may be blocking unless you got the link to the actual gif only
# embed example below

# for debugger add the optional param in line 18 "debug=True" to enable debug mode on the website
# careful with this as it allows to run code but requires a pin from the cmd given when the app starts
# debug mode also allows to reload the app automatically when you save the file to reflect the changes immediatelly 