import sys, os

#Sardegna = {}

#### carica il numero di decessi ufficiali per ogni comune di Italia, sia il valore del 2020 sia il valore medio dei 5 anni precedenti
giorni = {}
f = open("comune_giorno.csv", "r")
for l in f:
	c = l.strip().split(",")
	if c[-1].strip() != "9999" and "Sardegna" in l:
		comune = str(int(c[5].strip()))
		giorno = str(int(c[7].strip()))
		if giorno not in giorni:
			giorni[giorno] = [0, 0]
		dato_2020 = int(c[-1])
		dato_avg = float(int(c[-2]) + int(c[-3]) + int(c[-4]) + int(c[-5]) + int(c[-6]) ) / 5
		giorni[giorno][0] += dato_avg
		giorni[giorno][1] += dato_2020
f.close()

for G in giorni:
	print G, giorni[G][0], giorni[G][1]




