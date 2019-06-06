import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    backend_url = "http://backend:5000/" # due to internal DNS, we can
                                         # conveniently access the
                                         # backend via its name
     
    r = requests.get(backend_url)
    return "Message from backend: " + r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0') # flask by default only binds on localhost,
                            # need to bind on remote interface, too to be
                            # able to expose it from within Docker
