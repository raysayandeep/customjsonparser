import json
import datetime
# filedata = open('input1.json', 'r')

# data = json.load(filedata)


def objecttype(object):
    if type(object) is dict:
        return 'dict'
    if type(object) is list:
        return 'list'
    if type(object) is str:
        return 'str'
    if type(object) is int:
        return 'int'
    if type(object) is datetime.datetime:
        return 'date'
    if type(object) is bool:
        return 'bool'


def processdict(object, uniquekey, record_counter):
    for keys, values in object.items():
        print(">>>>>>DICT<<<<<<<", record_counter, keys)
        # print(keys, values)
        if keys == uniquekey:
            print(">>>>>>RECORD FOUND<<<<<<<", record_counter)
            record_counter += 1
        if type(values) is dict:
            processdict(values, uniquekey, record_counter)
        if type(values) is list:
            print(">>>>>>LIST ENTER FROM DICT<<<<<<<", record_counter)
            processlist(values, uniquekey, record_counter)
        if type(values) is str:
            processstring(keys, values, record_counter)
        if type(values) is int:
            processint(keys, values, record_counter)
        if type(values) is bool:
            processboolean(keys, values, record_counter)
        if type(values) is datetime.datetime:
            processdatetime(keys, values, record_counter)
        # else:
            # print(type(values), values)


def processlist(object, uniquekey, record_counter):
    for item in range(len(object)):
        print(">>>>>>LIST<<<<<<<", record_counter, item)
        # print(object[item])
        if type(object[item]) is list:
            print(">>>>>>LIST ENTER FROM LIST<<<<<<<", record_counter)
            processlist(object[item], uniquekey, record_counter)
        if type(object[item]) is dict:
            processdict(object[item], uniquekey, record_counter)
        if type(object[item]) is str:
            processstring('', object[item], record_counter)
        if type(object[item]) is int:
            processint('', object[item], record_counter)
        if type(object[item]) is bool:
            processboolean('', object[item], record_counter)
        if type(object[item]) is datetime.datetime:
            processdatetime('', object[item], record_counter)
        # else:
            # print(type(object[item]), object[item])
    print(">>>>>>LIST END<<<<<<<", record_counter)


def processstring(key, object, record_counter):
    print(">>>>>>STRING<<<<<<<", record_counter)
    construct(key, object, record_counter)


def processint(key, object, record_counter):
    print(">>>>>>INTEGER<<<<<<<", record_counter)
    construct(key, object, record_counter)


def processdatetime(key, object, record_counter):
    print(">>>>>>DATETIME<<<<<<<", record_counter)
    construct(key, str(object), record_counter)


def processboolean(key, object, record_counter):
    print(">>>>>>BOOLEAN<<<<<<<", record_counter)
    construct(key, object, record_counter)


def processobject(object, uniquekey, record_counter):
    print(">>>>>>PROCESS OBJECT<<<<<<<", record_counter)
    objtype = objecttype(object)
    if objtype == 'dict':
        processdict(object, uniquekey, record_counter)
    if objtype == 'list':
        print(">>>>>>LIST ENTER FROM PROCESS OBJECT<<<<<<<", record_counter)
        processlist(object, uniquekey, record_counter)
    if objtype == 'str':
        processstring('', object)
    if objtype == 'int':
        processint('', object)
    if objtype == 'date':
        processdatetime('', object)
    if objtype == 'bool':
        processboolean('', object)


def construct(key, value, record_counter):
    print(">>>>>>CONSTRUCT<<<<<<<", record_counter)
    print('{}.{}:{}'.format(record_counter, key, value))
    """ if key in newdict:
        print(">>>>>>NEW RECORD<<<<<<<")
        print(newlist)
        newlist.append(newdict)
    else: """
    newdict[key+str(record_counter)] = value
    print(">>>>>>CONSTRUCT END<<<<<<<", record_counter)


data = {"clients":
        [
            {
                "name": {
                    "fname": "Miss Layla",
                    "lname": "Elliot"
                },
                "address": {
                    "addressline1": "92096 Willie Fork",
                    "addressline2": "Rahata",
                    "locality": "Bhardaha",
                    "city": "East Lexieville",
                    "state": "Tennessee",
                    "pincode": 90224
                },
                "contact": {
                    "mobile": {
                        "coutrycode": "+1",
                        "number": "981-687-7064 x176"
                    },
                    "home": {
                        "citycode": "025",
                        "areacode": "2345",
                        "local": "9734",
                        "LaunchTime": datetime.datetime(2021, 5, 1)
                    }
                }
            },
            {
                "name": {
                    "fname": "Mr. Larry",
                    "lname": "Page"
                },
                "address": {
                    "addressline1": "34 Willie St",
                    "addressline2": "Penggila",
                    "locality": "Yellow Stone",
                    "city": "South California",
                    "state": "Texas",
                    "pincode": 50786
                },
                "contact": {
                    "mobile": {
                        "coutrycode": "+1",
                        "number": "456-687-7064",
                        "enabled": True
                    },
                    "home": {
                        "citycode": "025",
                        "areacode": "3225",
                        "local": "5422"
                    }
                }
            }
        ]
        }

newdict = {}
newlist = []
processobject(data, 'name', 0)
print(newdict)
