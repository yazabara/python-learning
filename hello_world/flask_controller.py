from flask import Flask

import hello_world

app = Flask(__name__)

__version__ = '0.0.1'


@app.route("/")
def hello_endpoint():
    """Route all GET root "/" requests and handle it: Hello world"""
    return hello_world.hello()


@app.route("/version")
def hello_version_endpoint():
    """Route all GET "/version"  requests and handle it: return hello-world module version"""
    return hello_world.__version__


@app.route("/app-version")
def app_version_endpoint():
    """Route all GET "/app-version" requests and handle it: return current module version"""
    return __version__


# start web application if run as hello world.py (not module)
if __name__ == '__main__':
    app.run()
