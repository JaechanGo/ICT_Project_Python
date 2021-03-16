import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
for row in dbcursor.execute('SELECT * FROM tel order by id asc'):
    print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[5])+"\t"+str(row[4])+"\t")
    print("--------------------------------------------------------------------------------------------")
    
res = dbcursor.execute('SELECT * FROM tel order by id desc')



name=input("삭제할 이름 입력 : ")
flag = 0
for row in res :
    if row[1] == name:
        print(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(
            row[5]) + "\t" + str(row[4]) + "\t")
        dbcursor.execute("delete from tel where name=?", (name,))
        dbconn.commit()
        flag = 1

if flag == 0:
    print("\n삭제 실패!!\n")
else:
    print("\n삭제 완료!!\n")

dbcursor.close()
dbconn.close()