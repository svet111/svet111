#Даны три матрицы a, b и c разного размера. Какая из матриц имеет наибольшую сумму элементов, кратных заданному числу и
# расположенных ниже главной/побочной диагонали и на ней?
import sys
def get_matrix(result, from_file):
    # side - длина стороны квадратной матрицы
    side = int(from_file.readline())
    for row_index in range(side):
        result.append(list(map(int, from_file.readline().split())))
    # теперь result содержит считанную матрицу
    # размера side X side
def calculate_main_diagonal(matrix, divider):
    answer = 0
    for i in range(len(matrix)):
        for j in range(i + 1):
            if matrix[i][j] % divider == 0:
                answer += matrix[i][j]
    return answer
def calculate_minor_diagonal(matrix, divider):
    answer = 0
    for i in range(len(matrix)):
        for j in range(i + 1):
            if matrix[i][-j - 1] % divider == 0:
                answer += matrix[i][-j - 1]
    return answer
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
        a_div = 0
        b_matrix = []
        b_div = 0
        c_matrix = []
        c_div = 0
        get_matrix(a_matrix, input_file)
        a_div = int(input_file.readline())
        get_matrix(b_matrix, input_file)
        b_div = int(input_file.readline())
        get_matrix(c_matrix, input_file)
        c_div = int(input_file.readline())

        # (сумма под (или на) главной диагональю; сумма под(или на) побочной диагональю)
        a_summs = (calculate_main_diagonal(a_matrix, a_div),
                   calculate_minor_diagonal(a_matrix, a_div))
        b_summs = (calculate_main_diagonal(b_matrix, b_div),
                   calculate_minor_diagonal(b_matrix, b_div))
        c_summs = (calculate_main_diagonal(c_matrix, c_div),
                   calculate_minor_diagonal(c_matrix, c_div))
        # Максимум между суммами под (или на) главной диагональю
        main_diag_max = max(a_summs[0], b_summs[0], c_summs[0])
        # Максимум между суммами под (или на) побочной диагональю
        minor_diag_max = max(a_summs[1], b_summs[1], c_summs[1])

        # Количество матриц с такой же макс суммой под главной диаг
        count_main_diag_max = 0
        if a_summs[0] == main_diag_max:
            count_main_diag_max += 1
        if b_summs[0] == main_diag_max:
            count_main_diag_max += 1
        if c_summs[0] == main_diag_max:
            count_main_diag_max += 1

        # Количество матриц с такой же макс суммой под побоч диаг
        count_minor_diag_max = 0
        if a_summs[1] == minor_diag_max:
            count_minor_diag_max += 1
        if b_summs[1] == minor_diag_max:
            count_minor_diag_max += 1
        if c_summs[1] == minor_diag_max:
            count_minor_diag_max += 1

        if count_main_diag_max != 1:
            output_file.write(
                f"Количество матриц с максимальной суммой под (или на) главной диагональю = {count_main_diag_max}\n")
        if count_minor_diag_max != 1:
            output_file.write(
                f"Количество матриц с максимальной суммой под (или на) побочной диагональю = {count_minor_diag_max}\n")
        if a_summs[0] == main_diag_max:
            output_file.write(
                "Матрица А имеет максимальную сумму под (или на) главной диагональю\n")
        if b_summs[0] == main_diag_max:
            output_file.write(
                "Матрица B имеет максимальную сумму под (или на) главной диагональю\n")
        if c_summs[0] == main_diag_max:
            output_file.write(
                "Матрица C имеет максимальную сумму под (или на) главной диагональю\n")

        if a_summs[1] == minor_diag_max:
            output_file.write(
                "Матрица А имеет максимальную сумму под (или на) побочной диагональю\n")
        if b_summs[1] == minor_diag_max:
            output_file.write(
                "Матрица B имеет максимальную сумму под (или на) побочной диагональю\n")
        if c_summs[1] == minor_diag_max:
            output_file.write(
                "Матрица C имеет максимальную сумму под (или на) побочной диагональю\n")

        input_file.close()
        output_file.close()
