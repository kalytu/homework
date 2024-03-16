def sz(spis):
    su = sum(spis)
    kile = len(spis)
    ser = su / kile
    return ser


ch = [1, 2, 3, 4, 5]
szch = sz(ch)
print("середнє значення чисел:", szch)


def per(chis):
    if chis < 2:
        return False
    for i in range(2, int(chis ** 0.5) + 1):
        if chis % i == 0:
            return False
    return True


chis = 17
prost = per(chis)
print(f"Число {chis} є простим: {prost}")


def golos(ryad):
    golos = "аоуіие"
    col= 0
    for buk in ryad:
        if buk in golos:
            col += 1
    return col

ryad = "сюди щось писати"
kolg = golos(ryad)
print("кількість голосних:", kolg)


a = int(input('a = '))
b = int(input('b = '))

def nsd(a, b):
    while a*b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b            

print (nsd(a, b))
