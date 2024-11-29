# main.py

import csv
import data_proccessing as dp

subjects = dp.valid_subjects()
for i in subjects:
    print(i)

while True:
    input_subject = input("과목 이름을 입력하세요 >> ")
    if input_subject not in subjects:
        print("잘못된 과목 이름입니다.")
    else:
        break
print(f"{input_subject} 과목의 도수분포그래프입니다.")
