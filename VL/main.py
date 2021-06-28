import numpy as np
from variables import (E_p_max, E_k_max, b, n, D)
from VangLandau import (coth)


configuration_matrix = np.loadtxt("matrix.txt")

E_max = float(b/n)*E_p_max + float(n/b)*E_k_max

Z = 0
E_k = 0
E_p = 0
dE_k = 0
dE_p = 0
Result_Energy = 0
Energy = 0
dE_k = 0.4
dE_p = 0.4
Constant_before_integral = (n / (np.pi * b)) ** (n * D / 2)  # сокращается в результате


if __name__ == '__main__':
    for i in range(100):
        for j in range(100):
            E_k = (i + 0.5) * 0.4
            E_p = (j + 0.5) * 0.4
            Z += configuration_matrix[i, j] * np.exp(-n / b * E_k - b / n * E_p) * (dE_k) * (dE_p)
            Energy += configuration_matrix[i, j] * np.exp(-n / b * E_k - b / n * E_p) * (dE_k) * (dE_p) * (
                        -n * D / (2 * b) + n / (b ** 2) * E_k - 1 / n * E_p)

    result = - (1 / Z) * Energy

    Numerical_result = D / 2 * coth(b / 2)

    Error = (Numerical_result - result) / Numerical_result
    print('Результат Монте-Карло: %s' % result)
    print('Результат по формуле: %s' % Numerical_result)
    print('Ошибка расчета %s' % Error)
