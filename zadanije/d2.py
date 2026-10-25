rindas = [
    "INFO Sistema palaista",
    "ERROR Faila kļūda",
    "INFO Darbs pabeigts",
    "ERROR Tīkla kļūda"
]

skaits = 0

for rinda in rindas:
    if "error" in rinda.lower():
        skaits += 1

print("ERROR rindas:", skaits)
