from solution import *
from code import P, C, a, A, b

y1, y2 = [], []
alpha_list = np.arange(0.49, 1, 0.01).tolist()
alpha_list.append(1)

task = "pessimist"
for alpha in alpha_list:
    y1.append(solution(P=P, C=C, a=a, A=A, b=b, task=task, alpha=alpha))

task = "optimist"
for alpha in alpha_list:
    y2.append(solution(P=P, C=C, a=a, A=A, b=b, task=task, alpha=alpha))

plt.plot(alpha_list, y1, label = "pessimist")
plt.plot(alpha_list, y2, label = "optimist")


plt.xlabel('alpha')
plt.ylabel('F')
plt.legend()
plt.show()