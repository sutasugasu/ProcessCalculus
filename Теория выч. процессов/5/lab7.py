#334б Вычислить:
#sigma_i=1^100(sigma_j=1^60(sin(i^3+j^4)))


___author___ = "Stanislav Glushkov"

import math
import numpy as np

from mymod import  calc

N=int(input("Введите первое число - "))
M=int(input("Введите второе число - "))
result = calc(N,M)  #вызов функции подсчёта суммы

print("Результат выражения - ", result)