from flask import Flask, jsonify
import pandas as pd
from flask import request

app = Flask(__name__)

data = pd.read_excel("Students.xlsx")

@app.route('/students')
def get_students():
    name = request.args.get('name')
    print(name)
    for i in range(len(data)):
        if data['Etunimi'][i] == name:
            return data['Sukunimi'][i]


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)