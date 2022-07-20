from scripts import Lexem
from scripts import data_output
import transliterator as tlr

def Lexer(symbols):
    words = []
    now = [' ', 'None']
    state = "space"

    for s in symbols:
        if s.cls == 'letter': #если буква
            if state =="space":
                words.append(Lexem(*now))
                now[0] = s.symbol
                now[1] = "identifier"
                state = 'identif'
            elif state == 'identif':
                now[0] += s.symbol
            elif state == 'arithmsign':
                state = 'space'
            elif state == 'col':
                state = 'space'
            elif state == 'equal':
                state = 'space'
            elif state == 'brcopen':
                state = 'space'
            elif state == 'brcclose':
                state = 'space'
            elif state == 'end':
                state = 'space'
            elif state == 'end':
                state = 'space'
            else:
                data_output(0)
                exit(0)
        elif s.cls == 'fig':   #если цифра
            if state=='space':
                words.append(Lexem(*now))
                now[0] = s.symbol
                now[1] = "fig"
                state='namber'
            elif  state=="identif":
                now[0] +=s.symbol
            elif state=='namber':
                now[0] += s.symbol
            elif state == 'arithmsign':
                state = 'space'
            elif state == 'col':
                state = 'space'
            elif state == 'equal':
                state = 'space'
            elif state == 'brcopen':
                state = 'space'
            elif state == 'brcclose':
                state = 'space'
            elif state == 'end':
                state = 'space'
            else:
                data_output(0)
                exit(0)
        elif s.cls == 'space':
            state ='space'
        elif s.cls =='arithmsign':
            words.append(Lexem(*now))
            now[0] = s.symbol
            now[1] = "arithmsign"
            state = 'space'
        elif s.cls =='col':
            words.append(Lexem(*now))
            now[0] = s.symbol
            now[1] = "col"
            state = 'space'
        elif s.cls =='equal':
            words.append(Lexem(*now))
            now[0] = s.symbol
            now[1] = "equal"
            state = 'space'
        elif s.cls =='end':
            words.append(Lexem(*now))
            now[0] = s.symbol
            now[1] = "end"
            state = 'space'
        elif s.cls =='brcopen':
            words.append(Lexem(*now))
            now[0] = s.symbol
            now[1] = "brcopen"
            state = 'space'
        elif s.cls =='brcclose':
            words.append(Lexem(*now))
            now[0] = s.symbol
            now[1] = "brcclose"
            state = 'space'
        elif s.cls =='err':
            data_output(0)
            exit(0)
        else:
            data_output(0)
            exit(0)
    words.append(Lexem(*now))
    words.pop(0)
    return words





