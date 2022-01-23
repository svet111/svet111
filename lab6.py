#Проверить, что в одномерном массиве нет элементов, попадающих в заданный диапазон. Если такой элемент есть, найти его номер.
import sys
import os.path
if len(sys.argv) != 3:
    print('Недостаточно параметров')
else:
    if not os.path.exists(sys.argv[1]):
        print('Файл не существует')
    else:
        f=open(sys.argv[1], 'r')
        number1=int(f.readline())
        number2 = int(f.readline())
        array_A=list(map(int, f.readline().split()))
        f.close()
        element_was_found = False
        found_index = None
        index=0
        while index<len(array_A) and not element_was_found:
            if array_A[index] > number1 and array_A[index] < number2:
                found_index = index
                element_was_found = True
            index+=1
        f = open(sys.argv[2], 'w')
        if element_was_found:
            f.write("Номер элемента, попадающего в заданный диапазон = " + str(found_index + 1) + ".")
        else:
            f.write("Нет элементов, попадающих в заданный диапазон.")
        f.close()