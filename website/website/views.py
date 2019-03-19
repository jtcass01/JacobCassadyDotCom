"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import render_template, send_file
from website import app
from website.google_analytics import track_event

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    track_event(
		category='home',
		action='home page visit')
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    track_event(
		category='about',
		action='about page visit')
    return render_template(
        'about.html',
        title='About Me',
        year=datetime.now().year,
        message=''
    )

@app.route('/projects')
def projects():
    """Renders the projects page."""
    track_event(
		category='projects',
		action='projects page visit')
    return render_template(
        'projects.html',
        title='Projects',
        year=datetime.now().year,
        message=''
    )

@app.route('/simon')
def simon():
    """Renders the simon project page."""
    track_event(
		category='projects',
		action='simon page visit')
    return render_template(
        'simon.html',
        title='Sign Interfaced Machine Operating Network (SIMON)',
        year=datetime.now().year,
        message=''
    )

@app.route('/vds')
def vds():
    """Renders the simon project page."""
    track_event(
		category='projects',
		action='vds page visit')
    return render_template(
        'vds.html',
        title='Variable Drag System (VDS)',
        year=datetime.now().year,
        message=''
    )

@app.route('/rc8_api')
def rc8_api():
    """Renders the simon project page."""
    track_event(
		category='projects',
		action='rc8_api page visit')
    return render_template(
        'rc8_api.html',
        title='Denso RC8 Python API',
        year=datetime.now().year,
        message=''
    )

@app.route('/awards_and_certifications')
def awards_and_certifications():
    """Renders the awards page."""
    track_event(
		category='awards_and_certifications',
		action='awards_and_certifications page visit')
    return render_template(
        'awards_and_certifications.html',
        title='Awards and Certifications',
        year=datetime.now().year,
        message=''
    )

@app.route('/transcripts')
def transcripts():
    """Renders the transcripts page."""
    track_event(
		category='transcripts',
		action='transcripts page visit')
    return render_template(
        'transcripts.html',
        title='University Transcripts',
        year=datetime.now().year,
        message=''
    )

@app.route('/work_history')
def work_history():
    """Renders the transcripts page."""
    track_event(
		category='work_history',
		action='work_history page visit')
    return render_template(
        'work_history.html',
        title='Work History',
        year=datetime.now().year,
        message=''
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    track_event(
		category='contact',
		action='contact page visit')
    return render_template(
        'contact.html',
        title='Contact Info',
        year=datetime.now().year,
        message=''
    )

@app.route('/robots.txt')
def robot():
    """Renders the dean certificate for fall 2013."""
    track_event(
		category='robot',
		action='robot stopped by')
    return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'robots.txt')


''' Dean's List Certificate Routes '''
@app.route('/dean_cert_fall_2013')
def dean_cert_fall_2013():
    """Renders the dean certificate for fall 2013."""
    track_event(
		category='contact',
		action='contact page visit')
    return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'transcripts' + os.path.sep + '2013' + os.path.sep + 'dean_cert_fall_2013.pdf')

@app.route('/dean_cert_spring_2014')
def dean_cert_spring_2014():
    """Renders the dean certificate for spring 2014."""   
    track_event(
		category='contact',
		action='contact page visit')
    return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'transcripts' + os.path.sep + '2014' + os.path.sep + 'dean_cert_spring_2014.pdf')

@app.route('/dean_cert_fall_2015')
def dean_cert_fall_2015():
	"""Renders the dean certificate for fall 2015."""
	track_event(
		category='contact',
		action='contact page visit')
	return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'transcripts' + os.path.sep + '2015' + os.path.sep + 'dean_cert_fall_2015.pdf')

@app.route('/dean_cert_fall_2016')
def dean_cert_fall_2016():
	"""Renders the dean certificate for fall 2016."""
	track_event(
		category='contact',
		action='contact page visit')
	return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'transcripts' + os.path.sep + '2016' + os.path.sep + 'dean_cert_fall_2016.pdf')

@app.route('/dean_cert_spring_2018')
def dean_cert_spring_2018():
	"""Renders the dean certificate for spring 2018."""
	track_event(
		category='contact',
		action='contact page visit')
	return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'transcripts' + os.path.sep + '2018' + os.path.sep + 'dean_cert_spring_2018.pdf')

@app.route('/dean_cert_fall_2018')
def dean_cert_fall_2018():
	"""Renders the dean certificate for fall 2018."""
	track_event(
		category='contact',
		action='contact page visit')
	return send_file(os.getcwd() + os.path.sep + 'website' + os.path.sep + 'static' + os.path.sep + 'transcripts' + os.path.sep + '2018' + os.path.sep + 'dean_cert_fall_2018.pdf')
