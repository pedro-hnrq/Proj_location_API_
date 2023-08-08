import re
from django.core.exceptions import ValidationError

def validate_zip_code(value):
    pattern = re.compile(r'^\d{5}-?\d{3}$')
    # Quantidade e formato de digito do CEP
    if not pattern.match(value):
        raise ValidationError('CEP inválido. Informe um CEP no formato "00000-000" ou "00000000" .')

    value = re.sub(r'\D', '', value)

    #Traço -
    if len(value) == 8:
        value = f'{value[:5]}-{value[5:]}'

    return value
    
def validate_state(value):
    pattern = re.compile(r'^[a-zA-ZÀ-ÿ\s]+$')
    if not pattern.match(value):
        raise ValidationError('Nome do estado inválido. Use apenas letras, acentos e espaços.')


def validate_name(value):
    pattern = re.compile(r'^[a-zA-ZÀ-ÿ\s]+$')
    if not pattern.match(value):
        raise ValidationError('O nome deve conter apenas letras e acentos.')

def validate_full_name(value):
    names = value.split()
    if len(names) < 2:
        raise ValidationError('Informe o nome e sobrenome separados por um espaço.')
    elif len(names) > 2:
        raise ValidationError('Informe apenas o primeiro nome e sobrenome separados por um espaço.')

def validate_age(value):
    if not isinstance(value, int) or value < 0:
        raise ValidationError('A idade deve ser um número inteiro não negativo.')
    elif value < 18:
        raise ValidationError('Usuário deve ser maior de 18 anos.')