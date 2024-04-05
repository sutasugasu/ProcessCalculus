#178в Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:
#в) являющихся квадратами четных чисел;

___author___ = "Stanislav Glushkov"

import math
import numpy as np

from mymod import rec_arr, find_sqrinarr

N=int(input("Введите кол-во элементов - "))
arr = rec_arr(N)        #вызов функции и запись элементов массива
count = find_sqrinarr(arr)   #вызов функции и поиск элементов массива

print("Результат выражения - ", count)