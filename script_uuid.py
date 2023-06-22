import uuid


# 1 вариант - самый понятный, как мне кажется
# создаем переменную строку, плюсуем ее с uuid начиная с 8 символа
# (по индексу 0-7 заменяем сиволы на autotest)
def first_function(identificator):
    string = 'autotest'
    a = string + identificator[8:]
    return a


# 2 вариант
# разбиваем строку на массивы (все что до первого - и после)
# с 0 индекса все приравниваем к нашей строке
# и соединяем нашу строку с сеператором - обратно (справа налево)
def second_function(identificator):
    string = 'autotest'
    b = identificator.split('-')
    b[0] = string
    c = '-'.join(b)
    return c


# 3 вариант - нагуглила что можно и так
# делим первую часть, которую нужно разделить от всей остальной по первому нахождению -
# и плюсуем нашу строку с разделителем и второй частью по индексу 1
def third_function(identificator):
    string = 'autotest'
    d = identificator.split('-', 1)
    e = string + '-' + d[1]
    return e


id = str(uuid.uuid4())
print(id)

print(first_function(id))
print(second_function(id))
print(third_function(id))
