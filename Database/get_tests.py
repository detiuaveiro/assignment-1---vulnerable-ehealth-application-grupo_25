import requests
import json
from random import random

response_API = requests.get('https://diagnosisapi.azurewebsites.net/api/DDxItems/GetTests?AuthenticationID=DEMO_AuthenticationID')

data = response_API.text

data_json = json.loads(data)

for i in range(0, len(data_json)):
    with open('tests.sql', 'a') as f:
        cod_anal = i
        procedimento = data_json[i]['procedure'] 
        valor_min = float(data_json[i]['lowRangeValueSI'])
        valor_max = float(data_json[i]['highRangeValueSI'])
        unidades = data_json[i]['unitsTypeSI']
        resultado = (valor_min + valor_max) / (2*random())

        if unidades != 'DEMO':
            f.write(f'INSERT INTO Teste (Cod_Anal, Procedimento, Valor_Min, Valor_Max, Unidades, Resultado) VALUES ({cod_anal}, \'{procedimento}\', {valor_min}, {valor_max}, \'{unidades}\', {resultado:.{5}});\n')
