import random

range_from = int(input("zakres liczb, od: "))
range_to = int(input("zakres liczb, do: "))
quantity_from = int(input("ile liczb, od? : "))
quantity_to = int(input("ile liczb, do? : "))
series_from = int(input("ile serii liczb, od? : "))
series_to = int(input("ile serii liczb, do? : "))

user_numbers = []



how_many_numbers = random.randint(quantity_from, quantity_to)

how_many_series = random.randint(series_from, series_to)

# for s in range(how_many_series):
for i in range(how_many_numbers):
    user_numbers.append(random.randint(range_from, range_to))

for s in range(how_many_series):
    print(user_numbers)


print(how_many_numbers)
print(how_many_series)
