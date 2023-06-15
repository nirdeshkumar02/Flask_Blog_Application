# A Blog Website project to learn Backend Development with Python-Flask.

## Directory Structure:

- Flask_Blog/flaskblog
    - static: This directory contains the css files.
    - templates: This directory has the html files helps to render ui.
    - instance: This directory contains the sql based file to store data.
    - init.py: Init file is used for initialization the Flask app and SQL DB.
    - forms.py: Forms file have the class to register and login the user with validation.
    - models.py: Models file contains the structure of user and post.
    - routes.py: All the routes related to application is defined here.

- Flask_Blog/run.py - The main file which run the application.
## To Run the Application:

There are two ways to run the application:
1. By Setting Environments Variables:
```
- $ENV:FLASK_APP="flaskblog.py"
- $ENV:FLASK_DEBUG=1
- Now run the command => "flask run"
```

2. By Calling Main function:
```
- Call the main class to name.
    if __name__ == '__main__':
        app.run(debug=True)
    
- Now Run the application => python flaskblog.py
```

3. Import SQL Instance to Local project using Python Shell
```
- Open terminal in the project directory
- Run `python` in the terminal
- Run the below command:
    >>> from flaskblog import app, db
    >>> app.app_context().push()
    >>> db.create_all()

## Features
- We can pass dynamic title to page from routers. (Individual Router with Individual Title).
- We use flask-wtf package to use form generation and its validation.