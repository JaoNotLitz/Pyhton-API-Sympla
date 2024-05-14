import json
from relatorio import EventParticipantManager
from id import EventManager
print("Relatório de Eventos")
token_user = 'Your API Key Here'
ids = EventManager(token_user).getIds()

# Nome do arquivo de saída
output_file = 'relatorio_eventos.json'

relatorio_eventos = {"Relatório de Eventos": []}

for event_id in ids:
    manager = EventParticipantManager(token_user, event_id)
    event_name = manager.get_event_name()
    if event_name:
        event_info = {
            "Evento": event_name,
            "Total de participantes": 0,
            "Preço total das vendas": 0,
            "Ingressos": {}
        }
        count_total, total_sales_price, ticket_count = manager.get_participants_info()
        event_info["Total de participantes"] = count_total
        event_info["Preço total das vendas"] = total_sales_price
        event_info["Ingressos"] = {ticket: count for ticket, count in ticket_count.items()}
        relatorio_eventos["Relatório de Eventos"].append(event_info)

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(relatorio_eventos, file, ensure_ascii=False, indent=4)
print(f"Relatório de eventos salvo em {output_file}")