from flask import Flask, render_template, request

login_app = Flask(__name__)

def check_username(usern, passw) -> 'bool':
    # will keep the logins as a dictionaries within a dictionary.
    # where the key in the first dictionary will be username and the value the actual username
    # and in the second dict keep the username as the key, and the password as the value
    # will need to edit this to check for that
    with open('logins.txt') as logs:
        if usern not in logs:
            add_username(usern, passw)
            return True
        else:
            return False

def add_username(usern, passw):
    with open('logins.txt', 'a') as txtfile:
        print({usern: passw}, file=txtfile)
        # TODO: will need to add it to the list of username.
        # lets see how it looks after I have added a few

@login_app.route('/')
def start_page() -> 'html':
    return render_template('home.html', the_title='Welcome to my simple login tester')

@login_app.route('/login')
def login_page() -> 'html':
    return render_template('login.html', the_title='Welcome!')

@login_app.route('/create')
def create_page() -> 'html':
    return render_template('create.html', the_title='Create account')

@login_app.route('/status', methods=['POST'])
def status_page() -> 'html':
    usern = request.form['username']
    passw = request.form['password']
    if check_username(usern, passw):
        return render_template('status.html', username=usern, check=True, the_title='Success')
    else:
        return render_template('status.html', username=usern, check=False, the_title='Failed')
        users = []
        # Will need to add the file to the users lists first.
        # Just going to see if I can get this to work
        # users.append({usern: passw})
        # with open('logins.txt', 'a') as file:
        #     print(str(users), file=file)
    # return render_template('login.html', the_title='Welcome!')



login_app.run(debug=True)
