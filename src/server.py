# Import 3rd party modules
from flask import Flask, render_template

# Create app instance of Flask
app = Flask(__name__)

# Define functions mapped to each route
## Index/Home page
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def home():
    return render_template('home.html')

## About Me page
@app.route('/about')
def about():
	return render_template('about.html')

## Projects page
@app.route('/projects')
def projects():
	return render_template('inprogress.html')

## Work History page
@app.route('/WorkHistory')
def WorkHistory():
	return render_template('inprogress.html')

## Certifications page
@app.route('/Certifications')
def Certifications():
	return render_template('inprogress.html')

## University Transcripts page
@app.route('/UniversityTranscripts')
def UniversityTranscripts():
	return render_template('transcripts.html')

# Run App
if __name__ == "__main__":
    app.run(debug=True)
