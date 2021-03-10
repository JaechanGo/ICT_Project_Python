list=[]
while True:
    dat={}

    dat['code']=input("제품코드 =>")
    if dat['code'] == "exit":
        break

    dat['name']=(input("제품명 =>"))
    dat['count']=(int(input("수량 =>")))
    dat['price']=(int(input("단가 =>")))

    dat['tot']=(dat["count"] + dat["price"] )

    list.append(dat)

print("\n\t\t\t ...   성적   ...")
print("=============================================")
print(" 제품코드   제품명     수량     단가     판매금액")
print("=============================================")
for dat in list:
    print("%6s  %5s     %3d    %5d  %8d"  % (dat['code'],dat['name'],dat['count'],
                                        dat['price'],dat['tot']))
