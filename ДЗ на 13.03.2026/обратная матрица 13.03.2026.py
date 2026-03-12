a11, a12, a13, a21, a22, a23, a31, a32, a33 = 31, 2.8, 1.9, 1.9, 31, 2.1, 7.5, 3.8, 48
b1, b2, b3 = 2, 21, 56
da = (a11 * a22 * a33) + (a12 * a23 * a31) + (a21 * a32 * a13) - (a13 * a22 * a31) - (a11 * a23 * a32) - (a12 * a21 * a33)
if da == 0:
    print("Определитель равен нулю. Метод обратной матрицы неприменим.")
else:

    A11 = (a22 * a33 - a23 * a32)
    A12 = -(a21 * a33 - a23 * a31)
    A13 = (a21 * a32 - a22 * a31)
    A21 = -(a12 * a33 - a13 * a32)
    A22 = (a11 * a33 - a13 * a31)
    A23 = -(a11 * a32 - a12 * a31)
    A31 = (a12 * a23 - a13 * a22)
    A32 = -(a11 * a23 - a13 * a21)
    A33 = (a11 * a22 - a12 * a21)


    inv_a11 = A11 / da
    inv_a12 = A21 / da
    inv_a13 = A31 / da

    inv_a21 = A12 / da
    inv_a22 = A22 / da
    inv_a23 = A32 / da

    inv_a31 = A13 / da
    inv_a32 = A23 / da
    inv_a33 = A33 / da


    x1 = inv_a11 * b1 + inv_a12 * b2 + inv_a13 * b3
    x2 = inv_a21 * b1 + inv_a22 * b2 + inv_a23 * b3
    x3 = inv_a31 * b1 + inv_a32 * b2 + inv_a33 * b3

    print(round(x1, 2), round(x2, 2), round(x3, 2))
