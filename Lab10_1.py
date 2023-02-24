names = []
total_elements = int(input("Podaj liczbę imion: "))

for i in range(1, total_elements + 1):
    names.append(input("Podaj " + i + " imię: "))

print("Pobrano zbiór imion:", names)