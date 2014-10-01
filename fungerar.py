__author__ = 'David'
__author__ = 'Andreas'

line = "Y"


while line not in ("n", "N"):
    val = input("Vad vill du gÃ¶ra? addition, subtraktion, multiplikation eller division?")



    if val == ("division"):
        siffra_1 = float(input("Skriv in tal 1:"))
        siffra_2 = float(input("Skriv in tal 2:"))
        print("Ditt svar Ã¤r:", siffra_1 / siffra_2)
        line = input("Vill du räka igen? j/n")
    if val == ("addition"):
        siffra_1 = float(input("Skriv in tal 1:"))
        siffra_2 = float(input("Skriv in tal 2:"))
        print("Ditt svar Ã¤r:", siffra_1 + siffra_2)
        line = input("Vill du räka igen? j/n")
    if val == ("subtraktion"):
        siffra_1 = float(input("Skriv in tal 1:"))
        siffra_2 = float(input("Skriv in tal 2:"))
        print("Ditt svar Ã¤r:", siffra_1 - siffra_2)
        line = input("Vill du räka igen? j/n")
    if val == ("multiplikation"):
        siffra_1 = float(input("Skriv in tal 1:"))
        siffra_2 = float(input("Skriv in tal 2:"))
        print("Ditt svar Ã¤r:", siffra_1 * siffra_2)

        line = input("Vill du räka igen? j/n")