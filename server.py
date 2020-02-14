from flask import Flask, render_template, request, redirect, url_for
from flask import session
import data_manager


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def home():
    messages = data_manager.get_newest_messages()
    return render_template('home.html', messages=messages)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        input_username = request.form['username']
        input_password = request.form['password']
        if input_password == request.form['password_confirmation']:
            hashed_password = data_manager.hash_password(input_password)
            try:
                data_manager.add_user_into_db(input_username, hashed_password)
            except:
                message_failed = "Sorry, that username already exists."
                return render_template('register.html', message_failed=message_failed)
            return redirect(url_for('home'))
        else:
            message_password_confirmation_failed = "Password confirmation unsuccessful. Please try again."
            return render_template('register.html',
                                   message_password_confirmation_failed=message_password_confirmation_failed)
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        message_login_failed = "Username or password invalid."
        try:
            hashed_password = data_manager.get_password_by_username(request.form['username'])
            if data_manager.verify_password(request.form['password'], hashed_password):
                session['username'] = request.form['username']
                return redirect(url_for('home'))
        except:
            return render_template('login.html', message_login_failed=message_login_failed)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/post-message', methods=['POST'])
def post_message():
    user_id = data_manager.get_user_id_by_username(session['username'])
    message = request.form['message']
    data_manager.add_new_message(user_id, message)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
