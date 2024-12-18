from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def headers():
    headers = dict(request.headers)
    # Build a simple HTML page to display headers
    html = "<html><body><h1>HTTP Headers</h1><table border='1'>"
    html += "<tr><th>Header</th><th>Value</th></tr>"

    for key, value in headers.items():
        html += f"<tr><td>{key}</td><td>{value}</td></tr>"

    html += "</table></body></html>"
    return html, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
