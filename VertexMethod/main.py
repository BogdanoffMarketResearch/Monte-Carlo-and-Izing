import math
import random as rn
import Vertex as func
from Vertex import (EquateLists, E, Sum_estimator_for_mean_E, coth)


# Задаем начальные параметры системы
# n, dx = map(int,input().split())
# Пока работаем при заданном n и dx
n = 5  # n - число вершин
dx = 0.5  # dx - сдвижка, меньше, чем указано в работе, но иначе энергия растет слишком быстро
N = 1  # N - число частиц
D = 3  # D - размерность пространства
b = [0.25, 0.5, 1, 2, 4]  # b - обратная температура
E_max = 50  # Максимальная энергия
N_mc = 10**6  # Число шагов Монте-Карло
X = []  # Задаем начальную конфигурацю: положим все значения координат равными нулю
# Нам нужно две таблички для решения задачи, эта нужна, чтобы хранить где-то новую конфигурацию
X_new_configuration = []
for i in range(n):  # задали начальную конфигурацию
    X.append([0, 0, 0])
    X_new_configuration.append([0, 0, 0])
X.append(X[0])  # замкнули: последняя равна нулевой вершине
X_new_configuration.append(X_new_configuration[0])


if __name__ == "__main__":
    Sum_estimators = 0
    for i in range(N_mc):
        E_begin = E(X, 2)
        random_top = rn.randint(0, n - 1)  # выбираем случайную вершину
        for i in range(3):  # производим случайное изменение конфигурации
            Delta_x = (rn.random() - 0.5) * dx
            X_new_configuration[random_top][i] += Delta_x
        if random_top == 0:
            X_new_configuration[n] = X_new_configuration[random_top]
        E_before = E(X_new_configuration, 2)
        if E_before > E_max:
            EquateLists(X_new_configuration, X)
            Sum_estimators += Sum_estimator_for_mean_E(X_new_configuration, 2)
            continue
        delta_E = E_before - E_begin
        if delta_E > 0:
            W = math.exp(-delta_E)  # вычисляем вероятность перехода
            if W >= rn.random():  # переходим или нет в новую конфигурацию
                EquateLists(X, X_new_configuration)
                Sum_estimators += Sum_estimator_for_mean_E(X, 2)
            else:
                EquateLists(X_new_configuration, X)
                Sum_estimators += Sum_estimator_for_mean_E(X, 2)
        else:
            func.EquateLists(X, X_new_configuration)
            Sum_estimators += Sum_estimator_for_mean_E(X, 2)

    result = Sum_estimators / N_mc

    Numerical_result = D / 2 * coth(b[2] / 2)

    Error = (Numerical_result - result) / Numerical_result
    print('Результат Монте-Карло: %s' % result)
    print('Результат по формуле: %s' % Numerical_result)
    print('Ошибка расчета %s' % Error)
