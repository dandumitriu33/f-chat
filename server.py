from flask import Flask, render_template, request, redirect, url_for
import data_manager



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


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


if __name__ == "__main__":
    app.run(debug=True)
