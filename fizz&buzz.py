fizz = int(input("Введіть число fizz: "))
buzz = int(input("Введіть число buzz: "))
n = int(input("Введіть число n: "))

for i in range(1, n + 1):
    if i % fizz == 0 and i % buzz == 0:
        print("FB", end=" ")
    elif i % fizz == 0:
        print("F", end=" ")
    elif i % buzz == 0:
        print("B", end=" ")
    else:
        print(i, end=" ")
