own_funds = 30_000.

deposit1 = own_funds
deposit2 = own_funds
deposit3 = own_funds
factor1 = 1.075
factor2 = 1.08
factor3 = 1.0825
deposit1 *= factor1
deposit2 *= factor2
deposit3 *= factor3
saldo1 = round(deposit1 - own_funds, 2) / 4 + own_funds
saldo2 = round(deposit1 - own_funds, 2) / 4 + saldo1
saldo3 = round(deposit1 - own_funds, 2) / 4 + saldo2
saldo4 = round(deposit2 - own_funds, 2) / 4 + own_funds
saldo5 = round(deposit2 - own_funds, 2) / 4 + saldo4
saldo6 = round(deposit2 - own_funds, 2) / 4 + saldo5
saldo7 = round(deposit3 - own_funds, 2) / 4 + own_funds
saldo8 = round(deposit3 - own_funds, 2) / 4 + saldo7
saldo9 = round(deposit3 - own_funds, 2) / 4 + saldo8

print("Roczny zysk z inwestycji wyniesie", round(deposit1 - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie",
      saldo1, "zł., po drugim kwartale wyniesie", saldo2, "zł., natomiast po trzecim kwartale będzie równe", saldo3, "zł.", "\n")
print("Roczny zysk z inwestycji wyniesie", round(deposit2 - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie",
      saldo4, "zł., po drugim kwartale wyniesie", saldo5, "zł., natomiast po trzecim kwartale będzie równe", saldo6, "zł.", "\n")
print("Roczny zysk z inwestycji wyniesie", round(deposit3 - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie",
      saldo7, "zł., po drugim kwartale wyniesie", saldo8, "zł., natomiast po trzecim kwartale będzie równe", saldo9, "zł.", "\n")