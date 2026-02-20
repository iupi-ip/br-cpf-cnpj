from br_cpf_cnpj.validators import is_valid_cpf, is_valid_cnpj


def test_valid_cpf():
    assert is_valid_cpf("529.982.247-25") is True


def test_invalid_cpf():
    assert is_valid_cpf("111.111.111-11") is False


def test_invalid_cpf_length():
    assert is_valid_cpf("529.982.247") is False


def test_valid_cnpj_numeric():
    assert is_valid_cnpj("11.222.333/0001-81") is True


def test_valid_cnpj_alphanumeric():
    assert is_valid_cnpj("2P.76B.MNX/0001-66") is True


def test_invalid_cnpj():
    assert is_valid_cnpj("AAAAAAAAAAAAAA") is False


def test_invalid_cnpj_length():
    assert is_valid_cnpj("11.222.333/0001") is False
    