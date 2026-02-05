from py_cpf_cnpj.calculation import calculate_dv_cpf, calculate_dv_cnpj


def test_calculate_dv_cpf_known_value():
    # 901.494.926-00
    # "529.982.247-25"
    assert calculate_dv_cpf("529982247") == (2, 5)


def test_calculate_dv_cnpj_numeric():
    # 21.080.418/0001-26
    assert calculate_dv_cnpj("210804180001") == (2, 6)


def test_calculate_dv_cnpj_alphanumeric():
    # JH.ZMW.5S0/0001-84
    dv1, dv2 = calculate_dv_cnpj("JHZMW5S00001")
    assert isinstance(dv1, int)
    assert isinstance(dv2, int)
