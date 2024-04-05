___author___ = "Stanislav Glushkov"


import numpy as np

import math
from random import uniform


def rec_arr(N):
    '''Функция записи элементов в массив'''
    arr = [] * N #Создание массива с N-ым кол-вом элементов
    for i in range(1, N+1):
        a = float(input(f"Введите {i}-е число = "))
        arr.append(a)
    return arr

def sum_arr(arr):
    '''Функция подсчета суммы массива'''
    sum = 0
    for i in range(0, len(arr)):
        sum += math.sqrt(10+arr[i]**2)
    return sum

def find_sqrinarr(arr):
    '''Функция подсчёта элементов массива, являющимися квадратами четных чисел'''
    k=0
    for i in range(0, len(arr)):
        if math.sqrt(arr[i])%2==0:
            k+=1
    return k
            

def calc(N,M):
    '''Функция подсчёта суммы'''
    sum = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            sum+= math.sin(pow(i,3) + pow(j,4))
    return sum


def add_col(arr, new_col):
    '''Функция добавления столбца в исходную матрицу между 5 и 6-м столбцом'''
    return np.insert(arr, 5, new_col, axis=1)       #Добавляет столбец в массив 
    






