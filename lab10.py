#Даны три прямоугольные матрицы a, b и c разного размера. Сформировать массивы, содержащие элементы матриц, которые
# не равны минимальному значению соответствующей части матрицы. Для матрицы a обрабатывать нижнюю половину,
# для матрицы b – левую половину, для матрицы c – правую половину.
import sys
def get_matrix(result, from_file):
    # rows - количество строк
    # cols - количество столбцов
    rows, cols = map(int, from_file.readline().split())
    for row_index in range(rows):
        result.append(list(map(int, from_file.readline().split())))
    # теперь result содержит считанную матрицу
    # размера rows X cols
def make_answer(result, matrix, min_value):
    for row in matrix:
        for element in row:
            if element != min_value:
                result.append(element)
def end_answer(A, to_file):
    if len(A) % 2 == 1:
        to_file.write("Матрица"+ А + "имеет нечётное кол-во строк\n")
    start_row = len(A) // 2 + len(A) % 2
    minimal_value = float('inf')
    for row_index in range(start_row, len(A)):
        for element in A[row_index]:
            minimal_value = min(minimal_value, element)
    return(minimal_value)

import os.path
if len(sys.argv) != 3:
    print('Недостаточно параметров')
else:
    if not os.path.exists(sys.argv[1]):
        print('Файл не существует')
    else:
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")

        a_matrix = []
        b_matrix = []
        c_matrix = []
        get_matrix(a_matrix, input_file)
        get_matrix(b_matrix, input_file)
        get_matrix(c_matrix, input_file)

        a_answer = []
        b_answer = []
        c_answer = []
        # Работа с матрицей A
        minimal_value = end_answer(A, output_file)
        make_answer(a_answer, a_matrix, minimal_value)
        output_file.write(f"Ответ для А: {a_answer}\n")
        # Работа с матрицей Б
        minimal_value = end_answer(B, output_file)
        make_answer(b_answer, b_matrix, minimal_value)
        output_file.write(f"Ответ для B: {b_answer}\n")
        # Работа с матрицей C
        minimal_value = end_answer(C, output_file)
        make_answer(c_answer, c_matrix, minimal_value)
        output_file.write(f"Ответ для С: {c_answer}\n")

        input_file.close()
        output_file.close()
