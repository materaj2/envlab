from flask import Flask, request, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import os

app = Flask(__name__)
Bootstrap(app)

app.secret_key = 'spg_P@ssw0rd'

# Load .env file
load_dotenv()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == os.getenv('USERNAME') and password == os.getenv('PASSWORD'):
            session['logged_in'] = True
            return redirect(url_for('panel'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/panel')
def panel():
    # Example of exposing environment variables - for educational purposes only
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('panel.html', username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
