import csv
filename =input()
fp = open(filename, 'r', encoding='utf-8')
#한줄씩 읽어 들이기
reader = csv.reader(fp) #list객체로 저장
for cells in reader:    #list의 객체접근
    print(cells)
    #print(cells[0],cells[1],cells[2])
fp.close()