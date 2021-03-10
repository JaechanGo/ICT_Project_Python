num1=input("1번째 숫자 : ")
num2=input("2번째 숫자 : ")

if num1<num2 :
    maxnum=num2
    minnum=num1
else:
    maxnum=num1
    minnum=num2
print("큰수 : ", maxnum)
print("작은수 : ", minnum)
count=0
for item in range(int(minnum),int(maxnum)+1):
    for i in range(2,item):
        if item % i == 0 :
            break
        else :
            print("%5d" % (item), end='')
            count+=1
            print("%5d"%(item),end='')
            if count%10==0 :
                print()

print()
print("소수의 개수는 : %d"%count)