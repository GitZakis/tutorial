# -*- coding: utf-8 -*-
# Πρόγραμμα: Υπολογισμός μέσου όρου 10 μαθητών σε 4 μαθήματα
# Python 2.7

kalyteros_mo = -1.0
kalyteros_mathitis = 0

for i in range(1, 11):   # 10 μαθητές
    print "-" * 40
    print "Μαθητής", i
    athroisma = 0.0

    for mathima in range(1, 5):   # 4 μαθήματα
        egkyros = False
        while not egkyros:
            vathmos = float(input("Δώσε βαθμό Μαθήματος %d (0-20): " % mathima))
            if 0 <= vathmos <= 20:
                egkyros = True
            else:
                print "Ο βαθμός πρέπει να είναι από 0 έως 20."
        athroisma = athroisma + vathmos

    mo = athroisma / 4.0
    print "Μέσος όρος μαθητή", i, "=", round(mo, 2)

    if mo > kalyteros_mo:
        kalyteros_mo = mo
        kalyteros_mathitis = i

print "-" * 40
print "Ο καλύτερος μέσος όρος ήταν:", round(kalyteros_mo, 2), "και τον είχε ο μαθητής", kalyteros_mathitis
