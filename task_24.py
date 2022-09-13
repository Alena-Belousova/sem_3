  

    #Задайте список из вещественных чисел. 
    #Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
  # Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


numb= input('введите числа через пробел ')
list=[]
list_1= []
list=numb.split(' ')
list=[float (numb) for numb in list]
i=0
for i in list:
    ostatok=i-int(i)
    
    list_1.append(ostatok)

print(list_1)
max=max(list_1)
min=min(list_1)
print(max)
print(min)
razn=max-min
print(razn)

 






