# 📦 br-cpf-cnpj
![Tests](https://github.com/RenanCampista/br-cpf-cnpj/actions/workflows/tests.yml/badge.svg)

A Python library for **CPF and CNPJ validation and generation**, with **support for the new alphanumeric CNPJ standard**.

---

## ✨ Features

- ✅ CPF validation  
- ✅ CNPJ validation (numeric and alphanumeric)  
- 🔢 Random CPF generator  
- 🔡 Random CNPJ generator (numeric or alphanumeric)  
- 🧪 Fully tested with pytest 
---

## 📥 Installation

```bash
pip install br-cpf-cnpj
```

---

## 🚀 Usage
### Validate CPF

```python
from br_cpf_cnpj import is_valid_cpf

is_valid_cpf("529.982.247-25")
# True

# Validate unmasked CPF
is_valid_cpf("55782724366")
# True

# Validate numeric CPF
is_valid_cpf(70714720178)
# True
```
**NOTE**: If the value is a number, it will be converted to a string and any leading zeros will be removed.


### Validate CNPJ

```python
from br_cpf_cnpj import is_valid_cnpj

# Validate numeric CNPJ
is_valid_cnpj("11.222.333/0001-81")
# True

# Validate alphanumeric CNPJ
is_valid_cnpj("2P.76B.MNX/0001-66")
# True

# Validate unmasked CNPJ
is_valid_cnpj("B4ESBMHS000102")
# True
```

### Generate Random CPF

```python
from br_cpf_cnpj import generate_random_cpf

cpf = generate_random_cpf(masked=True)
print(cpf)
# e.g., "123.456.789-09"

cpf_unmasked = generate_random_cpf(masked=False)
print(cpf_unmasked)
# e.g., "12345678909"
```

### Generate Random CNPJ

```python
from br_cpf_cnpj import generate_random_cnpj

# Generate numeric CNPJ
cnpj_numeric = generate_random_cnpj(alphanumeric=False, masked=True)
print(cnpj_numeric)
# e.g., "12.345.678/0001-95"

# Generate alphanumeric CNPJ
cnpj_alphanumeric = generate_random_cnpj(alphanumeric=True, masked=False)
print(cnpj_alphanumeric)
# e.g., "RSASKDDW000100"
```

---

## 🧠 How it works
### CPF
- Uses fixed weights (10 → 2, then 11 → 2)
- Applies the official modulo 11 algorithm
- Prevents invalid repeated-digit CPFs (e.g. `11111111111`)

### CNPJ (Alphanumeric)
- Supports digits (0–9) and uppercase letters (A–Z)
- Characters are converted using:
  `value = ord(char) - ord('0')`
- Weights cycle from 2 → 9

---

## Contributing
Contributions are very welcome!  
Feel free to open issues, suggest improvements, or submit pull requests.


## 📄 License
MIT License.

---

# Versão em Português
# 📦 br-cpf-cnpj
Uma biblioteca Python para **validação e geração de CPF e CNPJ**, com **suporte ao novo padrão de CNPJ alfanumérico**.

---

## ✨ Funcionalidades

- ✅ Validação de CPF
- ✅ Validação de CNPJ (numérico e alfanumérico)  
- 🔢 Gerador de CPF aleatório
- 🔡 Gerador de CNPJ aleatório (numérico ou alfanumérico)
- 🧪 Testes automatizados com pytest 

---

## 📥 Instalação

```bash
pip install br-cpf-cnpj
```

## 🚀 Uso
### Validar CPF

```python
from br_cpf_cnpj import is_valid_cpf

is_valid_cpf("529.982.247-25")
# True

# Validar CPF sem máscara
is_valid_cpf("55782724366")
# True

# Validar CPF numérico
is_valid_cpf(70714720178)
# True
```
**NOTA**: Se o valor for um número, ele será convertido para string e quaisquer zeros à esquerda serão removidos.


### Validar CNPJ

```python
from br_cpf_cnpj import is_valid_cnpj

# Validar CNPJ numérico
is_valid_cnpj("11.222.333/0001-81")
# True

# Validar CNPJ alfanumérico
is_valid_cnpj("2P.76B.MNX/0001-66")
# True

# Validar CNPJ sem máscara
is_valid_cnpj("B4ESBMHS000102")
# True
```

### Gerar CPF Aleatório

```python
from br_cpf_cnpj import generate_random_cpf

cpf = generate_random_cpf(masked=True)
print(cpf)
# e.g., "123.456.789-09"

cpf_unmasked = generate_random_cpf(masked=False)
print(cpf_unmasked)
# e.g., "12345678909"
```

### Gerar CNPJ Aleatório

```python
from br_cpf_cnpj import generate_random_cnpj

# Gerar CNPJ numérico
cnpj_numeric = generate_random_cnpj(alphanumeric=False, masked=True)
print(cnpj_numeric)
# e.g., "12.345.678/0001-95"

# Gerar CNPJ alfanumérico
cnpj_alphanumeric = generate_random_cnpj(alphanumeric=True, masked=False)
print(cnpj_alphanumeric)
# e.g., "RSASKDDW000100"
```

---

## 🧠 Como Funciona
### CPF
- Pesos fixos (10 → 2 e 11 → 2)
- Algoritmo módulo 11
- Rejeita CPFs inválidos com dígitos repetidos (e.g. `11111111111`)

### CNPJ (Alfanumérico)
- Aceita números (0–9) e letras (A–Z)
- Conversão baseada em valor ASCII:
  `value = ord(char) - ord('0')`
- Pesos cíclicos de 2 → 9

## Contribuindo
Contribuições são muito bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

## 📄 License
MIT License.
