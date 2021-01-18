from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'key'

toolbar = DebugToolbarExtension(app)

# Store answers in this list (ex ['Yes', 'No', 'Less than $10,000', 'Yes'])
responses = []


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/questions/0')
def question():
    return render_template("questions.html")