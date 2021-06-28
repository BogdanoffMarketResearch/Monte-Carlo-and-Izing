import numpy as np
from variables import (D, b, n)


# Кинетическая энергия i-вершины
def E_k(x):
    Sum = 0
    for i in range(n):
        Sum += (x[i][0] - x[i + 1][0]) ** 2 + (x[i][1] - x[i + 1][1]) ** 2 + (x[i][2] - x[i + 1][2]) ** 2
    return Sum


# Потенциальная энергия i-вершины
def E_p(x):
    Sum = 0
    for i in range(n):
        Sum += x[i][0] ** 2 + x[i][1] ** 2 + x[i][2] ** 2
    return Sum


# Полная энергия, где i - выбор температуры из массива
def E(x):
    global b, n
    return float(b / n) * E_p(x) + float(n / b) * E_k(x)


# Эстиметор потенциальной энергии
def estimator_p(x):
    Sum = 0
    for i in range(n):
        Sum += x[i][0] ** 2 + x[i][1] ** 2 + x[i][2] ** 2
    return (float(1) / float(n)) * Sum


# Эстиматор кинетической энергии
def estimator_k(x):
    Sum = 0
    for i in range(n):
        Sum += (x[i][0] - x[i + 1][0]) ** 2 + (x[i][1] - x[i + 1][1]) ** 2 + (x[i][2] - x[i + 1][2]) ** 2
    result = n * D / (2 * b) - float(n) / float(b ** 2) * Sum
    return result


# Далее будет вестить суммирование по каждому шагу МонтеКарло, значиений эстиматора

#Sum_estimators = 0


def Sum_estimator_for_mean_E(x):
    estimator_k(x) + estimator_p(x)


def EquateLists(A, B):
    for i in range(len(A)):
        A[i] = list(B[i])


def Get_index(E):
    """
    Получить индекс для соответствующей ячейки с энергией E
    """
    result = E * 100 // 40
    return int(result)


def coth(b):
    """
    расчет гиперболического котангенса
    """
    result = np.tanh(b)
    return 1 / result
