points = int(input("Podaj liczbę punktow (0-100): "))
print("Twoja ocena jest, ", end=" ")

if points > 95:
    print("bardzo dobra 5.0")
elif points > 84:
    print("ponad dobra 4.5")
elif points >= 70:
    print("dobra 4.0")
elif points > 60:
    print("dość dobra 3.5")
elif points > 50:
    print("dostateczna 3.0")
else:
    print("niedostateczna 2.0")