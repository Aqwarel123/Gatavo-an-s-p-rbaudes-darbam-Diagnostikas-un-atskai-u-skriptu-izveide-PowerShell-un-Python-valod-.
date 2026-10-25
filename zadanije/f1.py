import sys

if len(sys.argv) < 2:
    print("Lietošana: python f1.py ERROR")
    sys.exit()

limenis = sys.argv[1]
rindas = []

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        if limenis in rinda:
            rindas.append(rinda.strip())

print("Skaits:", len(rindas))
print(*rindas[:3], sep="\n")
