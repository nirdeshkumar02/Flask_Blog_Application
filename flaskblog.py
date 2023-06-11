# Importing the Flask class and Setting Up the app variable as an instance of Flask class
from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)

# Setting Secret Configuration for external attacks.
app.config['SECRET_KEY'] = "3d6e044ffd997a7be3e38d017453be94"

posts = [
    {
        'author': 'Nirdesh Kumar',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Sarvesh Kumar',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 21, 2023'
    }
]

# Serving two routes by single function
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title="Home Page")


@app.route("/about")
def about():
    return render_template('about.html', title="About Page")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Registration Page", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login Page", form=form)


if __name__ == '__main__':
    app.run(debug=True)