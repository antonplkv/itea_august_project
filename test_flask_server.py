from flask import Flask
app = Flask(__name__)


@app.route('/test')
def test():
    return 'Hello world'


app.route(host='0.0.0.0', port=80)