"""
Módulo de funções de processamento de imagens

Este módulo contém uma coleção de funções que realizam operações de processamento de imagens,
incluindo carregamento, conversão para tons de cinza, conversão para preto e branco, e salvamento das imagens.

Conteúdo:
    - carregar_imagem(): Carrega uma imagem e retorna os dados de pixel como uma lista RGB.
    - converter_para_tons_de_cinza(): Converte pixels RGB para tons de cinza usando uma fórmula personalizada.
    - converter_para_preto_branco(): Converte pixels em tons de cinza para preto e branco.
    - salvar_imagem(): Salva uma imagem a partir dos dados de pixel fornecidos.
"""

from PIL import Image

def carregar_imagem(image_path):
    """
    Carrega uma imagem e retorna os dados de pixel como uma lista RGB.

    Args:
        image_path (str): O caminho da imagem a ser carregada.

    Returns:
        tuple: Uma tupla contendo os dados de pixel da imagem, a largura e a altura da imagem.
        None: Se a imagem não puder ser carregada.
    """
    try:
        img = Image.open(image_path)
        pixels = list(img.convert("RGB").getdata())
        largura, altura = img.size
        return pixels, largura, altura
    except IOError:
        return None

def converter_para_tons_de_cinza(pixels):
    """
    Converte pixels RGB para tons de cinza usando uma fórmula personalizada.

    Args:
        pixels (list): Uma lista contendo os dados de pixel da imagem em formato RGB.

    Returns:
        list: Uma lista contendo os tons de cinza correspondentes aos pixels da imagem.
    """
    tons_cinza = [
        int(0.299 * r + 0.587 * g + 0.114 * b) for r, g, b in pixels
    ]
    return tons_cinza

def converter_para_preto_branco(tons_cinza, threshold=128):
    """
    Converte pixels em tons de cinza para preto e branco.

    Args:
        tons_cinza (list): Uma lista contendo os tons de cinza correspondentes aos pixels da imagem.
        threshold (int, optional): O limiar de tons de cinza para determinar se o pixel será preto ou branco. 
            O padrão é 128.

    Returns:
        list: Uma lista contendo os valores 0 (preto) ou 255 (branco) para cada pixel da imagem.
    """
    binarizado = [255 if pixel >= threshold else 0 for pixel in tons_cinza]
    return binarizado

def salvar_imagem(output_path, pixels, largura, altura, modo):
    """
    Salva uma imagem a partir dos dados de pixel fornecidos.

    Args:
        output_path (str): O caminho onde a imagem será salva.
        pixels (list): Uma lista contendo os dados de pixel da imagem.
        largura (int): A largura da imagem.
        altura (int): A altura da imagem.
        modo (str): O modo de formatação da imagem. Padrão é "L" para tons de cinza.

    Returns:
        None
    """
    img = Image.new(modo, (largura, altura))
    img.putdata(pixels)
    img.save(output_path)
