from br_cpf_cnpj.normalize import normalize_cpf, normalize_cnpj


def test_normalize_cpf():
    assert normalize_cpf("123.456.789-09") == "12345678909"
    assert normalize_cpf("12345678909") == "12345678909"
    assert normalize_cpf("  123.456.789-09  ") == "12345678909"
    assert normalize_cpf(12345678909) == "12345678909"
    assert normalize_cpf("00A.123.456-78") == "0012345678"


def test_normalize_cpf_invalid():
    assert normalize_cpf(None) == ""


def test_normalize_cnpj_numeric():
    assert normalize_cnpj("12.345.678/0001-95") == "12345678000195"
    assert normalize_cnpj("12345678000195") == "12345678000195"
    assert normalize_cnpj("  12.345.678/0001-95  ") == "12345678000195"


def test_normalize_cnpj_alfanumeric():
    assert normalize_cnpj("AB.CD.EF/12-34") == "ABCDEF1234"
    assert normalize_cnpj("  AB.CD.EF/12-34  ") == "ABCDEF1234"
    