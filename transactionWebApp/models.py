
from app import db
class users(db.Model):
    userid = db.Column('userid', db.Integer, primary_key = True)
    balance = db.Column(db.Float)
    avg_transaction_amount = db.Column(db.Float)
    standard_deviation = db.Column(db.Float)
    avg_monthly_balance = db.Column(db.Float)
    no_of_transactions=db.Column(db.Integer)
    def __init__(self, balance, avg_transaction_amount, standard_deviation, avg_monthly_balance,no_of_transactions):
       self.balance=balance
       self.avg_transaction_amount = avg_transaction_amount
       self.standard_deviation = standard_deviation
       self.avg_monthly_balance = avg_monthly_balance
       self.no_of_transactions = no_of_transactions

class transactions(db.Model):
    tid = db.Column('tid', db.Integer, primary_key = True)
    uid = db.Column(db.Integer)
    txn_date = db.Column(db.Date)
    txn_type = db.Column(db.VARCHAR(2))
    amount = db.Column(db.Float)
    txn_marked=db.Column(db.SmallInteger)
    def __init__(self,uid,txn_date,txn_type,amount,txn_marked):
        self.uid=uid
        self.txn_date=txn_date
        self.txn_type=txn_type
        self.txn_marked=txn_marked
        self.amount=amount
#    whooshalchemy.whoosh_index(app, Post)