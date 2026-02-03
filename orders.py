import json

with open("translator.json", "r") as my_file:
    orders = json.load(my_file)


print('1. Какой номер самого дорого заказа за июль?')

max_price = 0
max_order = ''

for order_num, orders_data in orders.items():
    price = orders_data['price']

    if price > max_price:
        max_order = order_num
        max_price = price

print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')


print('2. Какой номер заказа с самым большим количеством товаров?')

max_quantity = 0
max_order = ''

for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']

    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity

print(f'Номер заказа с самым большим количеством товаров: {max_order}, количество товаров: {max_quantity}')


# print('3. В какой день в июле было сделано больше всего заказов?')
#
# from datetime import datetime
#
# max_date = ''
# sum_order = 0
#
# for order_num, orders_data in orders.items():
#     date = orders_data['date']
#
#     all_date = date.sort()
#
# цикл по датам (если дата = ... считаем кол-во заказов)
# условный оператор для сопоставления даты и кол-ва заказов
# метод для макс числа
#
# print(f'Больше всего заказов было сделано на дату: {max_date}, количество заказов: {sum_order}')


print('4. Какой пользователь сделал самое большое количество заказов за июль?')

all_users = []
max_user = ''
max_order = ''

for order_num, orders_data in orders.items():
    user_id = orders_data["user_id"]

    all_users.append(user_id)

    count_users = all_users.count(user_id)
    # print(f"{user_id}: {count_users}")  #вероятно, допущена ошибка: каждый пользователь встречается один раз

    max_count = max({count_users})

    if count_users == max_count:
        max_user = user_id
        max_order = max_count

print(f'Клиент, сделавший самое большое количество заказов: {max_user}, количество заказов: {max_count}')


print('5. У какого пользователя самая большая суммарная стоимость заказов за июль?')

all_users = []
all_prices = []
max_user = ''
max_price = 0

for order_num, orders_data in orders.items():
    user_id = orders_data["user_id"]
    price = orders_data["price"]

    all_users.append(user_id)
    all_prices.append(price)

    if user_id in all_users:
        print(f"{user_id}: {price}")

    best_price = max(all_prices)

    if price == best_price:
        max_user = user_id
        max_price = price

print(f'Клиент с самой большой стоимостью заказов: {max_user}, сумма: {max_price}')


print('6. Какая средняя стоимость заказа была в июле?')

all_orders = []
all_prices = []

for order_num, orders_data in orders.items():
    all_orders.append(order_num)
    all_prices.append(orders_data["price"])

orders = len(all_orders)
prices = (sum(all_prices))
price_count = prices // orders
print (f'Средняя месячная стоимость заказа: {price_count}')


print('7. Какая средняя стоимость товаров в июле?')

all_quantitys = []
all_prices = []

for order_num, orders_data in orders.items():
    all_quantitys.append(orders_data["quantity"])
    all_prices.append(orders_data["price"])

quantitys = sum(all_quantitys)
prices = (sum(all_prices))
price_count = prices // quantitys
print (f'Средняя месячная стоимость товаров: {price_count}')