from kafka import KafkaConsumer
import threading
import binascii
import ast
from multiprocessing import Process
from dbo import Dbo
from databaseConfig import *
import datetime
import statistics
dboObject=Dbo()
dboObject.createTables()
#Read data and call function based on transaction type
def consumeData(topic):
    try:
        consumer = KafkaConsumer(topic, value_deserializer=lambda v: binascii.unhexlify(v).decode('utf-8'))
    except:
        print("Error!!")
    for msg in consumer:
        msg=ast.literal_eval(msg.value)
        if(msg[2] == 'C'):
            performCreditOperation(msg)
        elif (msg[2] == 'D'):
            performDebitOperation(msg)
# Retrieves month number used for forming date to be inserted in sql
def getMonth(month):
    if(month=='Jan'):
        return 1
    if (month == 'Feb'):
        return 2
    if (month == 'Mar'):
        return 3
    if (month == 'Apr'):
        return 4
    if (month == 'May'):
        return 5
    if (month == 'Jun'):
        return 6
    if (month == 'Jul'):
        return 7
    if (month == 'Aug'):
        return 8
    if (month == 'Sep'):
        return 9
    if (month == 'Oct'):
        return 10
    if (month == 'Nov'):
        return 11
    if (month == 'Dec'):
        return 12

#Call credit operation with flag oper setting to 1(used later for adding amount)
def performCreditOperation(msg):
    calculalate(msg, 1)
#Call credit operation with flag oper setting to -1(used later for subtracting amount or further)
def performDebitOperation(msg):
    calculalate(msg,-1)
def calculalate(msg,oper):
    try:
        userId = int(msg[0])
        amount = int(msg[3])
        dateObj = msg[1]
        dateObj = datetime.date(int(dateObj[5:9]), getMonth(dateObj[2:5]), int(dateObj[0:2]))
        #insert transaction into transaction table
        try:
            tid=dboObject.insertData(transactionTableName,(userId,dateObj,msg[2],amount))
        except Exception as ex:
            print("Failed to insert data in transactions: "+str(ex))
        #find user and if not exists insert its entry in users table
        try:
            data=dboObject.findUserById(userId)
			# If no data retrieved, means no user entry exists
            if(data==0):
                #User not found / exists, add user in users table
                try:
                    dboObject.insertData(usersTableName, (userId, oper*amount, amount, 0.00, amount, 1))
                except Exception as ex:
                    print("Error in inserting User data" + str(ex))
            else:
                #user exists/ update user table
                (userId,total_balance,avg_transaction_amount,standard_deviation,avgMonthlyBalance,noOfTransactions)=data
                
				#calculate total balance
				total_balance=float(total_balance)+float(amount*oper)
                
				#calculate average transaction amount
				avg_transaction_amount = float(avg_transaction_amount * noOfTransactions)+float(amount)
                noOfTransactions=noOfTransactions+1
                avg_transaction_amount=float(avg_transaction_amount)/noOfTransactions
                
				try:
                    #get all transacations of user to calculate standard deviation of transaction amount
                    (transactionsAmountList,transactionDateList)=dboObject.getTransactionsByUserId(userId)
                except Exception as ex:
                    print("Failed to query transaction data for User: " + str(ex))
                
				#calculating standard deviation
                standard_deviation = statistics.stdev(transactionsAmountList)
                
				#check if balance goes above 2 * standard deviation
                if(total_balance>2*standard_deviation):
                    #mark transaction in transaction table
                    try:
                        dboObject.updateTransaction(tid)
                    except Exception as ex:
                        print("Failed to update transaction."+str(ex))
                
				try:
                    print("update user called" + str(noOfTransactions))
                    dboObject.updateUser((total_balance,avg_transaction_amount,standard_deviation,noOfTransactions,userId))
                except Exception as ex:
                    print("Failed to update user transaction summary."+str(ex))
        except Exception as ex:
            print("Failed to query data in Users: "+str(ex))
    except Exception as ex:
        print("Error in inserting data"+str(ex))

try:
    # _thread.start_new_thread( consumeData, ("C_transac" ) )
    # _thread.start_new_thread( consumeData, ("D_transac" ) )
    t1 = Process(target=consumeData, args=('Credit_transac',))
    t2 = Process(target=consumeData, args=('Debit_transac',))
    t1.start()
    t2.start()
except:
   print ("Error: unable")