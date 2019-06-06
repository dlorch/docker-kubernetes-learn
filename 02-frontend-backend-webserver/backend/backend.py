from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from backend"

if __name__ == '__main__':
    app.run(host='0.0.0.0') # flask by default only binds on localhost,
                            # need to bind on remote interface, too to be
                            # able to expose it from within Docker
