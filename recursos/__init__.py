"""
Pacote Redução de Dimensionamento de Imagens

Este pacote contém os módulos e funções necessários para realizar a redução de dimensionamento de imagens.
"""

from .funcoes import carregar_imagem
from .funcoes import converter_para_tons_de_cinza
from .funcoes import converter_para_preto_branco
from .funcoes import salvar_imagem

__all__ = ['carregar_imagem', 'converter_para_tons_de_cinza', 'converter_para_preto_branco', 'salvar_imagem']
