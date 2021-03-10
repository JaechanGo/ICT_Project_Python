# -*- coding: utf-8 -*-   
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

if num1 > num2:
    min_num = num2
    max_num = num1
else:
    min_num = num1
    max_num = num2

print()

cnt = 0 # 소수의 갯수를 저장
for i in range(min_num, max_num + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else: # 소수인 경우 수행
        print("%5d " % (i), end="")
        cnt += 1 # 소수의 갯수 카운트
        if cnt % 10 == 0: # 소수의 갯수가 10의 배수이면 줄바꿈 수행
            print()

if cnt % 10 != 0:
    print()

print("총소수의 갯수 = %d" % (cnt))