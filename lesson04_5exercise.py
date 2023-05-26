#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
def distribute_denominations(amount):
    denominations = [1, 5, 10, 20, 50, 100]  # Доступні номінали купюр
    distribution = {}

    for denomination in sorted(denominations, reverse=True):
        count = min(amount // denomination, 10)  # Максимальна кількість купюр даного номіналу
        if count > 0:
            distribution[denomination] = count
            amount -= count * denomination

    if amount == 0:
        return distribution
    else:
        return None  # Неможливо розподілити задану суму

# Приклад використання
amount = 128
result = distribute_denominations(amount)

if result:
    print(f"Розподіл дрібних купюр для суми {amount}:")
    for denomination, count in result.items():
        print(f"Номінал {denomination} грн: {count} шт.")
else:
    print(f"Неможливо розподілити суму {amount} дрібними купюрами.")
