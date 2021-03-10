lst = []

while True:
    dat = {}

    dat['hakbun'] = input("학번 입력 => ")
    if dat['hakbun'] == "exit":
        break

    dat['irum'] = input("이름 입력 => ")
    dat['kor'] = int(input("국어점수 입력 => "))
    dat['eng'] = int(input("영어점수 입력 => "))
    dat['math'] = int(input("수학점수 입력 => "))

    dat['tot'] = dat['kor'] + dat['eng'] + dat['math']
    dat['avg'] = dat['tot'] / 3

    if dat['avg'] >= 90:
        dat['grade'] = "수"
    elif 80 <= dat['avg'] < 90:
        dat['grade'] = "우"
    elif 70 <= dat['avg'] < 80:
        dat['grade'] = "미"
    elif 60 <= dat['avg'] < 70:
        dat['grade'] = "양"
    else:
        dat['grade'] = "가"

    lst.append(dat)
    print()

print("\n\t\t        *** 성적표 ***")
print("================================================")
print("학번   이름   국어   영어   수학   총점   평균   등급")
print("================================================")
for dat in lst:
    print("%4s %3s  %3d   %3d    %3d   %3d  %6.2f   %s" % (dat['hakbun'], dat['irum'], dat['kor'], dat['eng'],
                                                  dat['math'], dat['tot'], dat['avg'], dat['grade']))