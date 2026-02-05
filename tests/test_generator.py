from br_cpf_cnpj.generator import generate_random_cpf, generate_random_cnpj
from br_cpf_cnpj.validator import is_valid_cpf, is_valid_cnpj


def test_generate_random_cpf():
    cpf = generate_random_cpf()
    assert len(cpf) == 11
    assert is_valid_cpf(cpf)


def test_gerate_random_cpf_masked():
    cpf = generate_random_cpf(masked=True)
    assert len(cpf) == 14  # Format: XXX.XXX.XXX-XX
    assert is_valid_cpf(cpf)


def test_generate_random_cnpj_alphanumeric():
    cnpj = generate_random_cnpj()
    assert len(cnpj) == 14
    assert is_valid_cnpj(cnpj)


def test_generate_random_cnpj_numeric():
    cnpj = generate_random_cnpj(alphanumeric=False)
    assert cnpj.isdigit()
    assert is_valid_cnpj(cnpj)


def test_generate_random_cnpj_masked():
    cnpj = generate_random_cnpj(masked=True)
    assert len(cnpj) == 18  # Format: XX.XXX.XXX/XXXX-XX
    assert is_valid_cnpj(cnpj)
    