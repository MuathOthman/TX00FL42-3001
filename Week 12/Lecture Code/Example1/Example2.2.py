from flask import Flask, request

app = Flask(__name__)
@app.route('/sum/<num1>/<num2>')
def calculate_sum(num1, num2):
    total_sum = int(num1)+int(num2)
    response = {
        "number1" : num1,
        "number2" : num2,
        "total_sum" : total_sum
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)