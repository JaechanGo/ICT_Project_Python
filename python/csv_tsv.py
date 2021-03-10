import csv

#.tst쓰기
f = open('test.csv','w',encoding='utf-8',newline='')
wr = csv.writer(f, delimiter='\t')
wr.writerow([1,"김정수", False])
wr.writerow([2,"박상미", True])
f.close()

#tsv 읽기
f = open('test.csv', 'r', encoding='utf-8')
rdr = csv.reader(f,delimiter='\t') #list객체로 저장
r=list(rdr)
print(r)
print("ID=%s : Name=%s"%(r[0][0], r[0][1]))

f.close()