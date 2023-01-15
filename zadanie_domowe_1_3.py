own_funds = 30_000.
deposit = own_funds
factor1 = 0.075
factor2 = 0.08
factor3 = 0.0825
q = 0.25

print("Oprocentowanie lokaty:", factor1 * 100,"%\n")
deposit *= (1 + factor1 * q)
print("Saldo po I kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor1 * q)
print("Saldo po II kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor1 * q)
print("Saldo po III kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor1 * q)
print("Saldo po IV kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
print("Zysk rocznej lokaty z oprocentowaniem", factor1 * 100, "%, przy kapitalizacji kwartalnej wynosi", round(deposit - own_funds,2),
      "zł.\n\n")

own_funds = 30_000.
deposit = own_funds

print("Oprocentowanie lokaty:", factor2 * 100,"%\n")
deposit *= (1 + factor2 * q)
print("Saldo po I kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor2 * q)
print("Saldo po II kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor2 * q)
print("Saldo po III kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor2 * q)
print("Saldo po IV kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
print("Zysk rocznej lokaty z oprocentowaniem", factor2 * 100, "%, przy kapitalizacji kwartalnej wynosi", round(deposit - own_funds,2),
      "zł.\n\n")

own_funds = 30_000.
deposit = own_funds

print("Oprocentowanie lokaty:", factor3 * 100,"%\n")
deposit *= (1 + factor3 * q)
print("Saldo po I kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor3 * q)
print("Saldo po II kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor3 * q)
print("Saldo po III kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
deposit *= (1 + factor3 * q)
print("Saldo po IV kwartale kapitalizacji odsetek wynosi",round(deposit,2), "zł.\n ")
print("Zysk rocznej lokaty z oprocentowaniem", factor3 * 100, "%, przy kapitalizacji kwartalnej wynosi", round(deposit - own_funds,2),
      "zł.\n\n")