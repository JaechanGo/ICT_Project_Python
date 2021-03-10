# message = "Hello"
# messages = ["Hello World","Sangji Univercity"]
# numbers = (1,2,3)
# polygon = {"triangle":2, "rectangle":1, "line":0}
# color={"red","green","blue"}
#
# for item in message:
#     print(item)
# print("1.--------------")
#
# for item in messages:
#     print(item)
# print("2.--------------")
#
# for item in numbers:
#     print(item)
# print("3.--------------")
#
# for item in polygon:
#     print(polygon[item])
# print("4.--------------")
#
# for item in color:
#     print(item)
# #비순차의 경우

# total = 0
# for item in range(1,1010000000):
#     total += item
#     print(item)
#
# print(total)

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
            if i+1==item:
                count+=1
                print("%5d"%(item),end='')
                if count%10==0 :
                    print()
                continue

print()
print("소수의 개수는 : %d"%count)


