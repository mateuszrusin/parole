# - *- coding: utf- 8 - *-
from parole import Parole
import time

length = int(input('Jak długiego zlepku spółgłosek szukasz? '))
parole = Parole(length)

start_time = time.time()
words = parole.get_by_pandas()
end_time = time.time()

print("Znaleziono {} zlepków".format(sum(len(sublist) for sublist in words.values())))
print(f"Czas wykonania funkcji get_by_pandas(): {end_time - start_time:.4f} sekund")

parole.show(words)

start_time = time.time()
words = parole.get()
end_time = time.time()

print("Znaleziono {} zlepków".format(sum(len(sublist) for sublist in words.values())))
print(f"Czas wykonania funkcji get(): {end_time - start_time:.4f} sekund")

parole.show(words)
