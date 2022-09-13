
    #Напишите программу, 
   # которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

numb= input('введите числа через пробел ')
list=[]
list=numb.split(' ')
list=[int (numb) for numb in list]
sum=0
index_max= len(list)-1
list_1= []
for i,chislo in enumerate(list):
   if(i<len(list)/2):

       sum=list[i]*list[index_max]
       index_max=index_max-1
      
       list_1.append(sum)
print(list_1)


 






