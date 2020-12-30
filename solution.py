import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt


def solution(P, C, a, A, b, task, alpha):
    temp = pow((1 / alpha - 1) / 2, 0.5)
    if task == "optimist":
        a = a + a * temp
        C = C - C * temp
    elif task == "pessimist":
        a = a - a * temp
        C = C + C * temp
    else:
        print("Uncorrect task. This field requires value 'optimist' or 'pessimist'")
        return 1
    a *= -1
    a = a.tolist()
    for i in range(len(a)):
        a[i] = (
            list(np.zeros(len(a[i]) * i))
            + a[i]
            + list(np.zeros(len(a[i]) * (len(a) - 1 - i)))
        )
    b1 = [1 if i%4 == 0 else 0 for i in range(16)]
    b2 = [1 if (i-1)%4 == 0 else 0 for i in range(16)]
    b3 = [1 if (i-2)%4 == 0 else 0 for i in range(16)]
    b4 = [1 if (i-3)%4 == 0 else 0 for i in range(16)]
    b_koefs = [b1, b2, b3, b4]

    target = [(C - P)[k][j] for k in range(len(P)) for j in range(len(P[0]))]
    A[:] = [-i for i in A]
    constraint_matrix = a + b_koefs
    constraint_vector = A + b

    func = "F = "
    for i in range(16):
        func += str(target[i]) + "*x" + str(i+1) + " "
    print(func)
    c = 0
    for i in constraint_matrix:
        limit = ""
        for x in range(16):
            limit += str(i[x]) + "*x" + str(x+1) + " "
        print(limit + " <= " + str(constraint_vector[c]))
        c += 1

    res = linprog(target, A_ub=constraint_matrix, b_ub=constraint_vector, method="simplex")

    print(res.message, "\n")
    print("Result: " + str(-1*round(res.fun, 2)), "\n")
    for i in range(16):
        print("X" + str(i+1) + " = " + str(res.x[i]))

    return -1*round(res.fun, 2)
