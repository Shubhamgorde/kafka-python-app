from kafka import KafkaProducer
import time
import csv
import binascii
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')))
def sendRowData(data,topic):
    producer.send(topic, data)

with open('transaction-data.csv', "rt", encoding='utf8') as f:
    reader = csv.reader(f,dialect=csv.excel)
    print(reader)
    # header = reader.next()
    # transactionTypeINdex=header.index("Transaction type")
    for row in reader:
        if(row[2]=='C') :
            print("C"+str(row))
            sendRowData(str(row),'Credit_transac')
        elif (row[2] == 'D'):
            print("D"+str(row))
            sendRowData(str(row), 'Debit_transac')
    producer.flush()
