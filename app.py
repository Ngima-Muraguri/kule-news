#virtual environment
from flask import flask

app = Flask(__name__)

#route function to render html template
@app.route('/')
def home():

    return render_template('home.html')
