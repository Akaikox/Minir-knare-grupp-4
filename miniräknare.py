__author__ = 'Andreas'

val = input("Vad vill du göra? Addition, subtraktion, multiplication eller division?")

if val == ("division"):
    siffra_1 = int(input("Skriv in tal 1:"))
    siffra_2 = int(input("Skriv in tal 2:"))
    print(siffra_1 / siffra_2)

if val == ("")