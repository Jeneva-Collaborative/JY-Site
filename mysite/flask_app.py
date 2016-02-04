
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def indexhtml():
    return '<link rel="icon" type="image/png" href="resources/favicon-16x16.png" sizes="16x16">Hello from Flask!'

@app.route('/resources/<path:path>')
def resources():
    return send_from_directory('resources', path)

# If I'm logged in as a developer (local username check), then behave differently.

import os

if os.getlogin() == 'jray':
    if __name__ == '__main__':
        app.run()
