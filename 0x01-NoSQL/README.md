# 0x0D. NoSQL

## Resources
**Read or watch:**

* [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
* [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
* Building Your First Application: An Introduction to MongoDB
* [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
* [Aggregation](https://docs.mongodb.com/manual/aggregation/)
* [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
* [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/)
* [The mongo Shell](https://docs.mongodb.com/manual/reference/mongo/)

## Requirements
**MongoDB Command File**
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
* All your files should end with a new line
* The first line of all your files should be a comment: // my comment
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc
**Python Scripts**
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5.*)
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(\_\_import\_\_("my_module").\_\_doc\_\_)')
* All your functions should have a documentation (python3 -c 'print(\_\_import\_\_("my_module").my_function.\_\_doc\_\_)'
* Your code should not be executed when imported (by using if \_\_name__ == "\_\_main\_\_":)

## More Info
**Install MongoDB 4.2 in Ubuntu 18.04**
[Official installation guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```
Potential issue if documents creation doesn’t work or this error: `Data directory /data/db not found., terminating` ([source](https://bryantson.medium.com/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479) and [source](https://stackoverflow.com/questions/37702957/mongodb-data-db-not-found))

```bash
$ sudo mkdir -p /data/db
```

**Use “container-on-demand” to run MongoDB**
* Ask for container Ubuntu 18.04 - MongoDB
* Connect via SSH
* Or via the WebTerminal
* In the container, you should start MongoDB before playing with it:
```bash
$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
```
