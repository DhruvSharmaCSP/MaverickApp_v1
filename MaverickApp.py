from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def headers():
    headers = dict(request.headers)
    return headers, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
