#!/usr/bin/python3
def matrix_divided(matrix, div):
    counter = 0
    verify = []
    break_out_flag = False
    for i in matrix:
        for j in i:
            try:
                if type(j) not in [int, float]:
                    raise TypeError
            except TypeError:
                print("matrix must be a matrix (list of lists) \
                    of integers/floats")
                break_out_flag = True
                break
        if break_out_flag:
            break
    try:
        for i in matrix:
            for j in i:
                counter += 1
            if counter not in verify and len(verify) > 0:
                raise TypeError
            else:
                verify.append(counter)
                counter = 0
    except TypeError:
        print("Each row of the matrix must have the same size")
    try:
        if type(div) not in [int, float]:
            raise TypeError
        if div == 0:
            raise ZeroDivisionError
    except TypeError:
        print("div must be a number")
    except ZeroDivisionError:
        print("division by zero")
    try:
        return [[round(j/div, 2) for j in i] for i in matrix]
    except (TypeError, ZeroDivisionError):
        return
