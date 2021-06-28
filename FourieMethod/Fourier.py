import numpy as np


n = 6  # n - число вершин
dx = 0.5  # меньше, чем указано в работе, но иначе энергия растет слишком быстро
N = 1  # N - число частиц
D = 3  # D - размерность пространства
b = 4  # b - обратная температура b = [0.25, 0.5, 1, 2, 4]
E_max = 50  # Максимальная энергия
N_mc = 10**5


def E(x):  # x[i][?]!
    """
    Полная энергия
    """
    global b, n
    Sum1 = 0
    Sum2 = 0
    Sum3 = 0
    result = 0
    for i in range(1, n, 1):
        Sum1 += i**2 * np.dot(x[i], x[i])
        Sum2 += np.dot(x[i], x[i])
    Sum3 = np.array(x[1]) + np.array(x[3])/3 + np.array(x[5])/5
    Sum1 = (np.pi**2) / (2*b) * Sum1
    Sum2 = b/2 * Sum2
    Sum3 = 4 / np.pi*b*np.dot(x[0], Sum3)
    result = (Sum1 + Sum2 + Sum3 + b*np.dot(x[0], x[0]))
    return result

def estimator_p(x):
    """
    Эстиматор потенциальной энергии
    """
    global b, n
    Sum1 = 0
    Sum2 = 0
    for i in range(1, n, 1):
        Sum1 += x[i][0]**2 + x[i][1]**2 + x[i][2]**2
    Sum2 = np.array(x[1]) + np.array(x[3])/3 + np.array(x[5])/5
    return np.dot(x[0], x[0]) + 1/2 * Sum1 + 4/(np.pi)*np.dot(x[0], Sum2)


def estimator_k(x):
    global b, n, D
    """
    Эстиматор кинетической энергии
    """
    global b,n
    Sum = 0
    for i in range(1, n, 1):
        Sum += i**2 * np.dot(x[i], x[i])
    result = n*D/(2*b) - (np.pi**2)/(2 * b**2)*Sum
    return result

# Далее будет вестить суммирование по каждому шагу МонтеКарло, значений эстиматора
def Sum_estimator_for_mean_E(x):
    """
    Подсчет суммы для нахождения среднего по конфигурациям
    """
    result = estimator_k(x) + estimator_p(x)
    return result

def coth(b):
    """
    Расчет гиперболического котангенса
    """
    result = np.tanh(b)
    return 1/result


def EquateLists(A, B):
    """
    Приравнивает списки: A=B
    """
    for i in range(len(A)):
        A[i] = list(B[i])
