from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)

data = pd.read_excel("Students.xlsx")

@app.route('/students/<name>')
def get_students(name):
    print(name)
    for i in range(len(data)):
        if data['Etunimi'][i] == name:
            response = {
                "Etunimi": data['Etunimi'][i],
                "Sukunimi": data['Sukunimi'][i],
            }
            return jsonify(response)

CORS(app)
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)