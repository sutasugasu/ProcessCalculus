# Сумма sigma_1^128=1/i^2


__author__ = "Glushkov Stanislav"


N=int(input("Введите кол-во элементов суммы"))
x=0
for i in range(1, N+1):
   x+=1/((2*i)**2)
print (f"Сумма {N} членов суммы sigma_1^{N}=1/i^2 = {x:.6f}")