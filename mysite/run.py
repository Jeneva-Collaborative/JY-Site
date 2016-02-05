from app import app

import os

if os.getlogin() == 'jray':
    app.debug = True
    if __name__ == '__main__':
        app.run()

#app.run(host='0.0.0.0', port=8080, debug=True)

