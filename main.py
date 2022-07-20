import scripts as file_manager
import transliterator as tlr
import lexer
import keywords
import syntax
fm = file_manager.data_input()
trled = tlr.Transliterator(fm)

with open("log/transliteratorLog.txt", "a") as file:
    file.write("\n")
    file.write(str(trled))
    file.write("\n")

words = lexer.Lexer(trled)


with open("log/LexerLog.txt", "a") as file:
    file.write("\n")
    file.write(str(words))
    file.write("\n")

keywords.Keywords(words)

with open("log/KeywordsLog.txt", "a") as file:
    file.write("\n")
    file.write(str(words))
    file.write("\n")

result = syntax.Syntax(words)


with open("log/SyntaxLog.txt", "a") as file:
    file.write("\n")
    file.write(str(result))
    file.write("\n")

file_manager.data_output(result)

print(result)



