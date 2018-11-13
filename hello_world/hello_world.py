__version__ = '0.1'


def hello():
    """Method return <<hello world>>"""
    return "Hello world!"


# start web application if run as hello world.py (not module)
if __name__ == '__main__':
    print hello()
