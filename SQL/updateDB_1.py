import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()


name = input("수정할 이름 입력 : ")
res = dbcursor.execute('SELECT * FROM tel where name =?',(name,)) #동일한 데이터가 있는지 확인하는 라인
flag = 0
for row in res :
    tel =input("전화번호 : ")
    addr = input("주소 : ")
    memo = input("메모 : ")
    dbcursor.execute("update tel set tel=?, addr=?, memo=? where name=?", (tel,addr, memo, name))
    dbconn.commit()
    flag = 1

if flag == 0:
    print("\n수정실패!!\n")
else :
    print("\n수정완료!!\n")

dbcursor.close()
dbconn.close()