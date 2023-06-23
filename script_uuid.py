import uuid


def generate_uuid():
    return str(uuid.uuid4())


# 1 вариант - самый понятный, как мне кажется
# создаем переменную строку, плюсуем ее с uuid начиная с 8 символа
# (по индексу 0-7 заменяем сиволы на autotest)
def first_function():
    identificator = generate_uuid()
    string = 'autotest'
    a = string + identificator[8:]
    return a


# 2 вариант
# разбиваем строку на массивы (все что до первого - и после)
# с 0 индекса все приравниваем к нашей строке
# и соединяем нашу строку с сеператором - обратно (справа налево)
def second_function():
    identificator = generate_uuid()
    string = 'autotest'
    b = identificator.split('-')
    b[0] = string
    c = '-'.join(b)
    return c


# 3 вариант - нагуглила что можно и так
# делим первую часть, которую нужно разделить от всей остальной по первому нахождению -
# и плюсуем нашу строку с разделителем и второй частью по индексу 1
def third_function():
    identificator = generate_uuid()
    string = 'autotest'
    d = identificator.split('-', 1)
    e = string + '-' + d[1]
    return e


# 4 вариант - в строке нельзя заменить символы по их индексу, поэтому собираем
# еще одну строку посимвольно в цикле:
# первые 8 символов берем из строки autotest, а оставшиеся из uuid
def fourth_function():
    identificator = generate_uuid()
    string = 'autotest'
    result = ''

    for i in range(len(identificator)):
        if i < 8:
            result = result + string[i]
        else:
            result = result + identificator[i]
    return result


# 5 вариант - заменяем в листе uuid первые символы на все символы строки autotest
# получаем готовый лист и преобразуем его в строку с помощью join
def fifth_function():
    identificator = generate_uuid()
    string = 'autotest'
    id_list = list(identificator)

    for i in range(8):
        id_list[i] = string[i]
    return ''.join(id_list)



print(first_function())
print(second_function())
print(third_function())
print(fourth_function())
print(fifth_function())
