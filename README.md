# API de Personagens (projeto de estudo)

Essa é uma API simples que eu fiz usando FastAPI pra treinar e me divertir programando.

A ideia foi criar tipo uma "mini wiki" com personagens de um ARG que eu gosto, com algumas informações básicas como história, status, aliados e inimigos.

Não é um projeto profissional nem nada do tipo, é só prática mesmo.

## O que dá pra fazer

* Ver todos os personagens
* Buscar um personagem pelo ID
* Ver quais personagens estão vivos
* Ver quais personagens estão mortos

## Rotas

* GET `/personagens` → lista todos
* GET `/personagens/{id}` → pega um personagem específico
* GET `/personagens/vivos` → lista os vivos
* GET `/personagens/mortos` → lista os mortos

## Tecnologias

* Python
* FastAPI

## Observações

* Os dados ficam só em memória (não tem banco de dados)
* É um projeto simples, feito mais pra aprender como funciona API
* A parte mais trabalhosa foi organizar as informações dos personagens

## Objetivo

Aprender FastAPI, entender melhor como funcionam rotas, parâmetros e respostas em JSON, e ao mesmo tempo fazer algo baseado em um tema que eu gosto.

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
uvicorn main:app --reload
```

Depois acesse:

* http://127.0.0.1:8000
* http://127.0.0.1:8000/docs
