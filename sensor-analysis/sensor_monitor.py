import random
import numpy as np
import matplotlib.pyplot as plt
import csv
#krijg input van de user
def get_user_input():
    sensor_type = input("Welk sensortype wil je gebruiken? ")
    number_of_readings = int(input("Hoeveel metingen wil je genereren? "))
    min_value = float(input("Wat is de minimale sensorwaarde? "))
    max_value = float(input("Wat is de maximale sensorwaarde? "))
    alert_threshold = float(input("Wat is de drempelwaarde voor een alarm? "))

    return sensor_type, number_of_readings, min_value, max_value, alert_threshold
#genereer random sensor readings
def generate_readings(amount, min_val, max_val):
    random.seed(42)
    readings = []
    

    for i in range(amount):
        reading = random.uniform(min_val, max_val)
        readings.append(reading)
        

    return readings
#analizeer de data van de sensor readings
def analyze_readings(readings):
    average = np.mean(readings)
    max_value = np.max(readings)
    min_value = np.min(readings)
    standard_deviation = np.std(readings)

    return average, max_value, min_value, standard_deviation
#zoek naar outliers in de sensor readings
def find_outliers(readings, alert_threshold):
    alerts = []
    for reading in readings:
        if reading > alert_threshold:
            alerts.append(reading)
    return alerts
#maak een grafiek van de sensor readings
def plot_readings(readings, alert_threshold):
    sample_numbers = range(1, len(readings) + 1)

    plt.plot(sample_numbers, readings, label='Sensorwaarden', marker='o')
    plt.axhline(y=alert_threshold, color='r', linestyle='--', label='Drempelwaarde')
    plt.title("Sensormetingen")
    plt.xlabel("Meetnummer")
    plt.ylabel("Sensorwaarde")
    plt.grid(True)
    plt.legend()
    plt.show()
#maak een histogram van de sensor readings
def plot_histogram(readings):
    plt.hist(readings, bins=10)
    plt.title("Verdeling van gemeten waarden")
    plt.xlabel("Sensorwaarde")
    plt.ylabel("aantal metingen")
    plt.grid(True)
    plt.show()

#metingen opslaan in een csv bestand
def save_readings(readings, filename="sensor_data.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["hoeveelste waarde", "gemeten sensorwaarde"])
        for i, reading in enumerate(readings, start=1):
            writer.writerow([i, reading])

def load_readings(filename="sensor_data.csv"):
    readings = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            readings.append(float(row[1]))

    return readings


def main():
    print("Analyzeer je sensormetingen met dit programma.")
    print("1. Sensormetingen genereren")
    print("2. Sensormetingen inladen")

    choice = input("Maak een keuze (1 of 2): ")
    if choice == "1":
        print("Nieuwe metingen genereren")
        readings = generate_readings(amount, min_val, max_val)
    elif choice == "2":
        print("Bestaande metingen inladen")
        readings = load_readings()
    else:
        print("Ongeldige keuze")

    sensor, amount, min_val, max_val, alert_threshold = get_user_input()
    average, max_value, min_value, standard_deviation = analyze_readings(readings)
    outliers = find_outliers(readings, alert_threshold)
    print("Gekozen sensor:", sensor)
    print("Aantal metingen:", amount)
    print("Minimale sensorwaarde:", min_val)
    print("Maximale sensorwaarde:", max_val)
    print("Drempelwaarde voor een alarm:", alert_threshold)
    print("Gemiddelde sensorwaarde:", average)
    print("Maximale gemeten sensorwaarde:", max_value)
    print("Minimale gemeten sensorwaarde:", min_value)
    print("Standaardafwijking van de sensorwaarden:", standard_deviation)
    print("Gegenereerde metingen:", readings)
    print("Sensorwaarden boven de drempelwaarde (alerts):", outliers)
    print("Aantal alerts:", len(outliers))
    plot_readings(readings, alert_threshold)
    plot_histogram(readings)
    save_readings(readings)
    loaded_readings = load_readings()
    print("Ingelezen metingen:", loaded_readings)
    print(readings == loaded_readings)
    

if __name__ == "__main__":
    main()
