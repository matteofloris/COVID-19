import sys, os

#Sardegna = {}

valori_regione = {}
lista_comuni = {}

#### carica il numero di decessi ufficiali per ogni comune di Italia, sia il valore del 2020 sia il valore medio dei 5 anni precedenti
f = open("comune_giorno.csv", "r")
for l in f:
	c = l.strip().split(",")
	if c[-1].strip() != "9999" and "TOTALE_15" not in l:
		regione = c[2].strip()
		if "/" in regione: regione = regione.split("/")[0].strip()
		if regione not in valori_regione:
			valori_regione[regione] = {"avg_2015_2019":0, "2020":0}
		comune = str(int(c[5].strip()))
		if comune not in ["24125", "6193"]: 
			if comune not in lista_comuni:
				lista_comuni[comune] = regione
			valori_regione[regione]["2020"] += int(c[-1])
			avg = float(int(c[-2]) + int(c[-3]) + int(c[-4]) + int(c[-5]) + int(c[-6]) ) / 5
			valori_regione[regione]["avg_2015_2019"] += avg
		#if regione == "Sardegna": Sardegna[comune] = 0
f.close()

## estrae il numero di residenti al 2019 dei comuni del campione
residenti_2019_comuni_campione = {}
f = open("comuni.csv", "r")
for l in f:
	c = l.strip().split(",")
	if "Maschi" not in l and "Popolazione" not in l and c[2].strip() == "999":
		comune = str(int(c[0].strip()))
		if comune in lista_comuni:
			if comune not in residenti_2019_comuni_campione:
				residenti_2019_comuni_campione[comune] = 0
			residenti_2019_comuni_campione[comune] += int(c[10]) #M
			residenti_2019_comuni_campione[comune] += int(c[-1]) #F

			#if comune in Sardegna: Sardegna[comune] = residenti_2019_comuni_campione[comune]
f.close()

# estrae il numero di residenti per regione 
residenti_2019_regioni = {}
f = open("regioni.csv", "r")
for l in f:
	c = l.strip().split(",")
	if "Maschi" not in l and "Popolazione" not in l and "Totale" in l:
		regione = c[0].strip()
		if "/" in regione: regione = regione.split("/")[0].strip()
		if regione not in residenti_2019_regioni:
			residenti_2019_regioni[regione] = 0
		residenti_2019_regioni[regione] += int(c[9])  #M
		residenti_2019_regioni[regione] += int(c[-1]) #F
f.close()


### STAMPA per ogni regione
# nome, decessi_2020, decessi_pre2020, popolazione_campione, residenti_totali
for regione in valori_regione:
	decessi_2020 = valori_regione[regione]["2020"]
	decessi_pre2020 = valori_regione[regione]["avg_2015_2019"]
	popolazione_campione = 0
	for comune in lista_comuni:
		if lista_comuni[comune] == regione:
			popolazione_campione += residenti_2019_comuni_campione[comune]
	residenti_totali = residenti_2019_regioni[regione]

	print regione, decessi_2020, decessi_pre2020, popolazione_campione, residenti_totali
