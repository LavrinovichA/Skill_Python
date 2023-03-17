money = float(input('Введите сумму, которую планируете положить под проценты\n'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [round((x * money)/100, 3) for x in per_cent.values()]
print(deposit) #Вывод по заданию

print(dict(zip(per_cent.keys(), deposit))) #Вывод депозитов по банкам (более читаемо)

deposit_in_banks = list(per_cent.keys())[deposit.index(max(deposit))]
print('Максимальная сумма, которую вы можете заработать — ', max(deposit), '\nВ банке - ', deposit_in_banks) #вторая часть максимальный депозит

