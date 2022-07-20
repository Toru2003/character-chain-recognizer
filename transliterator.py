from scripts import Lexem
from scripts import data_output


def Transliterator(data):
    symbols = []
    i = 0
    while i < len(data):
        if data[i].isalpha():  #если i буква
            symbols.append(Lexem(data[i], "letter"))
        elif  data[i].isdigit():    #если i цифра
            symbols.append(Lexem(data[i], "fig"))
        elif data[i]=='=':
            symbols.append(Lexem(data[i], "equal"))
        elif data[i] == " ":
            symbols.append(Lexem(data[i], "space"))
        elif data[i] == ":":
            symbols.append(Lexem(data[i], "col"))
        elif data[i] == "+" or data[i] == "-":
            symbols.append(Lexem(data[i], "arithmsign"))
        elif data[i] == ";":
            symbols.append(Lexem(data[i], "end"))
        elif data[i] == "(":
            symbols.append(Lexem(data[i], "brcopen"))
        elif data[i] == ")":
            symbols.append(Lexem(data[i], "brcclose"))
        else:
            symbols.append(Lexem(data[i], "err"))
            data_output(0)
            exit(0)
        i += 1
    return symbols
