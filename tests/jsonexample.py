import json

data = {}

data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joaquin',
    'last_name': 'Hinners',
    'age': 21,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

""" with open('data.json', 'w') as file:
    json.dump(data, file, indent=4) """



with open('data.json') as file:
    data = json.load(file)
    print(f"data is of type: {type(data)}")

    for client in data['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')
        print(client.keys())



