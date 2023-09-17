import json
import datetime
import itertools
import pandas as pd


def processdict(responsedata, counter):
    print("#processdict#:")
    # print("newdict:", newpayload)
    # print("newlist:", newpayloadlist)clear
    # newpayloadlist.append(newpayload)
    for sub_key, sub_value in responsedata.items():
        # print(sub_key, sub_value)
        if type(sub_value) is list:
            processlist(sub_key, sub_value, counter)
            counter += 1
        if type(sub_value) is dict:
            processdict(sub_value, counter)
        if type(sub_value) not in [dict, list]:
            processstr(sub_key, sub_value, 0)
    counter += 1


def processlist(key, responsedata, counter):
    print("#processlist#:", key)
    strcounter = 0
    for sub_key in range(len(responsedata)):
        # createcustomjson(responsedata[sub_key])
        # print(responsedata[sub_key])
        if type((responsedata[sub_key])) is dict:
            processdict(responsedata[sub_key], counter)
        if type((responsedata[sub_key])) is list:
            processlist(key, responsedata[sub_key], counter)
        if type((responsedata[sub_key])) not in [dict, list]:
            processstr(key+str(strcounter), responsedata[sub_key], counter)
            strcounter += 1
    counter += 1


def processstr(key, value, counter):
    print("#processstr#:")
    # newpayload[key] = value
    # print(newpayload)
    print("{}:Key = {} : Value = {}".format(counter, key, str(value)))
    # newpayloadlist.append(newpayload)
    # return newpayload


def createcustomjson(responsedata):
    print("#createcustomjson#:", type(responsedata))
    if type(responsedata) in [dict]:
        processdict(responsedata, counter)
    if type(responsedata) in [list]:
        processlist(responsedata, counter)
    if type(responsedata) in [str]:
        processstr('', responsedata, counter)
    if type(responsedata) in [int]:
        None


# filters = ['LaunchTime', 'AmiLaunchIndex', 'Tags', 'Enabled']
# filters = ['Instances']

newresponsedata = {
    "Instances": [{
        "AmiLaunchIndex": 123,
        "ImageId": "img23232355abc",
        "InstanceId": "ins23232323",
        "LaunchTime": datetime.datetime(2015, 1, 1),
        "Tags": ['abc', 'def', 'ghe'],
        "Enabled": True

    },
        {
        "AmiLaunchIndex": 124,
        "ImageId": "img23232355abc",
        "InstanceId": "ins23232323",
        "LaunchTime": datetime.datetime(2021, 5, 1),
        "Tags": ['xyz', 'dse', 'fse'],
        "Enabled": False
    },
        {
        "AmiLaunchIndex": 125,
        "ImageId": "img23232355abc",
        "InstanceId": "ins23232323",
        "LaunchTime": datetime.datetime(2021, 5, 1),
        "Tags": ['xyz', 'dse', 'fse'],
        "Enabled": False
    }
    ]}
counter = 0
newpayload = {}
newpayloadlist = []
createcustomjson(newresponsedata)
