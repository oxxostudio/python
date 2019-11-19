from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    a = request.args
    return f'{a["aa"]},{a["bb"]}'


app.run(port=3000, debug=True)
