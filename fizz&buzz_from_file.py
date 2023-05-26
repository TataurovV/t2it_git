def fizzbuzz(fizz, buzz, n):
    result = []
    for num in range(1, n + 1):
        if num % fizz == 0 and num % buzz == 0:
            result.append("FB")
        elif num % fizz == 0:
            result.append("F")
        elif num % buzz == 0:
            result.append("B")
        else:
            result.append(str(num))
    return result

# Відкриваємо файл для читання
with open('input.txt', 'r') as file:
    for line in file:
        # Розділяємо рядок на числа
        fizz, buzz, n = map(int, line.strip().split())
        
        # Викликаємо функцію fizzbuzz
        output = fizzbuzz(fizz, buzz, n)
        
        # Виводимо результат
        print(" ".join(output))
