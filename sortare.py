
# Algoritmul Bubble Sort
def bubble_sort(numere):
    n = len(numere)

    for i in range(n):
        for j in range(0, n - i - 1):
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
