# -*- coding: utf-8 -*-
from sangpum_cls_1 import Sangpum_2

def f_menu():
    print("  *** 메뉴 ***")
    print("1. 제품정보 입력")
    print("2. 제품정보 출력")
    print("3. 제품정보 조회")
    print("4. 제품정보 수정")
    print("5. 제품정보 삭제")
    print("6. 프로그램 종료")
    print()

def input_proc():
    obj = Sangpum()
    obj.input_sangpum()
    obj.process_sangpum()
    lst.append(obj)
    print("\n제품정보 입력 성공!!!\n")

def output_proc():
    if len(lst) == 0:
        print("\n출력할 데이터가 없습니다!!!\n")
        return

    print("                   *** 상품정보 ***")
    print("======================================================")
    print("제품코드      제품명        수량        단가       판매금액")
    print("======================================================")
    total = 0
    for obj in lst:
        obj.output_sangpum()
        total += obj.kumack
    print("======================================================")
    print("\t\t\t\t\t\t    총 판매 금액 : %8d\n" % total)

def search_proc():
    code = input("조회할 제품코드를 입력하세요 : ")
    for obj in lst:
        if obj.code == code:
            print("\n제품코드    제품명        수량        단가      판매금액")
            print("=======================================================")
            print("%4s       %4s       %4d       %6d     %8d" %
                (obj.code, obj.irum, obj.su, obj.price, obj.kumack))
            print("=======================================================\n")
            break
    else:
        print("\n조회할 체품코드 %s가 없습니다!!\n" % code)

def update_proc():
    code = input("수정할 제품코드를 입력하세요 : ")
    for obj in lst:
        if obj.code == code:
            obj.su = int(input("수량 입력 => "))
            obj.price = int(input("단가 입력 => "))
            obj.process_sangpum()
            print()
            break
    else:
        print("\n수정할 체품코드 %s가 없습니다!!\n" % code)


def delete_proc():
    code = input("삭제할 제품코드를 입력하세요 : ")
    for obj in lst:
        if obj.code == code:
            lst.remove(obj)
            print("\n제품코드 %s 제품정보 삭제 성공!!\n" % obj.code)
            break
    else:
        print("\n삭제할 제품코드 %s가 없습니다!!\n" % code)

if __name__ == "__main__":
    lst = []

    while True:
        f_menu()

        menu = int(input("메뉴를 선택하세요 => "))
        print()

        if menu == 1:
            input_proc()
        elif menu == 2:
            output_proc()
        elif menu == 3:
            search_proc()
        elif menu == 4:
            update_proc()
        elif menu == 5:
            delete_proc()
        else:
            print("\n프로그램 종료...")
            break
