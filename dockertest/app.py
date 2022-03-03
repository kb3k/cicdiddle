from flask import Flask


# welcome to the fourth line


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>oh hi </h1>'


if __name__ == "__main__":
    app.run(ssl_context="adhoc", host="0.0.0.0", port=5000)
