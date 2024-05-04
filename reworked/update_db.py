from parse import *
from calc import *
from db import *

print('''1. Обновить всё.
2. Пересчитать рецепты.
''')
inp = input(">> ")
print('\n')

vols = [30, 50, 100]
if inp == '1':
	print('Парсим и обрабатываем данные...')
	# Загружаем локализацию
	locales_url = ['medicine', 'chemicals']
	locales = load_locales(locales_url)

	# Загружаем сырые рецепты
	recipes_url = ['medicine']
	raw_recipes = load_recipes(recipes_url)

	# Локализируем
	recipes = localize(raw_recipes, locales)

	save(recipes, 'raw_db.json')
	print('Сохранены минимальные рецепты в raw_db.json')
	print('Выполняем предрасчёты...')

	for i in vols:
		precalc = calc_all(recipes, i)
		save(precalc, f'{i}_calc.json')
		print(f'Данные сохранены в {i}_calc.json')
elif inp == '2':
	print('Выполняем расчёты...')
	recipes = load('raw_db.json')
	for i in vols:
		precalc = calc_all(recipes, i)
		save(precalc, f'{i}_calc.json')
		print(f'Данные сохранены в {i}_calc.json')
else:
	exit()

print("ГОТОВО.")
