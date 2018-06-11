import mysql.connector
from mysql.connector import errorcode
# from databaseConfig import DB_NAME,TABLES,USER_NAME, PASSWORD
from databaseConfig import *



class Dbo:

    def connect(self):
        return mysql.connector.connect(user=USER_NAME, password=PASSWORD,
                                           host='127.0.0.1',
                                           database=DB_NAME)
    def createTables(self):
        self.cnx = self.connect()
        # To create table if not exists
        cursor = self.cnx.cursor()
        for name, ddl in TABLES.items():
            try:
                print("Creating table {}: ".format(name), end='')
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        cursor.close()
	# common insert function for users and transaction table data
    def insertData(self,tableName,data):
        self.cnx = self.connect()
        cursor = self.cnx.cursor()
        if(tableName==transactionTableName):
            add_transaction = ("INSERT INTO transactions "
                        "(uid,  txn_date, txn_type, amount) "
                        "VALUES (%s, %s, %s, %s)")
            cursor.execute(add_transaction, data)
            id=cursor.lastrowid
        elif (tableName==usersTableName):
            add_user = ("INSERT INTO users "
                        "(userid, balance, avg_transaction_amount, standard_deviation,avg_monthly_balance,no_of_transactions) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
            cursor.execute(add_user, data)
            id = cursor.lastrowid
        cursor.close()
        self.cnx.commit()
        return id
	# Check if user exists and retrieve its entry so that it can be further used for calculations
    def findUserById(self,userId):

        self.cnx1 = self.connect()
        cursor = self.cnx1.cursor()
        query="SELECT * FROM users WHERE userid = %s"
        # query = ("SELECT first_name, last_name, hire_date FROM employees "
        #          "WHERE hire_date BETWEEN %s AND %s")
        # query = "SELECT * FROM users"
        userId=str(userId)
        cursor.execute(query,(userId,))
        row = cursor.fetchone()
        cursor.close()
        self.cnx1.commit()
        if row is not None:
            return row;
        return 0;


    def getTransactionsByUserId(self,userId):
        self.cnx=self.connect()
        cursor = self.cnx.cursor()
        query="SELECT * FROM transactions WHERE uid=%s"
        userId=str(userId)
        cursor.execute(query,(userId,),multi=True)

        data=cursor.fetchall()
        transactionAmount=[]
        transactionDate=[]
        for row in data:
            transactionAmount.append(row[4])
            transactionDate.append(row[2])
        cursor.close()
        self.cnx.commit()
        return (transactionAmount,transactionDate)

    def updateTransaction(self,tid):
        self.cnx = self.connect()
        cursor = self.cnx.cursor()
        query = "UPDATE transactions SET txn_marked=1 WHERE tid=%s"
        tid = str(tid)
        cursor.execute(query, (tid,), multi=True)
        cursor.close()
        self.cnx.commit()

    def updateUser(self,data):
        self.cnx = self.connect()
        cursor = self.cnx.cursor()
        query = "UPDATE users SET balance=%s, avg_transaction_amount=%s,standard_deviation=%s,no_of_transactions=%s WHERE userid=%s"

        cursor.execute(query, data, multi=True)
        cursor.close()
        self.cnx.commit()