def summ_of_all(*args):
    """
    Считает сумму всех входных аргументов
    
    Параметры:
    *args - любое кол-во входных элементов
    Возвращает:
    sum - сумму всех входных элементов
    """
    sum = 0
    for elem in args:
        sum += elem
    return sum

# print(summ_of_all(1, 2, 3, 4, 5, 6))
# print(summ_of_all())
# print(summ_of_all(23, 25))
# print(summ_of_all(3.0, 2.0))