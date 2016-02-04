# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def indexhtml():
    return """
<html>
    <head>
        <link rel="icon" type="image/png" href="static/img/favicon-16x16.png" sizes="16x16">
    </head>
    <body>
        Hello from Flask!
    </body>
</html>
""" #EndDoc

@app.route('/resources/<path:path>')
def resources():
    return send_from_directory('resources', path)

# If I'm logged in as a developer (local username check), then behave differently.

import os

if os.getlogin() == 'jray':
    app.debug = True
    if __name__ == '__main__':
        app.run()
