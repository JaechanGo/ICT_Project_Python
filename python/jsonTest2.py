import json
JSON_FIlE="./test.json"
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

    repos = JSON_DATA['snapshot']['repos']
    userid = JSON_DATA['snapshot']['userid']
    pw = JSON_DATA['snapshot']['passwd']

    print("repos value : " + repos)
    print("userid value : " + userid)
    print("passwd value : " + pw)

if __name__=="__main__":
    proc_json()
