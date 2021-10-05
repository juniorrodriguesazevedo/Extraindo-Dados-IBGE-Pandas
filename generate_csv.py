import requests
import pandas as pd
from utils.initials import states

class GenerateCSV:
    def export_csv(self, data, uf):
        formatted_data = self._formatted_data(data)
        csv = pd.DataFrame(formatted_data)
        csv.to_csv(f'csv/{uf}.csv', header=['Cidade', 'Habitantes'], index=False)
        print('Arquivo CSV criado com sucesso!')

    def _formatted_data(self, data):
        base = data[0]['resultados'][0]['series']
        list_city = []
        list_population = []

        for x in range(0, len(base)):
            list_city.append(base[x]['localidade']['nome'])
            list_population.append(base[x]['serie']['2021'])
        
        response = list(zip(list_city, list_population))

        return response

    def get_state(self, state):
        states
        cod = states.get(state)
        api = f'https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2021/variaveis/9324?localidades=N6[N3[{cod}]]'
        response = requests.get(api)
        
        return response.json()         