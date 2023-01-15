own_funds = 30_000.
deposit = own_funds
factor1 = 0.075
factor2 = 0.08
factor3 = 0.0825
q1 = 0.25
q2 = 0.5
q3 = 0.75

# saldo_q1 = round(own_funds + deposit * factor1 * q1, 2)
# saldo_q2 = round(own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2, 2)
# saldo_q3 = round(own_funds + (own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2) * factor1 * q3, 2)
# saldo_q4 = round(own_funds + (own_funds + (own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2) * factor1 * q3) * factor1, 2)
# profit = round((own_funds + (own_funds + (own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2) * factor1 * q3) * factor1) - own_funds, 2)
#
# print(saldo_q1)
# print(saldo_q2)
# print(saldo_q3)
# print(saldo_q4)
# print(profit)

print("Roczny zysk z inwestycji wyniesie", round((own_funds + (own_funds + (own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2) * factor1 * q3) * factor1) - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie", round(own_funds + deposit * factor1 * q1, 2),
      "zł., po drugim kwartale wyniesie", round(own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2, 2), "zł., po trzecim kwartale będzie równe", round(own_funds + (own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2) * factor1 * q3, 2), "zł., natomiast po czwartym kwartale będzie równe",
      round(own_funds + (own_funds + (own_funds + (own_funds + deposit * factor1 * q1) * factor1 * q2) * factor1 * q3) * factor1, 2), "zł.\n")

print("Roczny zysk z inwestycji wyniesie", round((own_funds + (own_funds + (own_funds + (own_funds + deposit * factor2 * q1) * factor2 * q2) * factor2 * q3) * factor2) - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie", round(own_funds + deposit * factor2 * q1, 2),
      "zł., po drugim kwartale wyniesie", round(own_funds + (own_funds + deposit * factor2 * q1) * factor2 * q2, 2), "zł., po trzecim kwartale będzie równe", round(own_funds + (own_funds + (own_funds + deposit * factor2 * q1) * factor2 * q2) * factor2 * q3, 2), "zł., natomiast po czwartym kwartale będzie równe",
      round(own_funds + (own_funds + (own_funds + (own_funds + deposit * factor2 * q1) * factor2 * q2) * factor2 * q3) * factor2, 2), "zł.\n")

print("Roczny zysk z inwestycji wyniesie", round((own_funds + (own_funds + (own_funds + (own_funds + deposit * factor3 * q1) * factor3 * q2) * factor3 * q3) * factor3) - own_funds, 2), "zł. Saldo po pierwszym kwartale wyniesie", round(own_funds + deposit * factor3 * q1, 2),
      "zł., po drugim kwartale wyniesie", round(own_funds + (own_funds + deposit * factor3 * q1) * factor3 * q2, 2), "zł., po trzecim kwartale będzie równe", round(own_funds + (own_funds + (own_funds + deposit * factor3 * q1) * factor3 * q2) * factor3 * q3, 2), "zł., natomiast po czwartym kwartale będzie równe",
      round(own_funds + (own_funds + (own_funds + (own_funds + deposit * factor3 * q1) * factor3 * q2) * factor3 * q3) * factor3, 2), "zł.\n")
