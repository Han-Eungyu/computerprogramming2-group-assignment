import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visualize(d1, d2, subject, year):
    plt.rcParams["font.family"] = "Malgun Gothic"
    plt.rcParams["axes.unicode_minus"] = False
    plt.figure(figsize=(11, 11))

    
    male_scores = np.repeat(d1.iloc[:, 0], d1.iloc[:, 1]) 
    female_scores = np.repeat(d2.iloc[:, 0], d2.iloc[:, 1]) 
    data = [male_scores, female_scores]  

    violin = plt.violinplot(data, showmeans=True, showextrema=True, widths=0.7)

    colors = ["skyblue", "pink"]
    for i, pc in enumerate(violin['bodies']):
        pc.set_facecolor(colors[i])  

    male_avg = male_scores.mean()
    female_avg = female_scores.mean()

    plt.hlines(male_avg, 0.9, 1.1, color="blue", linestyle="--", linewidth=1.5, label=f"남학생 표준점수 평균={male_avg:.1f}")
    plt.hlines(female_avg, 1.9, 2.1, color="red", linestyle="--", linewidth=1.5, label=f"여학생 표준점수 평균={female_avg:.1f}")

    plt.xticks([1, 2], ["남학생", "여학생"]) 
    plt.xlabel("성별")
    plt.ylabel("표준점수")
    plt.title(f"{year} 수능 {subject} 과목 학생 성별 별 점수 분포", size=18)
    plt.legend()
    plt.grid(axis="y")

    plt.show()





