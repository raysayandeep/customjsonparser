import json
import datetime
import data as dt


def filereader(filename, mode):
    fileobject = open(filename, mode)
    return fileobject


def writejson(newjson, newfiledata):
    json.dump(newjson, newfiledata, indent=4)


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


def processdict(pkey, object):
    for key, value in object.items():
        if type(value) is dict:
            processdict((pkey+'_'+key), value)
        if type(value) is list:
            processlist((pkey+'_'+key), value)
        if type(value) is str:
            processstring((pkey+'_'+key), value)
        if type(value) is int:
            processint((pkey+'_'+key), value)
        if type(value) is bool:
            processboolean((pkey+'_'+key), value)
        if type(value) is datetime.datetime:
            processdatetime((pkey+'_'+key), value)


def processlist(key, object):
    for item in range(len(object)):
        if type(object[item]) is list:
            print(">>>>>>LIST ENTER FROM LIST<<<<<<<")
            processlist(str(item)+'_'+key, object[item])
        if type(object[item]) is dict:
            processdict(str(item)+key, object[item])
        if type(object[item]) is str:
            processstring(str(item)+'_'+key, object[item])
        if type(object[item]) is int:
            processint(str(item)+'_'+key, object[item])
        if type(object[item]) is bool:
            processboolean(str(item)+'_'+key, object[item])
        if type(object[item]) is datetime.datetime:
            processdatetime(str(item)+'_'+key, object[item])


def processstring(key, object):
    construct(key, object)


def processint(key, object):
    construct(key, object)


def processdatetime(key, object):
    # print("date:", object.strftime("%m/%d/%Y, %H:%M:%S"))
    construct(key, object.strftime("%m/%d/%Y, %H:%M:%S"))


def processboolean(key, object):
    construct(key, object)


def processobject(object):
    objtype = objecttype(object)
    if objtype == 'dict':
        processdict('', object)
    if objtype == 'list':
        processlist('', object)
    if objtype == 'str':
        processstring('', object)
    if objtype == 'int':
        processint('', object)
    if objtype == 'date':
        processdatetime('', object)
    if objtype == 'bool':
        processboolean('', object)


def construct(key, value):
    filterflag = 0
    if len(filterdata):
        for filters in (range(len(filterdata))):
            filterflag = key.find(filterdata[filters])
            if filterflag > 0:
                newdict[key] = value
    else:
        newdict[key] = value


def returnasobject(payload):
    return payload


if __name__ == '__main__':

    # reading data from json file
    # filedata = filereader('input.json', 'r')
    # data = json.load(filedata)

    # read data from response
    data = dt.data

    # Initialize the placeholder for output
    newdict = {}

    # filter for keys
    filterdata = ['InstanceId', 'InstanceType', 'Tags']

    processobject(data)

    # print(returnasobject(newdict))

    newfiledata = filereader('output.json', 'w')
    writejson(newdict, newfiledata)
