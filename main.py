a = int(input("введіть число:"))

print(a)

if a%2==0 :
    print('число парне')
else :
    print('число не парне')




b = int(input("введіть число: "))

print("числа від 1 до", b, "включно:")
for i in range(1, number + 1):
    print(i)


def is_prime(c):
    if c <= 1:
        return False
    for i in range(2, int(numbcer**0.5) + 1):
        if c % i == 0:
            return False
    return True

c = int(input("введіть число: "))

if is_prime(c):
    print(c, "є простим числом.")
else:
    print(c, "є складеним числом.")

d = input("введіть рядок: ")
d1 = d[::-1]
print(d1)


e = int(input("введіть ціле число: "))

print("дільники числа", e, ":", e1=" ")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, e1=" ")



g = 0

for i in range(1, 101):
    g += i

print("сума всіх чисел від 1 до 100:", g)
