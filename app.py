from flask import Flask, jsonify, request

app = Flask(__name__)

expenses = [
    {
        'id': 1,
        'description': 'Amazon Purchase',
        'payment_type': 'Credit Card',
        'value': 30.50
    },
    {
        'id': 2,
        'description': 'Groceries',
        'payment_type': 'Cash',
        'value': 15.37
    },
    {
        'id': 3,
        'description': 'Netflix',
        'payment_type': 'Debit Card',
        'value': 17.99
    }
] 
  
earnings = [
    {
        'id': 1,
        'description': 'Wage',
        'earning_type': 'Deposit',
        'value': 1500
    },
    {
        'id': 2,
        'description': 'Freelance',
        'earning_type': 'Cash',
        'value': 120
    },
    {
        'id': 3,
        'description': 'Stocks',
        'earning_type': 'Deposit',
        'value': 267.83
    }
]

@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    return jsonify(expenses)

@app.route('/expenses/<int:id>', methods=['GET'])
def get_expenses_by_id(id):
    for expense in expenses:
        if expense.get('id') == id:
            return jsonify(expense)
        
@app.route('/expenses', methods=['POST'])
def insert_expense():
    new_expense = request.get_json()
    expenses.append(new_expense)
    return jsonify(expenses)

@app.route('/expenses/<int:id>', methods=['PUT'])
def edit_expense(id):
    editted_expense = request.get_json()
    for i, expense in enumerate(expenses):
        if expense.get('id') == id:
            expenses[i].update(editted_expense)
            return jsonify(expenses[i])
        
@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    for i, expense in enumerate(expenses):
        if expense.get('id') == id:
            del expenses[i]
    return jsonify(expenses)


@app.route('/earnings', methods=['GET'])
def get_all_earnings():
    return jsonify(earnings)

@app.route('/earnings/<int:id>', methods=['GET'])
def get_earnings_by_id(id):
    for earning in earnings:
        if earning.get('id') == id:
            return jsonify(earning)
        
@app.route('/earnings', methods=['POST'])
def insert_earning():
    new_earning = request.get_json()
    earnings.append(new_earning)
    return jsonify(earnings)

@app.route('/earnings/<int:id>', methods=['PUT'])
def edit_earning(id):
    editted_earning = request.get_json()
    for i, earning in enumerate(earnings):
        if earning.get('id') == id:
            earnings[i].update(editted_earning)
            return jsonify(earnings[i])
        
@app.route('/earnings/<int:id>', methods=['DELETE'])
def delete_earning(id):
    for i, earning in enumerate(earnings):
        if earning.get('id') == id:
            del earnings[i]
    return jsonify(earnings)

app.run(port=5000, host='localhost', debug=True)