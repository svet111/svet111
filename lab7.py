#Задан целочисленный одномерный массив a из n элементов. Найти номер последнего максимального элемента среди чётных
# элементов и расположенных после первого нечётного элемента, значение которого к тому же лежит в диапазоне [c, d].
# Если нет нечётных элементов со значением из диапазона, искать с начала массива.
import sys
import os.path
if len(sys.argv) != 3:
    print('Недостаточно параметров')
else:
    if not os.path.exists(sys.argv[1]):
        print('Файл не существует')
    else:
        f = open(sys.argv[1],'r')
        c_number = int(f.readline())
        d_number = int(f.readline())
        array_A = list(map(int, f.readline().split()))
        f.close()

        output_file = open(sys.argv[2], "a")

        start_position = 0
        flag = False
        while not flag:
            for index in range(len(array_A)):
                if array_A[index] % 2 == 1 and c_number <= array_A[index] and array_A[index] <= d_number:
                    start_position = index + 1
                    flag = True

        maximum_among_even = float('-inf')
        maximum_even_position = None
        max_even_was_found = False

        for index in range(start_position, len(array_A)):
            if array_A[index] % 2 == 0 and array_A[index] >= maximum_among_even:
                maximum_among_even = array_A[index]
                maximum_even_position = index
                max_even_was_found = True

        if max_even_was_found:
            output_file.write(
                "Номер последнего максимального четного элемента = " + str(maximum_even_position + 1) + ".")
        else:
            output_file.write("Подходящего элемента не найдено.")

        output_file.close()





