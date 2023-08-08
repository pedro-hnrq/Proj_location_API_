import requests

def get_address_info_by_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    data = response.json()
    if 'erro' in data:
        return None
    return {
        'logradouro': data.get('logradouro', ''),
        'bairro': data.get('bairro', ''),
        'cidade': data.get('localidade', ''),
        'complemento': data.get('complemento', ''),
        'uf': data.get('uf', ''),
    }