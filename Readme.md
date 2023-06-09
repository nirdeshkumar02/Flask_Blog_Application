# A Blog Website project to learn Backend Development with Python-Flask.

## Directory Structure:

- static: This directory contains the css files.
- templates: This directory has the html files helps to render ui.

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

## Features
- We can pass dynamic title to page from routers. (Individual Router with Individual Title)