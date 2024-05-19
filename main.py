# - *- coding: utf- 8 - *-
from parole import Parole

length = int(input('Jak długiego zlepku spółgłosek szukasz? '))
parole = Parole(length)
words = parole.get()
cnt = len(words)
print("Znaleziono {} zlepków".format(cnt))
parole.show(words)
