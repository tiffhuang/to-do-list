from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # TODO
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()