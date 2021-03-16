from sungjuk_2_1 import Sungjuk
import sqlite3

def create_table():
    dbconn = sqlite3.connect('sungjuk.db')

    dbcursor = dbconn.cursor()
    dbcursor.execute("""create table if not exists sungjuk(
            hakbun text primary key,
            irum text,
            kor integer,
            eng integer,
            math integer,
            tot integer,
            avg real,
            grade text)""")

    dbcursor.close()
    dbconn.close()

def f_menu():
    print("***메뉴***")
    print(" 1. 성적정보입력")
    print(" 2. 성적정보 출력")
    print(" 3. 성적정보 조회")
    print(" 4. 성적정보 수정")
    print(" 5. 성적정보 삭제")
    print(" 6. 성적정보 종료")


def f_input():
    obj = Sungjuk()

    print()
    obj.input_sungjuk()
    obj.process_sungjuk()

    sql = "insert into sungjuk (hakbun, irum, kor, eng, math, tot, avg, grade) values (?, ?, ?, ?, ?, ?, ?, ?)"


    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()
    dbcursor.execute(sql, (obj.hakbun, obj.irum, obj.kor, obj.kor, obj.eng, obj.math, obj.tot, obj.avg, obj.grade))
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

    print("성적 정보 입력 성공");

def f_output():
    total_avg =0

    dbconn=sqlite3.connec('sungjuk.db')
    dbcursor = dbconn.cursor()

    dbcursor.excute("SELECT count(*) FROM sungjuk")
    cnt = dbcursor.fetchone()[0] # fetchone(): 한개의 레코드(튜플)
    if cnt==0:
        print("\t데이터 미존재\t")
        return

    res = dbcursor.excute("SELECT * FROM sungjuk order by hakbun asc")

    print("\n             *성적표")
    print("======")
    print("학번 이름 국어 영어 수학 총점 평균 등급")
    print("===")
    for row in res:
        total_avg += row[6]
        print("%4s %4s %3d %3d %3d %3d %6.2f %s"
              % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    print("===")
    print(" 총학생수 = %d , 전체평균 = %.2f \n"% (cnt, total_avg / cnt))

    dbcursor.close()
    dbconn.close()

def f_update():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    res = dbcursor.excute("SELECT * FROM sungjuk order by hakbun asc")

    hakbun = input("\n 수정할 학번을 입력하세요 : ")
    for row in res:
        if (row[0] == hakbun):
            obj = Sungjuk()
            obj.hakbun = row[0]
            obj.kor = int(input("국어 점수 : "))
            obj.eng = int(input("영어 점수 : "))
            obj.math = int(input("수학 점수 : "))
            obj.process_sungjuk()

            dbcursor.execute("update sungjuk set kor=?, eng=?, math=?, tot=?, avg=?, grade=? where hakbun=?",
                             (obj.kor, obj.eng, obj.math, obj.tot, obj.avg, obj.grade, obj.hakbun))
            print("\n학번 %s 성적정보 수정 성공 !!!!\n" % obj.hakbun)
            break
    else:
        print("\n 수정할 제품코드 $s가 없습니다. \n" % hakbun)

    dbconn.commit()
    dbcursor.close()
    dbconn.close()

def f_delete():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()
    """
    res = dbcursor.excute("SELECT * FROM sungjuk order by hakbun asc")

    hakbun = input("\n삭제할 학번을 입력하세요 : ")

    for row in res:
        if(row[0]==hakbun):
            dbcursor.execute("delete from sungjuk where hakbun=?",(hakbun))
            print("학번  %s 성적정보 삭제 성공\n"%hakbun)
            break
    else:
        print("삭제할 학번 %s 이 없습니다."% hakbun)
    """
    hakbun = input("\n삭제할 학번을 입력하세요 : ")
    dbcursor.execute("delete from sungjuk where hakbun=?",(hakbun))

    if(dbcursor.fetchone()[0]==hakbun):
        dbcursor.execute("delete from sungjuk where hakbun=?",(hakbun))
        print("학번  %s 성적정보 삭제 성공\n" % hakbun)
    else:
        print("삭제할 학번 %s 이 없습니다."% hakbun)

if __name__=="__main__":
    students = []

    create_table()
    while True:
        f_menu()

        menu = int(input("메뉴를 선택하세요 => "))
        print()

        if menu == 1:
            f_input()
        elif menu == 2:
            f_input()
        elif menu == 3:
            f_input()
        elif menu == 4:
            f_input()
        elif menu == 5:
            f_input()
        else:
            print("\n프로그램 종료...")
            break