# Laborator 6 – Algoritmi de sortare

Acest proiect conține o aplicație Python care implementează doi algoritmi de sortare și utilizează Jira pentru organizarea activităților.

## Algoritmi implementați

**1. Bubble Sort**

Compară numerele vecine și le schimbă pozițiile dacă nu sunt în ordine crescătoare.

**2. Insertion Sort**

Parcurge numerele și introduce fiecare element în poziția corectă.

Ambii algoritmi sunt implementați fără `sorted()` sau `list.sort()`.

## Fișierele proiectului

- `sortare.py` – programul Python care realizează sortarea.
- `date.txt` – conține numerele, algoritmul ales și rezultatul.
- `README.md` – descrierea proiectului.

## Exemplu de utilizare

Conținutul inițial al fișierului `date.txt`:

```text
7 8 2 3 4 5
Insertion
```

După rularea programului:

```text
7 8 2 3 4 5
Insertion
Insertion: 2 3 4 5 7 8
```

Programul execută doar algoritmul indicat pe a doua linie și păstrează datele inițiale.

## Rularea programului

1. Deschidem folderul proiectului în Visual Studio.
2. Verificăm ca `sortare.py` și `date.txt` să fie în același folder.
3. Introducem numerele pe prima linie din `date.txt`.
4. Pe a doua linie scriem `Bubble` sau `Insertion`.
5. Rulăm `sortare.py`.
6. Deschidem `date.txt` pentru a vedea rezultatul.

## Verificarea erorilor

Programul verifică existența fișierului, validitatea numerelor și numele algoritmului selectat.

## Organizarea în Jira

Am creat un proiect Kanban numit **Laborator 6**.

Am organizat activitățile folosind stările To Do, In Progress și Done.

Am creat trei task-uri pentru implementarea programului și un Bug pentru problema identificării fișierului `date.txt`.

## GitHub

Am lucrat pe trei branch-uri:

- `feature/bubble-sort`
- `feature/insertion-sort`
- `feature/file-io`

Pentru fiecare etapă am creat un Pull Request.
