# Python-API-Sympla

This program generates a report in JSON format using the Sympla API with Python.

## id.py

`id.py` retrieves all the IDs of the available events in the Sympla account.

## relatorio.py

`relatorio.py` (Portuguese for "Report") contains the main logic of the program. The `EventParticipant` class has methods to make requests and return filtered data from the events.

## main.py

In `main.py`, you need to put your API Key in the `token_user` variable. The main function creates a JSON file with all the information of all filtered events.
