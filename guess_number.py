import random

number = random.randint(1, 3)
guess = int(input("Zgadnij jaka liczbe mam na mysli (1, 2, 3): "))
if guess == number:
    print("Brawo! To mialem na mysli!")
else:
    print("niestety myslalem o liczbie " + str(number) + ".")

#print(number)