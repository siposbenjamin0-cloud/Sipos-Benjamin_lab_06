
import os

# Bubble Sort
def bubble_sort(numere):
    for i in range(len(numere)):
        for j in range(len(numere) - 1):
            if numere[j] > numere[j + 1]:
                numere[j], numere[j + 1] = numere[j + 1], numere[j]

    return numere


# Insertion Sort
def insertion_sort(numere):
    for i in range(1, len(numere)):
        j = i

        while j > 0 and numere[j] < numere[j - 1]:
            numere[j], numere[j - 1] = numere[j - 1], numere[j]
            j = j - 1

    return numere


# Gasirea fisierului date.txt
folder = os.path.dirname(os.path.abspath(__file__))
cale = os.path.join(folder, "date.txt")

# Citirea fisierului
if os.path.exists(cale):
    fisier = open(cale, "r", encoding="utf-8")

    linia1 = fisier.readline()
    linia2 = fisier.readline()

    fisier.close()

    numere = []
    corect = True

    for x in linia1.split():
        if x.isdigit() or (len(x) > 1 and x[0] in "+-" and x[1:].isdigit()):
            numere.append(int(x))
        else:
            corect = False

    algoritm = linia2.strip()

    if linia1.strip() == "" or algoritm == "":
        print("Eroare: lipsesc datele!")

    elif not corect:
        print("Eroare: numere invalide!")

    elif algoritm != "Bubble" and algoritm != "Insertion":
        print("Eroare: algoritm necunoscut!")

    else:
        # Alegerea algoritmului
        if algoritm == "Bubble":
            rezultat = bubble_sort(numere)
        else:
            rezultat = insertion_sort(numere)

        # Pregatirea rezultatului
        text = ""

        for x in rezultat:
            text = text + str(x) + " "

        # Scrierea rezultatului in fisier
        fisier = open(cale, "w", encoding="utf-8")

        fisier.write(linia1.rstrip("\r\n") + "\n")
        fisier.write(linia2.rstrip("\r\n") + "\n")
        fisier.write(algoritm + ": " + text.strip() + "\n")

        fisier.close()

        print("Rezultat salvat in date.txt!")

else:
    print("Eroare: fisierul date.txt nu exista!")
    print("Fisierul este cautat aici:", cale)
