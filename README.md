# <문제의 해결 방안>
본 프로젝트는 두 개의 모듈 파일과 하나의 메인 파일로 구성된다. 

## 1. data_processing 모듈

### 개요
이 모듈은 수능 데이터 처리 및 분석을 위한 함수들을 제공한다. 
히스토그램과 같은 시각화를 쉽게 구현할 수 있도록 데이터를 필터링하고 준비하는 함수가 포함되어 있다.

### 포함된 함수

(1) **load_data**: CSV 파일을 로드하는 함수.
try-except 구문을 통해 데이터 로드 중 오류가 나도 프로그램이 종료되지 않게끔 하였고, except문에선 모든 예외를 처리하기 위해 최상위예외클래스를 사용했다.

(2) **valid_subjects**: 데이터에서 유효한 과목 리스트를 추출하는 함수.
데이터 프레임에서 '영역' 열의 고유 값을 unique를 통해 추출했다.

(3) **filter_data_by_subject**: 특정 과목 데이터를 필터링하는 함수.
pandas의 boolean indexing으로 특정 (입력받은) 과목의 데이터만 필터링하였다.

(4) **prepare_distribution_data**: 남학생/여학생 점수 분포 데이터를 준비하는 함수.
 필터링된 데이프레임을 파라미터로 받아서 남학생과 여학생의 데이터를 나눠 반환하는 함수다. pandas의 열 선택 기능을 이용해 표준점수 열과 성별 열만을 추출했다.

## 2-1. ModuleB 모듈

### 개요
해당 모듈은 데이터 시각화 작업을 수행하는 함수를 제공한다. 

### 포함된 함수

(1) **visualize**: 데이터를 시각화하는 함수.

Pandas Dataframe 형식의 데이터 두 개 (d1,d2), 문자열 형식의 데이터 하나(subject) 총 세 개의 parameter를 갖는다. 

matplotlib 내의 bar 함수를 사용해 막대그래프를 그린다. 

rcParams를 이용해 폰트를 사용자의 OS 기본 폰트에 해당하도록 설정한다. 

color="skyblue"의 남학생 막대그래프 (by d1) , color="pink"의 여학생 막대그래프 (by d2) 를 plt.bar( ) 를 이용해 시각화한다. 

plt.xlabel( ),plt.ylabel( ) 을 이용해 x축과 y축 라벨을 지정한다. 

plt.label( )을 이용해 그래프의 제목 및 크기를 지정한다. 

plt.legend( )를 이용해 범례를 표시한다. 

plt.grid( )를 이용해 y축의 격자선을 표시한다. 

plt.show( )를 이용해 그래프를 출력한다.

## 2-2. ModuleB_ver2 모듈

### 개요
해당 모듈은 데이터 시각화 작업을 수행하는 함수를 제공한다. 

### 포함된 함수

(1) **visualize**: 데이터를 시각화하는 함수.

Pandas Dataframe 형식의 데이터 두 개 (d1,d2), 문자열 형식의 데이터 두 개(subject, year) 총 네 개의 parameter를 갖는다. 

matplotlib 내의 violinplot 함수를 사용해 violin plot을 그린다. 

rcParams를 이용해 폰트를 사용자의 OS 기본 폰트에 해당하도록 설정한다. 

반복문을 이용해 각각의 violin plot의 색상을 지정한다. 

여학생과 남학생 점수의 평균을 hlines( )를 이용해 표시한다. 

plt.xlabel( ),plt.ylabel( ) 을 이용해 x축과 y축 라벨을 지정한다. 

plt.label( )을 이용해 그래프의 제목 및 크기를 지정한다. 

plt.legend( )를 이용해 범례를 표시한다. 

plt.grid( )를 이용해 y축의 격자선을 표시한다. 

plt.show( )를 이용해 그래프를 출력한다.


## 3. main.py
사용자로부터 그래프를 표시할 연도와 과목명을 차례로 입력 받는다.

**data_processing** 모듈의 **filter_data_by_subject, prepare_distribution_data** 함수를 이용하여 추출한 그 과목의 남녀 데이터를 **ModuleB** 모듈 **visualize** 함수의 매개변수로 입력하여 결과 그래프를 화면에 표시한다.



