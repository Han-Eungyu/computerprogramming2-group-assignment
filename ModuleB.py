import matplotlib.pyplot as plt

def visualize(d1,d2,subject):
    plt.figure(figsize=(11,7))
    plt.hist(d1.iloc[0],bins=d1.iloc[0],label="남학생",alpha=0.5,edgecolor="blue")
    plt.hist(d2.iloc[0],bins=d2.iloc[0],label="여학생",alpha=0.5,edgecolor="pink")
    plt.xlabel("표준점수")
    plt.ylabel("학생 수")
    plt.title(f"2024 수능 {subject} 과목 학생 성별 별 점수 분포()",size=18)
    plt.legend()
    plt.grid(axis='y')

    plt.show()




