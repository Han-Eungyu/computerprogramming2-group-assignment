# main.py

import csv
import data_processing as dp
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

filtered_data = dp.filter_data_by_subject(data, input_subject)

# 남학생과 여학생의 점수 분포 데이터 준비
male_data, female_data = dp.prepare_distribution_data(filtered_data)

# 분포 그래프 시각화
mb.visualize(male_data, female_data, input_subject)
