

DB_NAME = 'transactiondb'
USER_NAME='sadmin'
PASSWORD='admin'
usersTableName='users'
transactionTableName='transactions'
TABLES = {}
TABLES[usersTableName] = (
    "CREATE TABLE `users` ("
    "  `userid` int(11) NOT NULL,"
    "  `balance` float NOT NULL,"
    "  `avg_transaction_amount` float NULL,"
    "  `standard_deviation` float NOT NULL,"
    "  `avg_monthly_balance` float NULL,"
    "  `no_of_transactions` int(11),"
    "  PRIMARY KEY(userid)"
    ") ENGINE=InnoDB")

TABLES[transactionTableName] = (
    "CREATE TABLE `transactions` ("
    "  `uid` int(11) NOT NULL,"
    "  `tid` int(11) NOT NULL AUTO_INCREMENT,"
    "  `txn_date` date,"
    "  `txn_type` varchar(2),"
    "  `amount` float(11),"
    "  `txn_marked` smallint ,"
    " KEY (`tid`)"
    ") ENGINE=InnoDB")
