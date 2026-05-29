import flask
import jsonfy
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
def home():
    return 'Hello World!'
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})
app.add_url_rule('/', 'home', home)