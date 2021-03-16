import sqlite3
#삭제가 되었는지 확인은 불가한 Del_DB
dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
for row in dbcursor.execute('SELECT * FROM tel order by id asc'):
    print(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[5]) + "\t" + str(
        row[4]) + "\t")
    print("--------------------------------------------------------------------------------------------")

name = input("삭제할 이름 입력 : ")
res = dbcursor.execute("delete from tel where name=?", (name,))
print(res)
dbconn.commit()

dbcursor.close()
dbconn.close()