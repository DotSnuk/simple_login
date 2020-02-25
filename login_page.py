from flask import Flask, render_template, request

login_app = Flask(__name__)

@login_app('/')
@login_app('/login')
def login_page() -> 'html':
    render_template('login.html', the_title='Welcome to my simple login tester')