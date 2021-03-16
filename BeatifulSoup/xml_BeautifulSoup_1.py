from bs4 import BeautifulSoup

fp = open("song.xml","r")
soup=BeautifulSoup(fp,"html.parser")

for son in soup.findAll("song"):
    print(son['album'])
    print(son.title.string)
    print(son.length.string)
    print()
