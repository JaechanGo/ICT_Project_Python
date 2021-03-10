import os
import pickle

def f_output():
    total_avg =0
    cnt = 0
    if(not os.path.isfile("sungjuk.dat")):
        print("\n출력할 데이터가 없습니다.")
        return

    fp = open("sungjuk.dat","rb")

    if os.fstat(fp.fileno()).st_size ==0:
        print("\n출력할 데이터가 없습니다.")
        return

    print("\n\t\t        *** 성적표 ***")
    print("================================================")
    print("학번   이름   국어   영어   수학   총점   평균   등급")
    print("================================================")

    while True:
        obj = pickle.load(fp)
        total_avg+=obj.avg
        obj.output_sungjuk()
        cnt += 1
        if(fp.tell()==os.fstat(fp.fileno()).st_size):
            break;

        fp.close()
        print("================================================")
        print("===========총학생수 = %d, 전체 평균 = %.2f\n"%(cnt,total_avg/cnt))