even_total = 0
odd_total = 0

while True:
    number = input("Podaj liczbę: ")
    try:
        val = int(number)
        if (val % 2 == 0):
            even_total = even_total + val
        else:
            odd_total = odd_total + val

    except ValueError:
        print("To nie jest liczba całkowita!")
        break


print("Dotychczasowa suma liczb parzystych wynosi: " + str(even_total))
print("Dotychczasowa suma liczb nieparzystych wynosi: " + str(odd_total))


# if (i % 2 == 0