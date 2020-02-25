from flask import Flask, render_template

login_app = Flask(__name__)

@login_app.route('/')
def start_page() -> 'html':
    return render_template('home.html', the_title='Welcome to my simple login tester')

@login_app.route('/login')
def login_page() -> 'html':
    return render_template('login.html', the_title='Welcome!')


login_app.run(debug=True)
