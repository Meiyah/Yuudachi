__author__ = 'Jens'
#csv bestand schrijven
import csv
csvbestand='kluizen.csv'

try:
    f = open(csvbestand, 'w')
    writer = csv.writer(f, delimiter=';')
    writer.writerow(('Kluisnummer', 'Code'))
finally:
    f.close()

def keuze():
    x = input("Wat is uw keuze?: ")
    print(x)

def keuze1():
    import random
    r = random.randrange(1000, 9999)


def keuze2():

()

def keuze3():
    ()

def keuze4():