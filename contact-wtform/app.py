from flask import Flask, render_template
from form import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
# Secret key is needed for the CSRF token.
app.secret_key = "Call me maybe"
# Initializes bootstrap flask.
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # Checks the WTForm for validators.
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
