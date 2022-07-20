from collections import namedtuple    #создание лексемы
Lexem = namedtuple("Lexem", "symbol cls") #сама лексема lexem-название symbol-символ(ы) cls-класс

'''
Модуль collections - предоставляет специализированные типы 
данных, на основе словарей, кортежей, множеств, списков.

Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением, 
что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ к ним

'''
def data_input():      #файл цепочки
    with open("input.txt") as file:
        s = file.read()
        return s


def data_output(result): #результат просчитывания цепочки
    with open("output.txt", "w") as file:
        if result: #если result будет равен одному
            file.write('ACCEPT')
        else:
            file.write('REJECT')

