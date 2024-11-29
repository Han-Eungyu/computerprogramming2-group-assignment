import pandas as pd

def load_data(file_path, encoding="EUC-KR"):
    """데이터를 로드하는 함수"""
    try:
        data = pd.read_csv(file_path, encoding=encoding)
        return data
    except Exception as e:
        print(f"데이터 로드 중 오류: {e}")
        return None

def filter_data_by_subject(data, subject):
    """특정 과목 데이터만 필터링하는 함수"""
    return data[data["영역"] == subject]

def prepare_distribution_data(filtered_data):
    """남학생과 여학생의 점수 분포 데이터를 준비하는 함수"""
    male_data = filtered_data[["표준점수", "남자"]]
    female_data = filtered_data[["표준점수", "여자"]]
    
    male_scores = male_data["표준점수"]
    male_frequencies = male_data["남자"]
    female_scores = female_data["표준점수"]
    female_frequencies = female_data["여자"]
    
    return male_scores, male_frequencies, female_scores, female_frequencies
