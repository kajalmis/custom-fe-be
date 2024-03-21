from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/')
def index():
    return 'Backend: You are viewing the backend-Kajal.'

@app.route('/api/request', methods=['GET'])
def send_request():
    # You can add any necessary logic here
    return '200 OK you have successfully connected'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
