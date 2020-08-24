## adoption_site.py
from flask import Flask, render_template,session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey' #Secret key for the forms

class UpdateForm(FlaskForm):
    update = SubmitField('Update Data')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/covid_map')
def map():
    return render_template('folium_covid_map.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)

