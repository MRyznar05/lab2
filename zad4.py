gol = int(input('Liczba goli: '))
punkty = gol * 10

if gol >= 5 and gol <= 10:
    bonus = 5
    punkty = punkty + bonus
    print(punkty)
elif gol > 10:
    bonus = 15
    punkty = punkty + bonus
    print(punkty)
else:
    print(punkty)