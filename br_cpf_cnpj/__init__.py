from .__version__ import __version__, __author__
from .validator import is_valid_cpf, is_valid_cnpj
from .generator import generate_random_cnpj, generate_random_cpf

__all__ = [
    '__version__',
    '__author__',
    'is_valid_cpf',
    'is_valid_cnpj',
    'generate_random_cpf',
    'generate_random_cnpj'
]