<문제의 해결 방안>
본 프로젝트는 두 개의 모듈 파일과 하나의 메인 파일로 구성된다. 

1. data_processing.py
# data_processing 모듈

## 개요
이 모듈은 수능 데이터 처리 및 분석을 위한 함수들을 제공한다. 
히스토그램과 같은 시각화를 쉽게 구현할 수 있도록 데이터를 필터링하고 준비하는 함수가 포함되어 있다.

## 포함된 함수

(1) **load_data**: CSV 파일을 로드하는 함수.
try-except 구문을 통해 데이터 로드 중 오류가 나도 프로그램이 종료되지 않게끔 하였고, except문에선 모든 예외를 처리하기 위해 최상위예외클래스를 사용했다.

(2) **valid_subjects**: 데이터에서 유효한 과목 리스트를 추출하는 함수.
데이터 프레임에서 '영역' 열의 고유 값을 unique를 통해 추출했다.

(3) **filter_data_by_subject**: 특정 과목 데이터를 필터링하는 함수.
pandas의 boolean indexing으로 특정 (입력받은) 과목의 데이터만 필터링하였다.

(4) **prepare_distribution_data**: 남학생/여학생 점수 분포 데이터를 준비하는 함수.
 필터링된 데이프레임을 파라미터로 받아서 남학생과 여학생의 데이터를 나눠 반환하는 함수다. pandas의 열 선택 기능을 이용해 표준점수 열과 성별 열만을 추출했다.
 
2. ModuleB.py

3. main.py
사용자로부터 그래프를 표시할 과목명을 입력받는다. 
data_processing 모듈의 filter_data_by_subject, prepare_distribution_data 함수를 이용하여 추출한 그 과목의 남녀 데이터를 ModuleB 모듈의 visualize 함수의 매개변수로 입력하여 결과 그래프를 화면에 표시한다.
