from flask import Flask

merlot = Flask(__name__)

@merlot.route('/')
def read_root():
    return {'message': "Hello, World!"}




if __name__ == "__main__":
    merlot.run(debug=True, port=7070, host='0.0.0.0')

