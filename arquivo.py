import json


def carregar_produtos():

    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []


def salvar_produtos(produtos):

    with open("estoque.json", "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)