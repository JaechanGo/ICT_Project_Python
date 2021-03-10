from sungjuk_2_1 import Sungjuk
import pickle

if __name__ == "__main__":
    lst = []
    fp = open("sungjuk.dat", "wb")
    while True:
        obj = Sungjuk()

        if obj.input_sungjuk():
            break

        obj.process_sungjuk()
        lst.append(obj)
        print()

    print("\n                     *** 성적표 ***")
    print("=========================================================")
    print("학번     이름    국어    영어    수학    총점     평균     등급")
    print("=========================================================")
    for obj in lst:
        obj.output_sungjuk()
        pickle.dump(obj, fp)
    print("=========================================================")

    fp.close()