from flask import Flask, request

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    return ("Hello Students!")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
