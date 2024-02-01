from db import *
# Загружаем элементы БД
db = read_db()
els = list(db.keys())

## Сайт
from dash import Dash, dcc, html, Input, Output,callback
app = Dash(__name__, title="SS14 Tools", update_title=None)


#### ФОРМАТ СТРАНИЦЫ ####

app.index_string = '''
<!DOCTYPE html>
<html>
<head>
	{%metas%}
	<title>{%title%}</title>
	{%favicon%}
	{%css%}
</head>
<body>



{%app_entry%}
<footer>
	{%config%}
	{%scripts%}
	{%renderer%}
</footer>
</body>
</html>
'''

###### ОФОРМЛЕНИЕ #######


# Форматируем список для красоты
def list_form(ll):
	global db

	formatted = []
	imgs = {'medicine': '💊',
					'chemicals': '🧪',
					'botany': '🪴',
					'drinks': '🍸'}

	for i in ll:
		if type(i) == int:
			formatted.append(i)
		elif db[i][1] in imgs:
			formatted.append(imgs[db[i][1]] + ' ' + i)
		else:
			formatted.append(i)

	return formatted

# 'background-color': 'rgb(27, 29, 30)', 'color': 'rgb(255,255,255)'

# Типо контейнер для всего
# [
# Div,
# Div
# ]
app.layout = html.Div([

# Соцсети и исходный код + название
html.Div([

html.Div([
html.Img(src='assets/favicon.ico', width='50px', height='auto', style={'padding':10}),
html.Div(children='''SS14 Tools'''
, style={'color':'rgb(255,255,255)', 'font-weight': 'bold', 'font-size': '1.5rem'})
], style={'display': 'flex', 'flex-wrap': 'wrap', 'align-items': 'center', 'flex': 1}),

html.Div([
dcc.Link('Discord',href='https://discord.gg/VxHbM3cedQ'),
dcc.Link('Telegram',href='https://t.me/ss14tools')
], style={'display': 'flex', 'flex-wrap': 'wrap', 'align-items': 'center', 'flex': 1}),

#Пустой контейнер (для правильного отображения)
html.Div(style={'flex':1})

], style={'background-color': '#161819', 'margin': -8, 'display': 'flex', 'flexDirection': 'row', 'justify-content': 'flex-start'}),

# Название + объём + вывод
html.Div([
# Название + объём
html.Div([
	# Реакция
	html.Div([
		dcc.Dropdown(list_form(els), id='reaction', placeholder="Реакция", maxHeight=500,
		style={'font-size': '120%', 'font-family': 'NotaSans'})
	], style={'flex': 4}),

	# Объём
	html.Div([
		dcc.Dropdown(list_form([30, 50, 100, 300, 1000]), 100, id='amount', clearable=False, searchable=False
			, style={'font-family': '"Source Sans Pro", sans-serif', 'font-size': '120%'}) #, 'background-color': 'rgb(27, 29, 30)'})
	], style={'flex': 1, 'padding-left': 25})

], style={'display': 'flex', 'flexDirection': 'row'}),

	# Вывод
	html.Div(id='output', style={'text-align': 'center', 'padding-left': '15%', 'padding-right': '15%'})

], style={'padding': '5%', 'margin-left': '30%', 'margin-right': '30%'})

])
# vh - высота окна, vw - ширина окна
#
# 'background-color': '#242829',
# padding - отступ
#    [#####]
# margin - сужение
#     [###]
#########################





####### ЛОГИКА ##########

from calc import *

@callback(
	Output('output', 'children'),
	Input('reaction', 'value'),
	Input('amount', 'value')
)
def update_output(reaction, amount):
	if reaction:
		reaction = reaction[2:]
		comps, res = calc(reaction, amount, main = True)

		# Форматирование для HTML
		result = []
		for i in comps:
			result.append( html.Div(i + ': ' + str(comps[i])
, style={'background-color': 'rgb(213, 193, 86)', 'color': '#ffffff', 'margin-top': 10, 'border-radius': 10, 'padding': 15, 'font-family': '"Source Sans Pro", sans-serif', 'font-size': '120%'}) )

		# Выходное вещество
		result.append( html.Div(f'{reaction}: {res}'
, style={'background-color': 'rgb(61, 164, 113)', 'color': '#ffffff', 'margin-top': 10, 'border-radius': 10, 'padding': 15, 'font-family': '"Source Sans Pro", sans-serif', 'font-size': '120%'}) )


		return result


#########################



if __name__ == '__main__':
#	app.run(debug=True)
	app.run(debug=False)
