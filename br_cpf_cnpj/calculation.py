def calculate_dv_cpf(base: str) -> tuple[int, int]:
    """Calculates the two verification digits (DVs) for a given CPF base.
    
    Args:
        base (str): The first 9 digits of the CPF number.
    Returns:
        tuple[int, int]: A tuple containing the two calculated verification digits.
    """
    if len(base) != 9 or not base.isdigit():
        raise ValueError("CPF base must have exactly 9 digits")

    weight = 10
    total = 0
    for digit in base:
        total += int(digit) * weight
        weight -= 1

    resto = total % 11
    dv1 = 0 if resto < 2 else 11 - resto

    weight = 11
    total = 0
    for digit in base + str(dv1):
        total += int(digit) * weight
        weight -= 1

    resto = total % 11
    dv2 = 0 if resto < 2 else 11 - resto

    return dv1, dv2


def calculate_dv_cnpj(base: str) -> tuple[int, int]:
    """Calculates the two verification digits (DVs) for a given CNPJ base.

    Args:
        base (str): The first 12 characters of the CNPJ number.
    Returns:
        tuple[int, int]: A tuple containing the two calculated verification digits.
    """
    if len(base) != 12:
        raise ValueError("CNPJ base must have exactly 12 characters")

    weight = 2
    total = 0
    for i in range(11, -1, -1):
        total += (ord(base[i]) - ord('0')) * weight
        weight = weight + 1 if weight < 9 else 2

    resto = total % 11
    dv1 = 0 if resto < 2 else 11 - resto

    weight = 2
    total = 0
    base_dv1 = base + str(dv1)
    for i in range(12, -1, -1):
        total += (ord(base_dv1[i]) - ord('0')) * weight
        weight = weight + 1 if weight < 9 else 2

    resto = total % 11
    dv2 = 0 if resto < 2 else 11 - resto

    return dv1, dv2
