# main.py

import csv
import data_processing as dp
import ModuleB as mb

while True:
    year = input("연도를 입력하세요 (2020 ~ 2023): ")
    if year in ["2020", "2021", "2022", "2023"]:
        break
    else:
        print("잘못된 입력입니다.")

file_paths = {
    "2020": "20201231.csv",
    "2021": "20211231.csv",
    "2022": "20221231.csv",
    "2023": "20231231.csv"
}
file_path = file_paths[year]

file_encoding = "EUC-KR"

data = dp.load_data(file_path, file_encoding)
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
print(f"{input_subject} 과목의 Violin Plot입니다.")

filtered_data = dp.filter_data_by_subject(data, input_subject)

# 남학생과 여학생의 점수 분포 데이터 준비
male_data, female_data = dp.prepare_distribution_data(filtered_data)

# 분포 그래프 시각화
mb.visualize_violin(male_data, female_data, input_subject, year)
