# main.py

import csv
import data_proccessing as dp
import ModuleB as mb

file_path = "20231231.csv"
file_encoding = "EUC-KR"
if data is None:
    print("데이터를 로드하지 못했습니다. 프로그램을 종료합니다.")
    exit()
    
subjects = dp.valid_subjects(data)
for i in subjects:
    print(i)

while True:
    input_subject = input("과목 이름을 입력하세요 >> ")
    if input_subject not in subjects:
        print("잘못된 과목 이름입니다.")
    else:
        break
print(f"{input_subject} 과목의 도수분포그래프입니다.")
