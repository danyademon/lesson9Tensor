def password_checker(passwd):
    """
    Проверяет условия для пароля
    Параметры:
    passwd -- пароль
    Возвращает:
    True - если пароль подходит по всем параметрам
    False - если пароль не подходит хотя бы по одному параметру
    """
    if len(passwd)<6:
        print("Длина пароля должна быть не менее 6 символов")
        return False
    digits_counter = 0
    for i in filter(str.isdigit, passwd): digits_counter += 1
    if digits_counter == 0:
        print('Пароль должен содержать хотя бы одну цифру')
        return False
    if digits_counter == len(passwd):
        print('Пароль не должен состоять только из цифр')
        return False
    if passwd.lower().find('password') != -1:
        print('Пароль не должен содержать слово "password" в любом регистре')
        return False
    return True


# password = input('Введите пароль: ')

# pass_check_result = password_checker(password)

# if pass_check_result: print(f'Пароль {password} введен успешно.')

