from src.game import jogar_partida
from src.ranking import obter_ranking_ordenado, salvar_pontuacao


def exibir_ranking() -> None:
    """Exibe o ranking ordenado do maior para o menor."""
    ranking = obter_ranking_ordenado()
    print("\n================ RANKING ================")

    if not ranking:
        print("Nenhuma pontuacao registrada ainda.")
        print("=========================================")
        return

    for posicao, registro in enumerate(ranking, start=1):
        nome = registro.get("nome", "Jogador")
        pontos = registro.get("pontos", 0)
        palavra = registro.get("palavra", "-")
        print(f"{posicao:>2}o | {nome:<18} | {pontos:>4} pts | Palavra: {palavra}")

    print("=========================================")


def menu_principal() -> None:
    """Loop principal do menu no terminal."""
    while True:
        print("\n=== JOGO DA FORCA ===")
        print("1. Jogar (Programacao)")
        print("2. Jogar (Tecnologia)")
        print("3. Ver Ranking")
        print("4. Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao in ("1", "2"):
            tema = "programacao" if opcao == "1" else "tecnologia"
            _, pontuacao, palavra = jogar_partida(tema=tema)
            nome = input("\nDigite seu nome para salvar no ranking: ")
            salvar_pontuacao(nome=nome, pontos=pontuacao, palavra=palavra)
            print("Pontuacao salva com sucesso!")
        elif opcao == "3":
            exibir_ranking()
        elif opcao == "4":
            print("Ate a proxima!")
            break
        else:
            print("Opcao invalida. Escolha entre 1 e 4.")


if __name__ == "__main__":
    menu_principal()