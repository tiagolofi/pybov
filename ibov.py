
from bs4 import BeautifulSoup
from requests import get
from re import findall, sub
from datetime import datetime

class Ibov(object):

	"""collecting info about a stock - backend api"""
	
	def __init__(self, name, type_):
		
		self.name = name
		self.type_ = type_
		self.base_url = f'''https://www.infomoney.com.br/cotacoes/b3/{self.type_}/{self.name}/'''
		
	def parse_numbers(self, text):

		return float(sub(',', '.', findall('[\d+\,\-]+', str(text[0]))[0]))

	def parse_numbers_table(self, text):

		return float(sub(',', '.', findall('[\d+\,\-]+', str(text))[0]))

	def connecting(self):

		if self.type_ not in ['bdr', 'indice', 'acao']:

			return {'error': 'categories not found.'}

		else:

			html = get(self.base_url)

			soup = BeautifulSoup(html.text, 'html.parser')

			return soup

	def get_info(self):
		
		try:

			data = self.connecting()

			table = data.select('.tables table td')

			self.parse_numbers_table(table[3])
			
			desc = data.select_one('.tables .description p').text
	
			infos = {
				'timestamp': int(datetime.now().timestamp()),
				'name': sub('-', ' ', self.name.rsplit('-', 1)[0].title()),
				'type_': self.type_.upper(),
				'symbol': self.name.rsplit('-', 1)[1].upper(),
				'description': desc,
				'price': self.parse_numbers(data.select('.value p')),
				'open_': self.parse_numbers_table(table[3]),
				'min_': self.parse_numbers(data.select('.minimo p')),
				'max_': self.parse_numbers(data.select('.maximo p'))
			}
	
			infos['spread_max_min'] = round(infos['max_'] - infos['min_'], 2)
			infos['variation'] = round((infos['price']/infos['open_'])-1, 4)
			infos['spread_price_open'] = round(infos['price'] - infos['open_'], 2)
	
			return infos

		except:
 
			return {'error': 'info not available'}

if __name__ == '__main__':

	print(Ibov(type_ = 'acao', name = 'banco-inter-bidi4').get_info())
