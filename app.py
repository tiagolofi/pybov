
from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec, Response
from typing import Optional
from pydantic import BaseModel
from ibov import Ibov

# spec

app = Flask(__name__)
spec = FlaskPydanticSpec(
	'flask',
	version='v1', 
	title = 'API de Coleta de Preços da Bolsa em Tempo Real'
)
spec.register(app)

# contratos

class ErrorMessage(BaseModel):
	error: str

class Infos(BaseModel):
	timestamp: Optional[int] = None
	name: Optional[str] = None
	type_: Optional[str] = None
	symbol: Optional[str] = None
	description: Optional[str] = None
	price: Optional[float] = None
	open_: Optional[float] = None
	min_: Optional[float] = None
	max_: Optional[float] = None
	spread_max_min: Optional[float] = None
	variation: Optional[float] = None
	spread_price_open: Optional[float] = None

# recursos

@app.get('/info')
@spec.validate(
	resp=Response(
		HTTP_200=Infos,
		HTTP_403=ErrorMessage
	),
	tags=['Info']
)
def info():
	
	"""Coleta informações de um ativo"""

	args = request.args

	type_ = args.get('type', default='', type=str)
	
	name = args.get('name', default='', type=str)

	response = Ibov(type_ = type_, name = name)

	return jsonify(response.get_info())
