from flask import Flask, render_template
import embed

app = Flask(__name__)
post_id2=['10154226316550907%26id%3D33331950906', '992159644235360%26id%3185231581594841']

@app.route('/')
def home():
    return render_template('home.html', IDs= post_id2)
@app.route('/trends')
def trends():
    return render_template('trends.html')
@app.route('/about-us')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()


