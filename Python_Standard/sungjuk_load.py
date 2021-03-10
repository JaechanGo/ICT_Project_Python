import pickle
import os

if __name__ == "__main__":
    fp = open("sungjuk.dat", "rb")
    lst = []

    while True:
        obj = pickle.load(fp)
        lst.append(obj)
        if (fp.tell() == os.fstat(fp.fileno()).st_size):
            break;

    print("\n                     *** 성적표 ***")
    print("=========================================================")
    print("학번     이름    국어    영어    수학    총점     평균     등급")
    print("=========================================================")
    for obj in lst:
        obj.output_sungjuk()
    print("=========================================================")
    fp.close()