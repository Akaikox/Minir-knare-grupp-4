__author__ = 'Andreas'

val = input("Vad vill du göra? addition, subtraktion, multiplication eller division?")

if val == ("division"):
    siffra_1 = int(input("Skriv in tal 1:"))
    siffra_2 = int(input("Skriv in tal 2:"))
    print("Ditt svar är:", siffra_1 / siffra_2)

if val == ("addition"):
    siffra_1 = int(input("Skriv in tal 1:"))
    siffra_2 = int(input("Skriv in tal 2:"))
    print("Ditt svar är:", siffra_1 + siffra_2)