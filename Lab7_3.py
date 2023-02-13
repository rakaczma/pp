import random

number = random.randint(1, 10)
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10): "
guess = int(input(msg))
if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Masz kolejną szansę, moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało się odgadnąć za drugim razem!")
    else:
        msg = "Masz kolejną szansę, moja liczba jest "
        if number > 5:
            msg += "większa "
        else:
            msg += "mniejsza lub równa "
        msg += "od liczby 5: "
        guess = int(input(msg))
        if guess == number:
            print("Brawo! A jednak do trzech razy sztuka!")
        else:
            msg = "Niestety, myślałem o liczbie " + str(number) + "."
            print(msg)

