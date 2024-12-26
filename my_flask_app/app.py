from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data1')
def get_data1():
    data1 = {
        'message': 'Салат с кальмаром',
        'status': 'Дары моря с кайфом',
        'items': [f"{205} ккал"]
    }
    return jsonify(data1)

@app.route('/api/data2')
def get_data2():
    data2 = {
        'message': 'Шашлык',
        'status': 'Вая какой барашка',
        'items': [f"{580}ккал"]
    }
    return jsonify(data2)

@app.route('/api/data3')
def get_data3():
    data3 = {
        'message': 'Овощной салат',
        'status': 'Чтобы на попе не было прыщей',
        'items': [f"{14}ккал"]
    }
    return jsonify(data3)

if __name__ == '__main__':
    app.run(debug=True)
