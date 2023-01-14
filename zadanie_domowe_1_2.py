#13TB = 13.000.000MB
#194MB = 5sek

d1 = 13631488
d2 = 194

t = 5

#print(round((d1 / d2) * t))

print("Potrzeba",round((((d1 / d2) * t) / 60) / 60), "godzin, aby pobrać 13 TB danych.")

