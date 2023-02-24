user_number = int(input("Podaj liczbę całkowitą: "))

# print("{:08b}".format(user_number))

# print(bin(user_number))

print("Liczba jedynek w liczbie " + str(user_number) + " wynosi " + str(user_number.bit_count()) + ".")

# user_number.bit_count() - odkryłem tę funcjonalność wprowadzoną od wersji 3.10, od razu wylicza liczbe bitów :)