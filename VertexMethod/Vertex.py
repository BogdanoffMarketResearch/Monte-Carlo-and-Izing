import numpy as np

n = 5  # n - число вершин
dx = 0.5  # dx - сдвижка, меньше, чем указано в работе, но иначе энергия растет слишком быстро
N = 1  # N - число частиц
D = 3  # D - размерность пространства
b = [0.25, 0.5, 1, 2, 4]  # b - обратная температура
E_max = 50  # Максимальная энергия
N_mc = 10**5  # Число шагов Монте-Карло
X = []  # Задаем начальную конфигурацю: положим все значения координат равными нулю
# Нам нужно две таблички для решения задачи, эта нужна, чтобы хранить где-то новую конфигурацию
X_new_configuration = []
for i in range(n):  # задали начальную конфигурацию
    X.append([0, 0, 0])
    X_new_configuration.append([0, 0, 0])
X.append(X[0])  # замкнули: последняя равна нулевой вершине
X_new_configuration.append(X_new_configuration[0])


def E_k(x):
    """
    Calculation of kinetic energy
    :param x: Current configuration
    :return: Kinetic energy of this configuration
    """
    Sum = 0
    for i in range(n):
        Sum += (x[i][0]-x[i+1][0])**2 + (x[i][1]-x[i+1][1])**2 + (x[i][2]-x[i+1][2])**2
    return Sum


def E_p(x):
    """
    Calculation of potential energy
    :param x: Current configuration
    :return: Potential energy of this configuration
    """
    Sum = 0
    for i in range(n):
        Sum += x[i][0]**2 + x[i][1]**2 + x[i][2]**2
    return Sum


def E(x, i):
    """
    Calculation of full energy
    :param x: Current configuration
    :param i: Temperature from a given array: b
    :return: Full energy of this configuration
    """
    global b, n
    return float(n/b[i])*E_k(x) + float(b[i]/n)*E_p(x)


def estimator_p(x):
    """
    Estimator of kinetic energy
    :param x: Current configuration
    :return: Estimator of kinetic energy of this configuration
    """
    Sum = 0
    for i in range(n):
        Sum += x[i][0]**2 + x[i][1]**2 + x[i][2]**2
    return (1/n)*Sum


def estimator_k(x, i):
    """
    Estimator of potential energy
    :param x: Current configuration
    :return: Estimator of potential energy of this configuration
    """
    Sum = 0
    for i in range(n):
        Sum += (x[i][0]-x[i+1][0])**2 + (x[i][1]-x[i+1][1])**2 + (x[i][2]-x[i+1][2])**2
    result = n*D/(2*b[i]) - n/(b[i]**2)*Sum
    return result


def Sum_estimator_for_mean_E(x,i):
    """
    Calculate sum of kinetic and potential estimators
    :param x: Current configuration
    :param i: Temperature from a given array: b
    :return: Sum of kinetic and potential estimators
    """
    result = estimator_k(x,i) + estimator_p(x)
    return result


def coth(b):
    """
    Calculation of hyperbolic cotangent
    :param b: Temperature from a given array: b
    :return: Hyperbolic cotangent
    """
    result = np.tanh(b)
    return 1/result


def EquateLists(A,B):
    """
    Приравнивает списки: A=B
    """
    for i in range(len(A)):
        A[i] = list(B[i])