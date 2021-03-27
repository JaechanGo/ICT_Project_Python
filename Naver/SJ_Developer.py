import urllib.request
import datetime
import json
from Naver.config import *
import ssl

context = ssl._create_unverified_context()
#[Code 1]
def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req,context=context)
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
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text),page_start,display)
    url = base+node+parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

#[Code 3]
def getPostData(post, jsonResult):
    title = post['title']
    description = post['description']
    bloggerlink = post['bloggerlink']
    link = post['link']
    postdate = post['postdate']
    blogername = post['bloggername']

    jsonResult.append({ 'title':  title,'description':description,
                        'bloggerlink':bloggerlink,'link':link,
                        'postdate': postdate,'bloggername':blogername})
    return


def main():
    jsonResult = []

    #'news', 'blog', 'cafearticle'
    sNode = 'blog'
    search_text='박세욱'
    display_count = 100 #한번에 읽어올 기사

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
    print("jsonSearch = ", jsonSearch)
    while((jsonSearch != None) and (jsonSearch['display'] != 0)):
        for post in jsonSearch['items']:
            getPostData(post,jsonResult)

        nStart = jsonSearch['start']+jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)#start 값 변경에 따른 호출

    with open('%s_naever_%s.json'% (search_text,sNode),'w',encoding='utf8')as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    print('%s naver %s.json Saved ' % (search_text,sNode))

if __name__=='__main__':
    main()

