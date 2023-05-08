tickets = int(input("Введите количество билетов: "))
price = 0
for i in range(tickets):
    age = int(input(f"Введите возраст посетителя №{i+1}: "))
    if age < 18:
        tickprice = 0
    elif 18 <= age < 25:
        tickprice = 990
    else:
        tickprice = 1390
    price += tickprice

if tickets > 3:
    price *= 0.9

print(f"Общая стоимость билетов: {price} руб.")
