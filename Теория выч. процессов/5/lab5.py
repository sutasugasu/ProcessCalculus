# 136o Даны натуральное число n, действительные числа a1,..., an. Вычислить:
# sqrt(10+a_1^2)+...+sqrt(10+a_n^2)

___author___ = "Stanislav Glushkov"

import math
import numpy as np

from mymod import rec_arr, sum_arr

N=int(input("Введите кол-во элементов - "))
arr = rec_arr(N)        #вызов функции и запись элементов массива
sum = sum_arr(arr)      #вызов и суммирование всех элементов массива

print("Результат выражения - ", sum)