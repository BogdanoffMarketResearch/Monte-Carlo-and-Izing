import math
from Fourier import (EquateLists, E, Sum_estimator_for_mean_E, coth)
import random as rn
# Задаем начальные параметры системы
# n, dx = map(int,input().split()) # n - число вершин, dx - сдвижка
# Пока работаем при заданном n и dx
n = 6  # n - число вершин
dx = 0.5  # меньше, чем указано в работе, но иначе энергия растет слишком быстро
N = 1  # N - число частиц
D = 3  # D - размерность пространства
b = 4  # b - обратная температура b = [0.25, 0.5, 1, 2, 4]
E_max = 50  # Максимальная энергия
N_mc = 10**5  # Число шагов Монте-Карло
X = []  # Задаем начальную конфигурацю: положим все значения координат равными нулю
# нам нужно две таблички для решения задачи, эта нужна, чтобы хранить где-то новую конфигурацию
X_new_configuration = []
for i in range(n):  # задали начальную конфигурацию
    X.append([0, 0, 0])
    X_new_configuration.append([0, 0, 0])
# X.append(X[0]) # замкнули: последняя равна нулевой вершине


if __name__ == "__main__":
    Sum_estimators = 0
    for i in range(N_mc):
        E_begin = E(X)
        random_top = rn.randint(0, n - 1)  # выбираем случайную вершину
        for i in range(3):  # производим случайное изменение конфигурации
            Delta_x = (rn.random() - 0.5) * dx
            X_new_configuration[random_top][i] += Delta_x
        # if random_top==0:
        #    X_new_configuration[n] = X_new_configuration[random_top]
        E_before = E(X_new_configuration)
        # print(E_begin, E_before)
        if E_before > E_max:
            EquateLists(X_new_configuration, X)
            # Sum_estimators += estimator_k(X_new_configuration,0) + estimator_p(X_new_configuration)
            Sum_estimators += Sum_estimator_for_mean_E(X_new_configuration)
            # print("зашли в Е>E_max")
            continue
        delta_E = E_before - E_begin
        if delta_E > 0:
            W = math.exp(-delta_E)  # вычисляем вероятность перехода
            if W >= rn.random():  # переходим или нет в новую конфигурацию
                EquateLists(X, X_new_configuration)
                # Sum_estimators += estimator_k(X,0) + estimator_p(X)
                Sum_estimators += Sum_estimator_for_mean_E(X)
            # print("зашли в if W>rn.random")
            else:
                EquateLists(X_new_configuration, X)
                # Sum_estimators += estimator_k(X,0) + estimator_p(X)
                Sum_estimators += Sum_estimator_for_mean_E(X)
            # print("зашли в else W>rn.random")
        else:
            EquateLists(X, X_new_configuration)
            # Sum_estimators += estimator_k(X,0) + estimator_p(X)
            Sum_estimators += Sum_estimator_for_mean_E(X)
            # print("зашли в else delta_E>0")

    result = Sum_estimators / N_mc

    Numerical_result = D / 2 * coth(b / 2)

    Error = (Numerical_result - result) / Numerical_result
    print('Результат Монте-Карло: %s' % result)
    print('Результат по формуле: %s' % Numerical_result)
    print('Ошибка расчета %s' % Error)
