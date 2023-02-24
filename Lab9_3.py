# 0 1 0 0 1 - przykładowa liczba (9)
# 0 0 0 0 1 - maska
# &
# 0 0 0 0 1 - wynik (1)

number = int(input("Podaj liczbę: "))
n = int(input("Podaj nr bitu: "))

mask = 1 << n
result = number & mask

bit = int(bool(result))
print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit)

# sprawdzewnie
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(result))