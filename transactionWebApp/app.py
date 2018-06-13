# -*- coding: UTF-8 -*-
"""
hello_urlredirect: Using functions redirect() and url_for()
"""
from flask import Flask, redirect, url_for,render_template, abort
from flask_sqlalchemy import SQLAlchemy
from config import databaseURL
from flask import jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseURL
db = SQLAlchemy(app)
import models
PRODUCTS = {
    'iphone': {
        'name': 'iPhone 5S',
        'category': 'Phones',
        'price': 699,
    },
    'galaxy': {
        'name': 'Samsung Galaxy 5',
        'category': 'Phones',
        'price': 649,
    },
    'ipad-air': {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649,
    },
    'ipad-mini': {
        'name': 'iPad Mini',
        'category': 'Tablets',
        'price': 549
    }
}
@app.route('/')
@app.route('/users')
def transactionSummary():
    users=models.users.query.all()
    # print(users)
    # for item in users:
    #     print(item.userid, item.balance)
    return render_template('transactionSummary.html', users=users)

@app.route('/transactions')
def transactions():
    transactions = models.transactions.query.all()
    print(transactions)
    return render_template('transactions.html', transactions=transactions)


@app.route('/user-transactions/<uid>', methods=['GET'])
def userTransactions(uid):
    print(uid)
    userTransactions=models.transactions.query.filter_by(uid=uid).all()
    print(transactions)
    return render_template('userTransactions.html', userTransactions = userTransactions)

@app.route('/alerts')
def alerts():
    markedTransactions = models.transactions.query.filter_by(txn_marked=1)
    # markedTransactions = models.transactions.query.all()
    return render_template('alerts.html', markedTransactions=markedTransactions)

if __name__ == '__main__':
    app.run(debug=True)