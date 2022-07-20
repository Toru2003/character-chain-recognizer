from scripts import Lexem


keywords_list = ["and", "array", "asm", "begin", "break", "case", "const", "constructor", "continue", "destructor",
                 "div",
                 "do", "downto", "else", "end", "false", "file", "for", "function", "goto", "if", "implementation",
                 "in",
                 "inline", "interface", "label", "mod", "nil", "not", "object", "of", "on", "operator", "or", "packed",
                 "procedure", "program", "record", "repeat", "set", "shl", "shr", "string", "then", "to", "true",
                 "type",
                 "unit", "until", "uses", "var", "while", "with", "xor"]


def Keywords(words):

    for i in range(len(words)):
        if words[i].cls == "identifier":
            index = words[i].symbol.lower()
            if index in keywords_list:
                words[i] = Lexem(words[i].symbol, 'keyword'+index)
                continue
    return words















































