import numpy as np
from functools import reduce


def matrix_operation(matrices, operation):
    if operation == 'sum':
        return reduce(lambda a, b: a + b, matrices)
    elif operation == 'prod':
        return reduce(lambda a, b: np.dot(a, b), matrices)
    else:
        return reduce(lambda a, b: eval(operation), matrices)


# Przykładowe macierze
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix3 = np.array([[9, 10], [11, 12]])

# Lista macierzy
matrices = [matrix1, matrix2, matrix3]

# Użytkownik wybiera operację
operation = input("Podaj operację (sum, prod lub własna operacja np. 'a * b'): ")

# Wykonanie operacji
result = matrix_operation(matrices, operation)

# Wyświetlenie wyniku
print("Wynikowa macierz:\n", result)