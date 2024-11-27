from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello, DevOps!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
