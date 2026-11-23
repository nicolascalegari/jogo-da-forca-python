import random

PALAVRAS_POR_TEMA = {
    "programacao": [
        "algoritmo",
        "variavel",
        "dicionario",
        "excecao",
        "iteracao",
        "recursao",
        "polimorfismo",
        "encapsulamento",
    ],
    "tecnologia": [
        "servidor",
        "repositorio",
        "terminal",
        "compilador",
        "framework",
        "protocolo",
    ],
}


def escolher_palavra(tema: str = "programacao") -> tuple[str, str]:
    """Escolhe uma palavra aleatória do tema informado e retorna (palavra, tema)."""
    tema_normalizado = tema.lower().strip()
    if tema_normalizado not in PALAVRAS_POR_TEMA:
        tema_normalizado = "programacao"

    palavra = random.choice(PALAVRAS_POR_TEMA[tema_normalizado])
    return palavra.lower(), tema_normalizado