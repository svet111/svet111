#Вычислить значение выражения PA + 2 · PB – PC, где PA, PB и PC – произведения положительных элементов, не лежащих на
# главной диагонали, в матрицах A, B и C соответственно. Если вычисленное значение отрицательно, то заменить в
# матрицах отрицательные элементы их модулями, и снова вычислить значение этого выражения.
import sys
from module import *
import os.path
if len(sys.argv) != 3:
    print('Недостаточно параметров')
else:
    if not os.path.exists(sys.argv[1]):
        print('Файл не существует')
    else:
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")

        mat_A = get_matrix(input_file)
        mat_B = get_matrix(input_file)
        mat_C = get_matrix(input_file)
        p_A = calc_p(mat_A)
        p_B = calc_p(mat_B)
        p_C = calc_p(mat_C)

        value = p_A + 2 * p_B - p_C

        if value < 0:
            output_file.write(
                f"Вычисленное значение {value} отрицательно, заменяю элементы матрицы модулями\n")
            # если вычисленное значение отрицательно, заменяю отриц элементы их модулями в каждой матрице
            mat_A = abs_matrix(mat_A)
            mat_B = abs_matrix(mat_B)
            mat_C = abs_matrix(mat_C)
            p_A = calc_p(mat_A)
            p_B = calc_p(mat_B)
            p_C = calc_p(mat_C)
            value = p_A + 2 * p_B - p_C

        output_file.write(f"Вычисленное значение: {value}")

        input_file.close()
        output_file.close()
