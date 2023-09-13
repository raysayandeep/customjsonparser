import json


def filereader(filename, mode):
    fileobject = open(filename, mode)
    return fileobject


def loadjsondata(fileobject):
    return json.load(fileobject)


def processdict(key, jsondata, keylist, newjson):
    # print(type(jsondata))
    if type(jsondata) not in [int, list, str]:
        for key1, value in jsondata.items():
            # print(keylist)
            # print(key1)
            if key1 in keylist:
                # print(key1)
                newjson[key1] = value
            if type(value) not in [list, str, int]:
                processdict(key1, value, keylist, newjson)
            if type(value) not in [dict, str, int]:
                processlist(key1, value, keylist, newjson)
            if type(value) not in [dict, list, int]:
                processstring(value)
            if type(value) not in [dict, list, str]:
                processint(value)
    return newjson


def processlist(key, jsondata, keylist, newjson):
    # print(type(jsondata))
    if type(jsondata) not in [int, dict, str]:
        for value in range(len(jsondata)):
            # print(value)
            if type(jsondata[value]) not in [int, list, str]:
                processdict(key, jsondata[value], keylist, newjson)
            if type(jsondata[value]) not in [int, dict, str]:
                processlist(key, jsondata[value], keylist)
            if type(jsondata[value]) not in [dict, list, int]:
                processstring(jsondata[value])
            if type(jsondata[value]) not in [dict, list, str]:
                processint(jsondata[value])


def processstring(jsondata):
    # print('string:' + jsondata)
    return None


def processint(jsondata):
    # print('int:' + str(jsondata))
    return None


def createcustomjson(filedata, keylist, newdict):
    jsondata = loadjsondata(filedata)
    newjson = processdict('', jsondata, keylist, newdict)
    print(newjson)
    return newjson


def writejson(newjson, newfiledata):
    json.dump(newjson, newfiledata, indent=4)


# defining keys for which new json file will be created
keylist = ['fname', 'address', 'yearwiseupdate']
# initializing a new Dictionary for creating the custom json object
newdict = {}
# Opens the input json file and create file object
filedata = filereader('test.json', 'r')
# creates the new custom json object
newjson = createcustomjson(filedata, keylist, newdict)
# Opens the output json file and create file object
newfiledata = filereader('output.json', 'w')
# Writes the output json file
writejson(newjson, newfiledata)
