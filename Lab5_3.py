own_funds = 46_567.
deposit = own_funds
factor = 1.075

own_funds *= factor
own_funds *= factor
own_funds *= factor

print("Zysk z inwestycji wynosi:", round(deposit - own_funds, 2), "zł.")

