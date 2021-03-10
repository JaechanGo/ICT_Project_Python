import json
JSON_FIlE= "test.json"
JSON_DATA={}

def read_json(filename) :
    f = open(filename, 'rt')
    #f = oepn(filename, 'rt', encording='utf-8)
    js = json.loads(f.read())
    f.close()
    return js

def proc_json():
    global JSON_FIlE
    global JSON_DATA
    JSON_DATA = read_json(JSON_FIlE)

    for data in JSON_DATA:
        print(data)
        for item in JSON_DATA[data]:
            print("\t%s%s" % (item, JSON_DATA[data][item]))
        print()

if __name__=="__main__":
    proc_json()
