

   # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

   # Пример:

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

size= input('введите число ')
size= int(size)
list=[]
f1=0
f2=1
for i in range(size-1):
       f3=f1-f2
       list.append(f3)
       f1=f2
       f2=f3
list.reverse()
f1=0
f2=1
list.append(0)
list.append(1)
for i in range(size-1):
       f3=f1+f2
       list.append(f3)
       f1=f2
       f2=f3
print (list)
    












