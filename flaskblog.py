# Importing the Flask class and Setting Up the app variable as an instance of Flask class
from flask import Flask, render_template
app = Flask(__name__)

# Serving two routes by single function
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# Create another route for about
@app.route("/about")
def about():
    return render_template('about.html')

'''
To run the application set the env: 
    - $ENV:FLASK_APP="<python-file>"
    - $ENV:FLASK_DEBUG=1
    - Now run the command => "flask run"

You can also run the application without set the env:
    - By Providing below code.
    - Now Run the command => "python <python-file>"
'''

if __name__ == '__main__':
    app.run(debug=True)