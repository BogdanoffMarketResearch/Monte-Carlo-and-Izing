import numpy as np
from variables import (E_p_max, E_k_max, b, n, istimator_S, dx)
from VangLandau import (Get_index, E_k, E_p, EquateLists, E)
import random as rn
import math


configuration_matrix = np.zeros((100,100))
X = [] # Задаем начальную конфигурацю: положим все значения координат равными нулю
X_new_configuration = [] # нам нужно две таблички для решения задачи, эта нужна, чтобы хранить где-то новую конфигурацию
for i in range(n): # задали начальную конфигурацию
    X.append([0,0,0])
    X_new_configuration.append([0,0,0])
X.append(X[0])
X_new_configuration.append(X_new_configuration[0])


if __name__ == '__main__':
    count = 0
    for i in range(80):
        istimator_S *= 0.95
        for i in range(500000):
            E_begin = E(X)
            k, j = Get_index(E_k(X)), Get_index(E_p(X))
            random_top = rn.randint(0, n - 1)  # выбираем случайную вершину
            for i in range(3):  # производим случайное изменение конфигурации
                Delta_x = (rn.random() - 0.5) * dx
                X_new_configuration[random_top][i] += Delta_x
                if (Get_index(E_k(X_new_configuration)) >= 100) or (Get_index(E_p(X_new_configuration)) >= 100):
                    EquateLists(X_new_configuration, X)
                    configuration_matrix[k, j] += istimator_S
                    continue
                k_new, j_new = Get_index(E_k(X_new_configuration)), Get_index(E_p(X_new_configuration))
            if random_top == 0:
                X_new_configuration[n] = X_new_configuration[random_top]
                E_before = E(X_new_configuration)
            if (E_k(X_new_configuration) >= E_k_max) or (E_p(X_new_configuration) >= E_p_max):
                EquateLists(X_new_configuration, X)
                configuration_matrix[k, j] += istimator_S
                continue
            delta_S = configuration_matrix[k_new][j_new] - configuration_matrix[k][j]
            if delta_S > 0:
                W = math.exp(-delta_S)  # вычисляем вероятность перехода
                if W >= rn.random():  # переходим или нет в новую конфигурацию
                    EquateLists(X, X_new_configuration)
                    configuration_matrix[k_new, j_new] += istimator_S
                else:
                    EquateLists(X_new_configuration, X)
                    configuration_matrix[k, j] += istimator_S
            else:
                EquateLists(X, X_new_configuration)
                configuration_matrix[k_new, j_new] += istimator_S
            count += 1

    np.savetxt("matrix.txt", configuration_matrix)