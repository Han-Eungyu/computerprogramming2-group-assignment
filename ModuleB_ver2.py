import matplotlib.pyplot as plt
import pandas as pd

def visualize_violin(d1, d2, subject):
    plt.rcParams["font.family"] = "AppleGothic"
    plt.rcParams["axes.unicode_minus"] = False
    plt.figure(figsize=(11, 7))

    data = [d1.iloc[:, 1], d2.iloc[:, 1]] 
    labels = ['남성', '여성']
    
    plt.violinplot(data, showmeans=True, showextrema=True, widths=0.7)
    
    plt.xticks([1, 2], labels) 
    plt.xlabel("성별")
    plt.ylabel("표준점수")
    plt.title(f"2024 수능 {subject} 과목 학생 성별 별 점수 분포 (Violin Plot)", size=18)
    
    plt.grid(axis='y')
    plt.show()





