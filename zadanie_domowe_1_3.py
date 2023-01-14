own_funds = 30_000.
factor = 0.075
q1 = 0.25
q2 = 0.5
q3 = 0.75

saldo_q1 = round(own_funds + (own_funds * (factor * q1)), 2)
saldo_q2 = round(saldo_q1 + (saldo_q1 * (factor * q2)), 2)
saldo_q3 = round(saldo_q2 + (saldo_q2 * (factor * q3)), 2)
saldo_q4 = round(saldo_q3 + (saldo_q3 * factor), 2)

print(saldo_q1)
print(saldo_q2)
print(saldo_q3)
print(saldo_q4)

print("Roczny zysk z inwestycji wyniesie", saldo_q4, "zł. Saldo po pierwszym kwartale wyniesie", saldo_q1,
      "zł., po drugim kwartale wyniesie", saldo_q2, "zł., natomiast po trzecim kwartale będzie równe", saldo_q3, "zł.",
      "\n")


#
# deposit1 = own_funds
# deposit2 = own_funds
# deposit3 = own_funds
# factor1 = 1.075
# factor2 = 1.08
# factor3 = 1.0825
# deposit1 *= factor1
# deposit2 *= factor2
# deposit3 *= factor3
# saldo1 = round(deposit1 - own_funds, 2) / 4 + own_funds
# saldo2 = round(deposit1 - own_funds, 2) / 4 + saldo1
# saldo3 = round(deposit1 - own_funds, 2) / 4 + saldo2
# saldo4 = round(deposit2 - own_funds, 2) / 4 + own_funds
# saldo5 = round(deposit2 - own_funds, 2) / 4 + saldo4
# saldo6 = round(deposit2 - own_funds, 2) / 4 + saldo5
# saldo7 = round(deposit3 - own_funds, 2) / 4 + own_funds
# saldo8 = round(deposit3 - own_funds, 2) / 4 + saldo7
# saldo9 = round(deposit3 - own_funds, 2) / 4 + saldo8
#
# print("Roczny zysk z inwestycji wyniesie", round(deposit1 - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie",
#       saldo1, "zł., po drugim kwartale wyniesie", saldo2, "zł., natomiast po trzecim kwartale będzie równe", saldo3, "zł.", "\n")
# print("Roczny zysk z inwestycji wyniesie", round(deposit2 - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie",
#       saldo4, "zł., po drugim kwartale wyniesie", saldo5, "zł., natomiast po trzecim kwartale będzie równe", saldo6, "zł.", "\n")
# print("Roczny zysk z inwestycji wyniesie", round(deposit3 - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie",
#       saldo7, "zł., po drugim kwartale wyniesie", saldo8, "zł., natomiast po trzecim kwartale będzie równe", saldo9, "zł.", "\n")
