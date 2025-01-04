"""
Projeto Redução de Dimensionamento de Imagens

Objetivo:
    Implementar um algoritmo de binarização de imagens coloridas, transformando 
    uma ou mais imagens coloridas em níveis de cinza (0 a 255) e posteriormente 
    binarizá-las em preto e branco.

Descrição:
    Este projeto utiliza a biblioteca Pillow para carregar e processar as imagens.
    As imagens coloridas são convertidas para tons de cinza e, em seguida, para preto e branco.
    Os resultados são salvos em pastas separadas.

Requisitos:
    - Python >= 3.12
    - Biblioteca Pillow >= 11.1.0
"""

import os
from recursos.funcoes import carregar_imagem
from recursos.funcoes import converter_para_tons_de_cinza
from recursos.funcoes import converter_para_preto_branco
from recursos.funcoes import salvar_imagem


# Definir os caminhos das pastas
PASTA_COLORIDAS = "C:/Users/danie/OneDrive/Documentos/Cursos/ML/3-Algoritmos_de_Treinamento_em_Machine_Learning/Projeto/Reducao-de-Dimensionamento-de-Imagens/Imagens-Coloridas"
PASTA_TONS_CINZA = "C:/Users/danie/OneDrive/Documentos/Cursos/ML/3-Algoritmos_de_Treinamento_em_Machine_Learning/Projeto/Reducao-de-Dimensionamento-de-Imagens/Imagens-TonsCinza"
PASTA_PRETO_BRANCO = "C:/Users/danie/OneDrive/Documentos/Cursos/ML/3-Algoritmos_de_Treinamento_em_Machine_Learning/Projeto/Reducao-de-Dimensionamento-de-Imagens/Imagens-PretoBranco"

def processar_imagens():
    """
    Processa todas as imagens da pasta de entrada e salva os resultados nas pastas de saída.

    Certifica-se de que as pastas de saída existem, lista todas as imagens na pasta de entrada,
    carrega a imagem e obtém os pixels, converte para tons de cinza e salva a imagem,
    e, em seguida, converte para preto e branco e salva a imagem.

    Args:
        Nenhum

    Returns:
        Nenhum
    """
    # Certificar-se de que as pastas de saída existem
    os.makedirs(PASTA_TONS_CINZA, exist_ok=True)
    os.makedirs(PASTA_PRETO_BRANCO, exist_ok=True)

    # Listar todas as imagens na pasta de entrada
    for arquivo in os.listdir(PASTA_COLORIDAS):
        caminho_entrada = os.path.join(PASTA_COLORIDAS, arquivo)

        # Verificar se é uma imagem suportada
        if arquivo.lower().endswith((
            '.bmp', '.jpg', '.jpeg', '.png', '.tiff', '.webp')):
            print(f"Processando: {arquivo}")

            # Carregar imagem e obter pixels
            pixels, largura, altura = carregar_imagem(caminho_entrada)

            # Converter para tons de cinza
            tons_cinza = converter_para_tons_de_cinza(pixels)
            caminho_saida_cinza = os.path.join(PASTA_TONS_CINZA, arquivo)
            salvar_imagem(caminho_saida_cinza, tons_cinza, largura, altura, "L")

            # Converter para preto e branco
            binarizado = converter_para_preto_branco(tons_cinza)
            caminho_saida_pb = os.path.join(PASTA_PRETO_BRANCO, arquivo)
            salvar_imagem(caminho_saida_pb, binarizado, largura, altura, "L")

            print(f"Imagens salvas: {caminho_saida_cinza}, {caminho_saida_pb}")
        else:
            print(f"Arquivo ignorado (não é uma imagem suportada): {arquivo}")

if __name__ == "__main__":
    processar_imagens()
