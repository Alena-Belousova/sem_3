#     Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#    Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numb= input('введите числа через пробел ')

list=[numb.split(' ')]

list=numb.split(' ')
list=[int (numb) for numb in list]
sum=0
for a,b in enumerate(list):
    if(a%2!=0):
      sum=sum+b 
print(sum)





