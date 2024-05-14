import requests

class EventParticipantManager:
    def __init__(self, token_user, event_id):
        self.token_user = token_user
        self.event_id = event_id
        self.url_event_info = f'https://api.sympla.com.br/public/v3/events/{self.event_id}'
        self.url_participants = f'https://api.sympla.com.br/public/v3/events/{self.event_id}/participants'
        self.headers = {'s_token': self.token_user}

    def get_event_info(self):
        try:
            response_event_info = requests.get(self.url_event_info, headers=self.headers)
            data_event_info = response_event_info.json()
            event_info = data_event_info['data'] if 'data' in data_event_info else None
            return event_info
        except requests.exceptions.RequestException as e:
            print('Erro ao obter informações do evento:', e)

    def get_event_name(self):
        event_info = self.get_event_info()
        if event_info:
            event_name = event_info['name']
            event_start_date = event_info['start_date']
            event_end_date = event_info['end_date']
            return f"{event_name} (Início: {event_start_date}, Término: {event_end_date})"
        else:
            return "Evento não encontrado"

    def get_participants_info(self):
        try:
            total_participants = []
            page_size = 100
            page_number = 1
            while True:
                params = {'page_size': page_size, 'page': page_number}
                response_participants = requests.get(self.url_participants, headers=self.headers, params=params)
                data_participants = response_participants.json()
                if 'data' not in data_participants or not data_participants['data']:
                    break
                total_participants.extend(data_participants['data'])
                if data_participants['pagination']['has_next']:
                    page_number += 1
                else:
                    break

            ticket_count = {}
            count_total = 0
            total_sales_price = 0

            for participant in total_participants:
                ticket_name = participant['ticket_name'].lower()
                ticket_price = participant['ticket_sale_price']

                if 'casais' in ticket_name:
                    ticket_count[ticket_name] = ticket_count.get(ticket_name, 0) + 2
                    count_total += 2
                elif 'famílias' in ticket_name:
                    ticket_count[ticket_name] = ticket_count.get(ticket_name, 0) + 3
                    count_total += 3
                else:
                    ticket_count[ticket_name] = ticket_count.get(ticket_name, 0) + 1
                    count_total += 1

                total_sales_price += ticket_price

            return count_total, total_sales_price, ticket_count

        except requests.exceptions.RequestException as e:
            print('Erro ao obter informações dos participantes:', e)

