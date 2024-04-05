#675 Даны действительные числа a1,...,an действительная квадратная матрица порядка n (n ≥ 6). 
#Получить действительную матрицу размера n x (n+1),
#вставив в исходную матрицу между пятым и шестым столбцами новый столбец с элементами a1,...,an .


___author___ = "Stanislav Glushkov"

import math
import numpy as np

from mymod import rec_arr, add_col


i = int(input("Введите количество строк - "))
j = int(input("Введите количество столбцов - "))
rand = int(input("Введите максимальное рандомное число для массива - "))
vect = rec_arr(i)
array = np.random.randint(rand, size=(i, j)) #создание рандомного массива
result = add_col(array, vect)
print(array)
print("-------------------------------------------------------")
print(result)
