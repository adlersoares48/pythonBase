def func_exponencial(base_num, exp_num):
    result = 1
    for index in range(exp_num):
        result *= base_num
    return result
print(func_exponencial(3, 4))