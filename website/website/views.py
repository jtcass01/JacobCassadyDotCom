"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from website import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Me',
        year=datetime.now().year,
        message=''
    )

@app.route('/projects')
def projects():
    """Renders the projects page."""
    return render_template(
        'projects.html',
        title='Projects',
        year=datetime.now().year,
        message=''
    )

@app.route('/awards_and_certifications')
def awards_and_certifications():
    """Renders the awards page."""
    return render_template(
        'awards_and_certifications.html',
        title='Awards and Certifications',
        year=datetime.now().year,
        message=''
    )

@app.route('/transcripts')
def transcripts():
    """Renders the transcripts page."""
    return render_template(
        'transcripts.html',
        title='Transcripts',
        year=datetime.now().year,
        message=''
    )

@app.route('/work_history')
def work_history():
    """Renders the transcripts page."""
    return render_template(
        'work_history.html',
        title='Work History',
        year=datetime.now().year,
        message=''
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact Info',
        year=datetime.now().year,
        message=''
    )