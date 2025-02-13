import os
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response(
        {
            'response': 'Hello, World!',
            'status': 200
        }
    )
    return response

@app.route('/repeat', methods=['GET']) # 2) Route W/ Get Parameter

def repeat():
    input = request.args.get('input')
    return {
            "body": input,
            "status": 200
    } 

@app.route('/health') # 3) Expose on Endpoints
@app.route('/healthcheck') # 3) Expose on Endpoints
def health(): 
    response = make_response(
        {
        "body": "OK",
        "status": 200
        }
    )
    return response

@app.route('/hang') 
def hang():
    while True:
        pass 

if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)
    
    port = os.getenv('PORT')
    app.run(host='0.0.0.0', debug=True, port=port, threaded = False)
