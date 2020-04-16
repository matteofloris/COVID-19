# COVID-19

Calcolo della discrepanza tra dati ufficiali di decessi per COVID-19 al 28 Marzo 2020 e decessi reali.
Sorgenti di dati:
- comuni.csv e regioni.csv da http://demo.istat.it/pop2019/index3.html per ottenere la popolazione residente per regione e per comune
- comune_giorno.csv da https://www.istat.it/it/files//2020/03/comune-giorno.zip per ottenere il Dataset analitico con i decessi giornalieri in ogni singolo comune di residenza per sesso e classi di età quinquennali (per i primi 4 mesi degli anni che vanno dal 2015 al 2019 e, solo per i comuni verificati, l’aggiornamento per il periodo che va dall’1 gennaio al 28 marzo 2020)

Lanciare lo script:
python parser.py
per ottenere la tabella riassuntiva.
Una rielaborazione del risultato è il file allegato, a cui ho aggiunto i decessi ufficiali al 28 marzo e numero di tamponi al  28 marzo secondo la Protezione Civile (https://github.com/pcm-dpc)


