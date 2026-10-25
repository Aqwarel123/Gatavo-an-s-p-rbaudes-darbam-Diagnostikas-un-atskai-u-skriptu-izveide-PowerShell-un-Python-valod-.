
skaits = {}

rindas = [
    "2026-10-25 12:00 ERROR Serveris1: kļūda",
    "2026-10-25 12:01 ERROR Serveris2: kļūda",
    "2026-10-25 12:02 ERROR Serveris1: kļūda",
    "2026-10-25 12:03 INFO Serveris2: viss kārtībā",
    "2026-10-25 12:04 ERROR Serveris1: kļūda"
]

for rinda in rindas:
    dalas = rinda.split()
    if dalas[2] == "ERROR":
        serviss = dalas[3].rstrip(":")
        skaits[serviss] = skaits.get(serviss, 0) + 1

for serviss, skaits_kopa in sorted(skaits.items(), key=lambda x: x[1], reverse=True):
    print(serviss, skaits_kopa)
