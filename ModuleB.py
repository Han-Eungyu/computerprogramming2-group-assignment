import matplotlib.pyplot as plt
import pandas as pd

def visualize(d1,d2,subject):
    plt.figure(figsize=(11,7))
    plt.bar(d1.iloc[:,0], d1.iloc[:,1], width=1.0, label="남성", alpha=0.5,color="skyblue") 
    plt.bar(d2.iloc[:,0], d2.iloc[:,1], width=1.0, label="여성", alpha=0.5,color="pink") 

    plt.xlabel("표준점수")
    plt.ylabel("학생 수")
    plt.title(f"2024 수능 {subject} 과목 학생 성별 별 점수 분포",size=18)
    plt.legend()
    plt.grid(axis='y')
    plt.rcParams['font.family'] = 'NanumGothic'


    plt.show()




