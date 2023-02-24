range_from = int(input("od: "))
range_to = int(input("do: "))

is_first = True
for number in range(range_from, range_to + 1):
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        if not is_first:
            print(", ")
        print(number, end="")
    is_first = False
print(".")