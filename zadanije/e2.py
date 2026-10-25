import csv

skaits = {"INFO": 747, "WARNING": 284, "ERROR": 146, "CRITICAL": 23}

with open(r"C:\Users\MB\Documents\zadanije\limeni.csv", "w", newline="", encoding="utf-8-sig") as f:
    rakstitajs = csv.writer(f, delimiter=";")
    rakstitajs.writerow(["Līmenis", "Skaits"])
    for limenis, skaits_kopa in skaits.items():
        rakstitajs.writerow([limenis, skaits_kopa])
