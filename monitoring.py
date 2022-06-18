
from requests import get
from json import dump, load
# from pandas import DataFrame
from time import sleep
# from matplotlib import pyplot as graph
from os import remove
from tqdm import tqdm
from plyer import notification

class Monitoring(object):

	"""Monitoring"""
	
	def __init__(self, name, type_, interval, n_query):
				
		self.NAME = name
		self.TYPE = type_
		self.INTERVAL = interval
		self.N_QUERY = n_query
		self.PATH_DIR = 'monitoring/'		

	def do_query(self):
	
		url = f'''https://apibov.herokuapp.com/info?name={self.NAME}&type={self.TYPE}'''
	
		response = get(url)
	
		data = response.json()
	
		return data
	
	def save_data_query(self, data):
	
		try:
	
			with open(self.PATH_DIR + self.NAME + '.json', 'r') as db:
		
				file = load(db)
	
			with open(self.PATH_DIR + self.NAME + '.json', 'w', encoding = 'utf-8') as db:
	
				dump(file + [data], db, indent = 2, ensure_ascii = True)
	
		except: 
	
			with open(self.PATH_DIR + self.NAME + '.json', 'w', encoding = 'utf-8') as db:
	
				dump([data], db, indent = 2, ensure_ascii = True)
	
	def apply_routine_query(self, target):
	
		count = 0
	
		pb = tqdm(total = self.N_QUERY)

		while True:
		
			if count < self.N_QUERY:
		
				data = self.do_query()

				if data['price'] <= target:

					notification.notify(
						title = 'Meta de preço alcançada!',
						message = 'Preço atual: ' + str(data['price']),
						timeout = 5
					)

				self.save_data_query(data)
		
				sleep(self.INTERVAL)
		
				count += 1

				pb.update(count)

			else:
		
				break
	
	# def store_in_dataframe(self):
	# 
	# 	with open(self.PATH_DIR + self.NAME + '.json', 'r') as db:
	# 	
	# 		file = load(db)
	# 
	# 	dataframe = DataFrame(file)
	# 
	# 	return dataframe
	
	# def do_graph(self, variable):
	# 
	# 	df = self.store_in_dataframe()
	# 
	# 	x = df['timestamp']
	# 
	# 	y = df[variable]
	# 
	# 	graph.plot(x, y)
	# 
	# 	graph.show()

	def delete_m(self):

		try:

			remove(self.PATH_DIR + self.NAME + '.json')

		except:

			pass

if __name__ == '__main__':

	m = Monitoring(interval = 5, n_query = 5, name = 'magazine-luiza-mglu3', type_ = 'acao')

	m.delete_m()

	m.apply_routine_query(target = 2.38)

	# m.do_graph(variable = 'price')
