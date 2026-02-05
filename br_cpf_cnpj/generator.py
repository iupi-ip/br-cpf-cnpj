import random
import string

from .calculation import calculate_dv_cpf, calculate_dv_cnpj


def generate_random_cpf(masked: bool = False) -> str:
    """
    Generates a valid random CPF number (only digits).

    Args:
        masked (bool): If True, generates masked CPF (with dots and hyphen).
                       If False, generates numeric-only CPF.
    Returns:
        str: A valid CPF with 11 digits.
    """
    base = ''.join(str(random.randint(0, 9)) for _ in range(9))

    dv1, dv2 = calculate_dv_cpf(base)

    if masked:
        return f"{base[:3]}.{base[3:6]}.{base[6:9]}-{dv1}{dv2}"
    return f"{base}{dv1}{dv2}"


def generate_random_cnpj(masked: bool = False, alphanumeric: bool = True) -> str:
    """
    Generates a valid random CNPJ number.

    Args:
        masked (bool): If True, generates masked CNPJ (with dots, slashes, and hyphen).
                       If False, generates numeric-only CNPJ.
        alphanumeric (bool): If True, generates alphanumeric CNPJ.
                             If False, generates numeric-only CNPJ.

    Returns:
        str: A valid CNPJ with 14 characters.
    """
    if alphanumeric:
        charset = string.digits + string.ascii_uppercase
    else:
        charset = string.digits

    base = ''.join(random.choice(charset) for _ in range(12))

    dv1, dv2 = calculate_dv_cnpj(base)

    if masked:
        return f"{base[:2]}.{base[2:5]}.{base[5:8]}/{base[8:12]}-{dv1}{dv2}"
    return f"{base}{dv1}{dv2}"
