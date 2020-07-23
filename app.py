## adoption_site.py
from flask import Flask, render_template, send_file

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey' #Secret key for the forms

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

@app.route('/hamza-musse-resume-engineering.pdf/')
def show_static_pdf():
    with open('/hamza-musse-resume-engineering.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='file.pdf')

if __name__ == '__main__':
    app.run(debug=True)
