from .normalize import normalize_cnpj, normalize_cpf
from .calculation import calculate_dv_cnpj, calculate_dv_cpf


def is_valid_cnpj(value: str) -> bool:
    """Checks if the given value is a valid CNPJ number.

    Args:
        value (str): CNPJ value (numeric or alphanumeric).
    Returns:
        bool: True if the CNPJ number is valid, False otherwise.
    """
    cnpj = normalize_cnpj(value)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False
    
    base = cnpj[:12]
    dv1, dv2 = calculate_dv_cnpj(base)

    return (dv1, dv2) == (int(cnpj[12]), int(cnpj[13]))


def is_valid_cpf(value: str | int) -> bool:
    """Checks if the given value is a valid CPF number.

    Args:
        value (str | int): The CPF number to validate.
        NOTE: If the value is a number, it will be converted to a string and any leading zeros will be removed.
    Returns:
        bool: True if the CPF number is valid, False otherwise.
    """    
    cpf = normalize_cpf(value)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    base = cpf[:9]
    dv1, dv2 = calculate_dv_cpf(base)

    return (dv1, dv2) == (int(cpf[9]), int(cpf[10]))
