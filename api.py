import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello Mark</h1>'

app.run( host = "0.0.0.0", port = 1234)
