# Hello! my name is.. Aplication

from crypt import methods
from markupsafe import Markup
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "mynameis2022"

# applications
@app.route("/")
def index():
    html_string = Markup("<h2>What's your name?</h2>")
    flash(html_string)
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():

    # collect data from FORM fields
    mynameis = str(request.form['hello_input'])
    mynameis = mynameis.upper()

    # set a condition.
    if mynameis == '':
        html_string = Markup("<h2 class='alertmessage'>Come On! What's your name?</h2>")

    else:

        html_string = Markup("<h2>Hello! my name is <span class='myname'>"+mynameis+"</span></h2>")
    flash(html_string)
    return render_template("index.html")

# end of application
