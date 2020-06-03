# - *- coding: utf- 8 - *-
from parole import Parole

length = int(input('Jak długiego zlepku spółgłosek szukasz? '))
parole = Parole(length)
words = parole.get()
cnt = len(words)
print("Znaleziono {} zlepków".format(cnt))
if cnt:
    action = input("P - pokaż, Z - zapisz: ")
    if action.upper() == 'P':
        parole.show(words)
    elif action.upper() == 'Z':
        parole.save(words)
