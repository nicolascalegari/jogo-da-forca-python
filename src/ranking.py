from datetime import datetime
import json
from pathlib import Path

CAMINHO_RANKING = Path(__file__).resolve().parent.parent / "data" / "ranking.json"


def carregar_ranking() -> list[dict]:
    """Carrega o ranking do arquivo JSON. Retorna lista vazia se não existir ou estiver inválido."""
    if not CAMINHO_RANKING.exists():
        return []

    try:
        with CAMINHO_RANKING.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def salvar_pontuacao(nome: str, pontos: int, palavra: str) -> None:
    """Adiciona uma nova entrada ao ranking e salva no disco."""
    CAMINHO_RANKING.parent.mkdir(parents=True, exist_ok=True)
    ranking = carregar_ranking()

    nome_limpo = nome.strip() or "Jogador Anonimo"
    nova_entrada = {
        "nome": nome_limpo,
        "pontos": pontos,
        "palavra": palavra,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

    ranking.append(nova_entrada)

    with CAMINHO_RANKING.open("w", encoding="utf-8") as arquivo:
        json.dump(ranking, arquivo, indent=4, ensure_ascii=False)


def obter_ranking_ordenado() -> list[dict]:
    """Retorna as pontuações ordenadas do maior para o menor."""
    ranking = carregar_ranking()
    return sorted(ranking, key=lambda item: item.get("pontos", 0), reverse=True)