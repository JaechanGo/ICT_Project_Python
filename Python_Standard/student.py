list=[]
while True:
    dat={}

    dat['hackbun']=input("학번입력 =>")
    if dat['hackbun'] == "exit":
        break

    dat['name']=(input("이름입력 =>"))
    dat['kor']=(int(input("국어 점수 =>")))
    dat['math']=(int(input("수학 점수 =>")))
    dat['eng']=(int(input("영어 점수 =>")))

    dat['tot']=(dat["kor"] + dat["math"] + dat["eng"])
    dat['avg']=(dat["tot"]/3)

    if dat['avg']>=90:
        dat['grade'] = "수"
    elif 80 <= dat['avg']<90:
        dat['grade'] = "우"
    elif 80 <= dat['avg']<90:
        dat['grade'] = "미"
    elif 80 <= dat['avg']<90:
        dat['grade'] = "양"
    else:
        dat['grade'] = "가"

    list.append(dat)

print("\n\t\t\t ...   성적   ...")
print("=============================================")
print(" 학번   이름     국어   수학   영어   총점   평균   등급")
print("=============================================")
for dat in list:
    print("%4s  %5s  %3d  %3d  %3d  %3d  %6.2f %2s"  % (dat['hackbun'],dat['name'],dat['kor'],dat['math'],dat['eng']
                                                   ,dat['tot'],dat['avg'],dat['grade']))
