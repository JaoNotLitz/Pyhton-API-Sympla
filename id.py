import requests
from datetime import datetime

class EventManager:
    def __init__(self, token_user):
        self.token_user = token_user
        self.url = 'https://api.sympla.com.br/public/v4/events'
        self.headers = {'s_token': self.token_user}

    def getIds(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            data = response.json()

            # Verifica se a solicitação foi bem-sucedida
            if response.status_code == 200:
                # Obtém a data e hora atuais
                current_datetime = datetime.now()

                # Filtra apenas os eventos publicados que ainda não terminaram
                current_events = [event for event in data['data'] if 
                                event.get('published') == 1 and 
                                datetime.strptime(event['end_date'], '%Y-%m-%d %H:%M:%S') > current_datetime]

                # Extrai os IDs dos eventos filtrados
                event_ids = [event['id'] for event in current_events]
                return event_ids
            else:
                print("Erro ao obter os eventos:", data['message'])

        except requests.exceptions.RequestException as e:
            print('Erro ao fazer a solicitação:', e)
