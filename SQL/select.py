import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

print("No \t 성명   \t 전화번호 \t 주소 \t\t 메모 \t 입력일자")
print("---------------------------------------------------------------")

#for row in dbcursor.execute('SELECT * FROM tel order by id asc'):
#    print(str(row[0]) + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[5] + "\t" + row[4])
#    print("-----------------------------------------------------------")

#fetchone() 예
#res = dbcursor.execute('SELECT * FROM tel order by id asc')
#row = res.fetchone()
#print(str(row[0]) + "\t" + row[1] + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[5]) +"\t"+ str(row[4]))
#print("-----------------------------------------------------------")

#fetchall()의
res = dbcursor.execute('SELECT * FROM tel order by id asc')
for row in res.fetchall():
    print(str(row[0]) + "\t" + row[1] + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[5]) +"\t"+ str(row[4]))
    print("-----------------------------------------------------------")

dbcursor.close()
dbconn.close()
