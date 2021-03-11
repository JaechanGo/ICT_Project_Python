import urllib.request
import datetime
import json
from Naver.config import *

#[Code 1]
def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() ==200:
            print("[%s] Url Request Success "% datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s"%(datetime.datetime.now(), url))
        return None


#[Code 2]
def getNaverSearchResult(sNode, search_text, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/$s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text),page_start,display)
    url = base+node+parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

#[Code 3]


