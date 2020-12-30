from solution import *


P=np.array(
    [
        [45, 25, 35, 20],
        [30, 20, 20, 25],
        [8, 16, 20, 24],
        [32, 16, 14, 12]
    ]
)
C=np.array(
    [
        [10, 8, 10, 12],
        [20, 7, 12, 10],
        [3, 5, 8, 10],
        [10, 8, 10, 5]
    ]
)
a=np.array(
    [
        [25, 20, 50, 50],
        [20, 12, 15, 45], 
        [15, 10, 20, 40],
        [10, 40, 10, 25]
    ]
)
A=[500, 200, 100, 1000]
b=[50, 80, 30, 45]
task="pessimist"
alpha = 1

if __name__ == "__main__":
    solution(P=P, C=C, a=a, A=A, b=b, task=task, alpha=alpha)
