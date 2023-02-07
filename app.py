from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, randint, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tastycakes'
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("madlib.html")

@app.route('/response')
def response():
    noun = request.args.get('noun')
    place = request.args.get('place')
    adj = request.args.get('adj')
    plural = request.args.get('plural')
    verb = request.args.get('verb')
    return render_template('response.html', place=place, noun=noun, adj=adj, verb=verb, plural=plural)