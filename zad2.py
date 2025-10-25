x = float(input("Podaj liczbę x: "))
y = float(input("Podaj liczbę y: "))
z = float(input("Podaj liczbę z: "))

if x < y and x < z:
    print(x)
    if y < z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif y < x and y < z:
    print(y)
    if x < z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif z < y and z < x:
    print(z)
    if y < x:
        print(y)
        print(x)
    else:
        print(x)
        print(y)