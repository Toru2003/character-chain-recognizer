from scripts import Lexem

def Syntax(words):
    state = "start"
    for s in words:
        if state == 'start':
            if s.cls == 'keywordif':
                state = 'ifcl'
            else:
                return 0

        elif state == 'ifcl':
            if s.cls == 'identifier':
                state = 'name'
            else:
                return 0

        elif state == 'name':
            if s.cls == 'keywordthen':
                state = 'thencl'
            else:
                return 0

        elif state == 'thencl':
            if s.cls == 'identifier':
                state = 'name2'
            else:
                return 0

        elif state == 'name2':
            if s.cls == 'col':
                state = 'colon'
            else:
                return 0


        elif state == 'colon':
            if s.cls == 'equal':
                state = 'equ'
            else:
                return 0

        elif state == 'equ':
            if s.cls == 'identifier':
                state = 'func'
            else:
                return 0


        elif state == 'func':
            if s.cls == 'brcopen':
                state = 'brc1'
            else:
                return 0

        elif state == 'brc1':
            if s.cls == 'identifier':
                state = 'name3'
            else:
                return 0

        elif state == 'name3':
            if s.cls == 'brcclose':
                state = 'brc2'
            else:
                return 0

        elif state == 'brc2':
            if s.cls == 'keywordelse':
                state = 'elsecl'
            elif s.cls == 'end':
                state = 'semicolon'
            else:
                return 0
        elif state == 'semicolon':   #так как .cls состоит из символов то проверяем если после semicolon есть к примеру переменная то выводим 0
            if s.cls.isalnum():
                return 0
            else:
                continue
        elif state == 'elsecl':
            if s.cls == 'identifier':
                state = 'func2'
            else:
                return 0

        elif state == 'func2':
            if s.cls == 'brcopen':
                state = 'brc3'
            else:
                return 0

        elif state == 'brc3':
            if s.cls == 'fig':
                state = 'namber'
            elif s.cls == 'arithmsign':
                state = 'znak'
            else:
                return 0

        elif state == 'znak':
            if s.cls == 'fig':
                state = 'namber'
            else:
                return 0

        elif state == 'namber':
            if s.cls == 'brcclose':
                state = 'brc4'
            else:
                return 0

        elif state == 'brc4':
            if s.cls == 'end':
                state = 'semicolon'
            else:
                return 0

    if state == 'semicolon':
        return 1
    else:
        return 0
















