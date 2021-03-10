# -*- coding: utf-8 -*-
lst = []

while True:
    dict_rec = {}

    dict_rec["code"] = input("제품코드 입력 => ")
    if dict_rec["code"].lower() == "exit":
        break
    dict_rec["irum"] = input("제품명 입력 => ")
    dict_rec["su"] = int(input("수량 입력 => "))
    dict_rec["price"] = int(input("단가 입력 => "))

    dict_rec["kumack"] = dict_rec["su"] * dict_rec["price"]

    lst.append(dict_rec)
    print()

print("\n                   *** 상품정보 ***")
print("======================================================")
print("제품코드      제품명        수량        단가       판매금액")
print("======================================================")
for data in lst:
    print("%4s       %4s       %4d       %6d     %8d" %
          (data["code"], data["irum"], data["su"], data["price"], data["kumack"]))
print("======================================================")