**Sensor data analyse**

In dit Python-programma kan de gebruiker sensor data genereren, weergeven, inladen en analyseren

De gebruiker kan zelf het sensortype, het aantal metingen, de minimale en maximale sensorwaarde en een alertdrempel instellen

Het programma kan nieuwe sensormetingen genereren of eerder opgeslagen metingen uit een CSV-bestand inladen.

**Functionaliteiten**

Sensormetingen genereren: Genereert willekeurige sensorwaarden binnen een opgegeven bereik.

Data analyseren: Bereken het gemiddelde, de minimale waarde, de maximale waarde en de standaardafwijking met NumPy.

Alarmdrempel: Controleer welke sensormetingen boven de drempelwaarde liggen die de gebruiker zelf in kan stellen.

Lijngrafiek: Toont alle sensormetingen met een rode stippellijn voor de alertdrempel.

Histogram: Laat zien hoe de sensorwaarden verdeeld zijn.

CSV-bestanden: Kan sensormetingen opslaan en opnieuw laden.

Foutafhandeling: Controleert gebruikersinvoer en vangt verschillende fouten op.

**Benodigdheden**

Voor dit project heb je Python 3 en deze libraries nodig:

NumPy

Matplotlib

Installeer deze libraries via de terminal:

pip install numpy matplotlib

**Gebruik**

Start het programma in VS Code:

Na het starten kan de gerbuiker het keuzemenu volgen in de terminal deze vraagt:

Sensortype

Aantal metingen

Minimale sensorwaarde

Maximale sensorwaarde

Alertdrempel

Dan genereert het programma de metingen of pakt hij deze van het gegeven csv bestand en laat hij deze zien in 2 grafieken

Als je kiest om de data te genereren slaat het programma deze automatisch op

Projectstructuur

sensor-analysis/

sensor_monitor.py — main met alle functies.

sensor_data.csv — Bestand met opgeslagen sensormetingen.

README.md — Documentatie van het project.

Gebruikte bibliotheken
random  sensormetingen genereren
numpy   statistische berekeningen
matplotlib grafieken en histogrammen tekenen
csv     sensormetingen opslaan en inladen


