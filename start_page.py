from flask import Flask, render_template, request

login_app = Flask(__name__)
dict_from_file = {}
with open('logins.txt') as logs:
    for line in logs:
        if ' ' in line:
            key, value = line.split(' ', 1)
            dict_from_file[key] = value


def check_username(usern, passw) -> 'bool':
    if usern not in dict_from_file.keys():
        return True
    else:
        return False

def check_password(usern, passw) -> 'bool':
    if dict_from_file[usern] == passw:
        return True
    else:
        return False


def add_username(usern, passw):
    with open('logins.txt', 'a') as txtfile:
        print(usern, passw, file=txtfile)
    dict_from_file[usern] = passw

@login_app.route('/')
def start_page() -> 'html':
    return render_template('home.html', the_title='Welcome to my simple login tester')

@login_app.route('/login')
def login_page() -> 'html':
    return render_template('login.html', the_title='Login')

@login_app.route('/create')
def create_page() -> 'html':
    return render_template('create.html', the_title='Create account')


@login_app.route('/status_create', methods=['POST'])
def status_create_page() -> 'html':
    usern = request.form['username']
    passw = request.form['password']
    if check_username(usern, passw):
        add_username(usern, passw)
        return render_template('status.html', username=usern, check=True, the_title='Success!')
    else:
        return render_template('status.html', username=usern, check=False, the_title='Failed')


@login_app.route('/status_login', methods=['POST'])
def status_login_page() -> 'html':
    usern = request.form['username']
    passw = request.form['password']
    if check_password(usern, passw):
        return render_template('status_login.html', username=usern, check=True, the_title='Success')
    else:
        return render_template('status_login.html', username=usern, check=False, the_title='Wrong password')


login_app.run(debug=True)
