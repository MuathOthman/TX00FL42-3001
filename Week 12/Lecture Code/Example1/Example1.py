from flask import Flask, request

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    number1 = float(args.get("number1")) # 20
    number2 = float(args.get("number2")) # 30
    name = str(args.get("name"))
    total_sum = number1+number2
    print(name)
    return str(total_sum)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
