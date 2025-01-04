# <h1 align="center">Redução de Dimensionamento de Imagens</h1>

![Python](https://img.shields.io/badge/language-Python-blue.svg)
![Versão](https://img.shields.io/badge/version-1.0.0-blue.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/Danieltandrade/Reducao-de-Dimensionamento-de-Imagens)
![GitHub](https://img.shields.io/github/license/Danieltandrade/Reducao-de-Dimensionamento-de-Imagens.svg)
![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/Danieltandrade/Reducao-de-Dimensionamento-de-Imagens)

## Introdução

Este projeto é uma implementação de um algoritmo de binarização de imagens coloridas, que transforma imagens coloridas em níveis de cinza e posteriormente em preto e branco.

## Objetivo

O objetivo deste projeto é criar um algoritmo que possa reduzir a dimensionalidade de imagens coloridas, tornando-as mais fáceis de processar e armazenar.

## Funcionalidades

* Leitura de imagens coloridas
* Conversão de imagens coloridas para tons de cinza
* Conversão de imagens em tons de cinza para preto e branco
* Salvar imagens processadas em pastas separadas

## Requisitos

* Python >= 3.12
* Pillow >= 11.1.0

## Instalação

1. Clone o repositório: `git clone https://github.com/Danieltandrade/Reducao-de-Dimensionamento-de-Imagens.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o script: `python main.py`

## Uso

1. Coloque as imagens coloridas que deseja processar na pasta `Imagens-Coloridas`.
2. Execute o script na pasta do projeto: `python main.py`.
3. As imagens processadas serão salvas nas pastas `Imagens-TonsCinza` e `Imagens-PretoBranco`.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma ideia ou sugestão para melhorar o projeto, por favor, abra uma __issue__ ou envie um pull __request__.

## Licença

Este projeto é licenciado sob a licença __GNU GENERAL PUBLIC LICENSE V3__. Veja o arquivo `LICENSE` para mais detalhes.

## Conclusão

O projeto demonstrou um bom funcionamento para reduzir a dimensionalidade de imagens coloridas, permitindo que eles sejam processados e armazenados de forma mais eficiente. Ele pode ser usado como uma ferramenta para ajudar a lidar com imagens com alta dimensionalidade, como imagens de alta resolução ou imagens com muitos pixels coloridos, com isso tornando-as mais fáceis de processar e armazenar.
