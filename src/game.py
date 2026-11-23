from src.words import escolher_palavra

FORCA_ESTAGIOS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]

MAX_ERROS = len(FORCA_ESTAGIOS) - 1


def calcular_pontuacao(palavra: str, erros: int, venceu: bool) -> int:
    """Calcula a pontuação final com base na dificuldade da palavra e tentativas restantes."""
    if not venceu:
        return 0

    chances_restantes = MAX_ERROS - erros
    pontos_base = len(palavra) * 10
    bonus_chances = chances_restantes * 15
    return pontos_base + bonus_chances


def formatar_palavra_oculta(palavra: str, letras_corretas: set[str]) -> str:
    """Exibe as letras descobertas e '_' para as letras ainda não adivinhadas."""
    return " ".join(letra if letra in letras_corretas else "_" for letra in palavra)


def ler_palpite(letras_tentadas: set[str]) -> str:
    """Solicita e valida uma única letra ainda não tentada."""
    while True:
        entrada = input("Digite uma letra: ").strip().lower()

        if len(entrada) != 1 or not entrada.isalpha():
            print("Entrada invalida! Digite apenas uma letra (A-Z).")
            continue

        if entrada in letras_tentadas:
            print(f"Voce ja tentou a letra '{entrada}'. Escolha outra.")
            continue

        return entrada


def jogar_partida(tema: str = "programacao") -> tuple[bool, int, str]:
    """Executa uma partida completa e retorna (venceu, pontuacao, palavra_secreta)."""
    palavra, tema_escolhido = escolher_palavra(tema)
    letras_palavra = set(palavra)
    letras_corretas: set[str] = set()
    letras_erradas: set[str] = set()

    print(f"\n=== NOVA PARTIDA | Tema: {tema_escolhido.upper()} ===")

    while len(letras_erradas) < MAX_ERROS:
        print(FORCA_ESTAGIOS[len(letras_erradas)])
        print(f"Palavra: {formatar_palavra_oculta(palavra, letras_corretas)}")
        print(f"Chances restantes: {MAX_ERROS - len(letras_erradas)}/{MAX_ERROS}")

        if letras_erradas:
            print(f"Letras erradas: {', '.join(sorted(letras_erradas))}")

        palpite = ler_palpite(letras_corretas | letras_erradas)

        if palpite in letras_palavra:
            letras_corretas.add(palpite)
            print(f"Boa! A letra '{palpite}' esta na palavra.")
        else:
            letras_erradas.add(palpite)
            print(f"Que pena! A letra '{palpite}' nao esta na palavra.")

        if letras_palavra.issubset(letras_corretas):
            print(f"\nParabens! Voce acertou a palavra: '{palavra.upper()}'")
            pontuacao = calcular_pontuacao(palavra, len(letras_erradas), venceu=True)
            print(f"Pontuacao obtida: {pontuacao} pontos.")
            return True, pontuacao, palavra

    print(FORCA_ESTAGIOS[MAX_ERROS])
    print(f"\nFim de jogo! Suas chances acabaram. A palavra era: '{palavra.upper()}'")
    return False, 0, palavra