
from monitoring import Monitoring

while True:

	nome = input('Nome e ticker da empresa:\n')

	tipo = input('Tipo ("acao" ou "bdr"):\n')

	intervalo = int(input('Intervalo de tempo em segundos:\n'))
	
	n_query = int(input('Quantidade de requisições:\n'))
	
	# var = input('Variável do gráfico:\n')
	
	preco = round(float(input('Preço Alvo:\n')), 2)

	m = Monitoring(interval = intervalo, n_query = n_query, name = nome, type_ = tipo)

	m.delete_m()

	m.apply_routine_query(target = preco)

	# m.do_graph(variable = var)
