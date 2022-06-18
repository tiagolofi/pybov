
# Infos sobre a Bolsa Brasileira

Webscrapping das informações do site do Invest***

Apreciem.

### Query e Args

[Exemplo de Query](https://apibov.herokuapp.com/info?name=magazine-luiza-mglu3&type=acao)

Args usadas: 
- "name": "magazine-luiza-mglu3";
- "type": "acao" ("bdr" ou "acao")

### Response

- description: detalhes sobre a empresa;
- max_: máxima;
- min_: mínima;
- name: nome da empresa;
- open_: abertura;
- price: preço atual;
- spread_max_min: variação (máx - min);
- spread_price_open: variação absoluta;
- symbol: ticker da empresa;
- timestamp: timestamp (int)
- type_: ACAO ou BDR
- variation: variação
