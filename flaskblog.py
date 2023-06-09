# Importing the Flask class and Setting Up the app variable as an instance of Flask class
from flask import Flask, render_template
app = Flask(__name__)

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
    # Inside the layout; As page change then default title will be override using this.
    return render_template('home.html', posts=posts, title="Home Page")

# Create another route for about
@app.route("/about")
def about():
    # Inside the layout; As page change then default title will be override using this.
    return render_template('about.html', title="About Page")

if __name__ == '__main__':
    app.run(debug=True)