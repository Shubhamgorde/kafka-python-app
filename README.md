# FleetManagement
Fleet Management portal is implemented using angular 5 and angular-cli version 1.6 or later. 
Fleet management provides a open source platform to manage fleets. There are four users in system including superadmin, tenant admin, fleet admin and driver. Tenant admin can manage his/her fleets, vehicles and users. He is also able to monitor vehicle parameters and associated reports.

## Getting Started
###About
The project illustrates using python for kafka broker setup. Used **kafka-python** library to interact with broker.
Two consumers are created(based on transaction type) using python multiprocessing library(kafka-consumer.py)
A producer is reading csv file(transaction-data.csv) and publishing data over topic
MySQL is used for maintaining *transaction summary* of user in **users** table and all *transactions* are maintained in **transactions** table

### Prerequisites
1. You need to have [Python](https://www.python.org) installed.
2. Install [Git](http://www.git-scm.com/downloads).
3. [optional]You need to have [Pycharm](https://www.jetbrains.com/pycharm) installed as a editor.
4. Please make sure that you have java 8 and environment variable set (JAVA_HOME : ~/jdk-8 path) 
5. Install [MySQL](https://dev.mysql.com/downloads/)(or you can connect to any SQL server)

##Setting up of Kafka broker
### You need to install apache zookeeper
1. Download and Extract Apache Zookeeper [here]( http://zookeeper.apache.org/releases.html#download)
2. Copy and Rename “zoo_sample.cfg” to “zoo.cfg” in ~\zookeeper-3.4.9\conf
3. Find & edit dataDir=/tmp/zookeeper to :\zookeeper-3.4.9\data using any text editor like notepad or notepad++. (change the zookeeper version as yours)
4. Add entries in System Environment Variables.
    Add in System Variables ZOOKEEPER_HOME = C:\Tools\zookeeper-3.4.9
    Edit System Variable named “Path” and append this in the last ;%ZOOKEEPER_HOME%\bin;
5. Open command prompt and type zkserver.
	```shell
zkserver
```

### Setting up Apache Kafka
1. Download and Extract Apache Kafka from [here](https://kafka.apache.org/).
2. Go to config folder in Apache Kafka and edit “server.properties” using any text editor.
3. Find log.dirs and repelace after “=/tmp/kafka-logs” to “=C:\Tools\kafka_2.10–0.10.1.1\kafka-logs”
Note: If your Apache Zookeeper on different server then change the “zookeeper.connect” property.
4. Running Apache Kafka
```shell
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

Your kafka broker is up and running.

Now You can run consumer and producer with your respective topic.

