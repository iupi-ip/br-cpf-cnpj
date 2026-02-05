import re


def normalize_cpf(value: str | int) -> str:
    """Normalizes a CPF number by removing any non-digit characters and leading zeros."""
    if not value or not isinstance(value, (str, int)):
        return ''
    return re.sub(r'\D', '', str(value))


def normalize_cnpj(value: str) -> str:
    """Normalizes a CNPJ by removing formatting characters and uppercasing letters."""
    if not value or not isinstance(value, str):
        return ''
    return re.sub(r'[^A-Za-z0-9]', '', value).upper()
