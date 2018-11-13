from flask import Flask

from hello_world import hello

app = Flask(__name__)


@app.route("/")
def hello_endpoint():
    """Route all requests and handle it: Hello world"""
    return hello()


# start web application if run as hello world.py (not module)
if __name__ == '__main__':
    app.run()
