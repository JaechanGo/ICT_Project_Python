import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

print("No \t 성명      \t 전화번호 \t\t 주소 \t\t 메모 \t 입력일자")
print("--------------------------------------------------------------------------------------------")

for row in dbcursor.execute('SELECT * FROM tel order by id asc'):
    print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[5])+"\t"+str(row[4])+"\t")
    print("--------------------------------------------------------------------------------------------")