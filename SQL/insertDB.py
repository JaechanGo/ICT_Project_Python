import sqlite3
import time
dbconn = sqlite3.connect('tel.db')

dbcursor=dbconn.cursor()

name=input("이름 : ")
tel=input("전화번호 : ")
addr=input("주소 : ")
memo=input("메모 : ")
input_time=str(time.asctime(time.localtime(time.time())))

#dbcursor.excute("insert into tel (name, tel, addr, input_time, memo) \
#values( '"+name+ "', '"+tel+"', '"+addr+"', '"+input_time+"','"+memo+"')")

dbcursor.execute("insert into tel (name, tel, addr, input_time, memo) values (?,?,?,?,?)",
                 (name, tel, addr, input_time, memo))
#튜플이 모여있는 list 구조로 execute 을 사용 sql 구문을 data만큼 사용

dbconn.commit()
#insert문은 DML이므로 commit을 해야함

for row in dbcursor.execute('SELECT * FROM tel'):
    print(row)


dbcursor.close()
dbconn.close()