
# Algoritmul Bubble Sort
def bubble_sort(numere):
    n = len(numere)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numere[j] > numere[j + 1]:
                numere[j], numere[j + 1] = numere[j + 1], numere[j]

    return numere

