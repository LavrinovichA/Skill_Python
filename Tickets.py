num_tickets = int(input("Введите количество билетов: "))
ages = []
total_price = 0

for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    ages.append(age)
    if age < 18:
        total_price += 0
    elif age < 25:
        total_price += 990
    else:
        total_price += 1390

if num_tickets > 3:
    total_price *= 0.9

print("Общая стоимость билетов: ", total_price)
