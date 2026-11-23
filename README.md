# Jogo da Forca com Ranking (Python)

Jogo da forca interativo no terminal desenvolvido em **Python**, com suporte a temas, cálculo de pontuação e ranking persistente ordenado do maior para o menor.

## Sobre o Projeto

O objetivo deste projeto é aplicar fundamentos essenciais da linguagem Python de forma organizada e modular, simulando uma aplicação de linha de comando (CLI) completa com salvamento de estado entre execuções.

## Como Funciona

1. **Menu Inicial:** O jogador escolhe entre jogar uma partida (selecionando um tema), visualizar o ranking geral ou sair.
2. **Dinâmica do Jogo:**
   - O sistema sorteia uma palavra secreta de uma lista predefinida de acordo com o tema.
   - A cada rodada, o jogador informa uma letra e o programa valida se a entrada é válida e ainda não foi utilizada.
   - Acertos revelam posições na palavra; erros avançam o desenho da forca e consomem tentativas.
3. **Pontuação e Ranking:**
   - Ao final da partida, o jogador informa seu nome e o resultado é salvo em `data/ranking.json`.
   - A opção **Ver Ranking** lê o arquivo e exibe os jogadores ordenados de forma decrescente pela pontuação.

## Técnicas e Conceitos Utilizados

- **Modularização de código:** Separação de responsabilidades entre interface/menu (`main.py`), lógica do jogo (`src/game.py`), banco de palavras (`src/words.py`) e persistência (`src/ranking.py`).
- **Controle de fluxo e loops:** Uso de `while` para o menu principal, loop da partida e validação de entradas, além de `for` para formatação do ranking.
- **Manipulação de strings e conjuntos (`set`):** Normalização de texto (`.strip().lower()`), verificação de caracteres (`.isalpha()`) e uso de `set` para controlar letras corretas, erradas e condição de vitória (`issubset`).
- **Persistência em JSON e `pathlib`:** Leitura e escrita segura de arquivos com `Path`, `json.load` e `json.dump`, além de tratamento de exceções (`try/except`).
- **Ordenação customizada:** Uso de `sorted(..., key=..., reverse=True)` para ordenar o ranking do maior para o menor.

## Como Executar

```bash
git clone [https://github.com/nicoalscalegari/jogo-da-forca-python.git](https://github.com/nicoalscalegari/jogo-da-forca-python.git)
cd jogo-da-forca-python
python main.py

## Exemplo de Uso

=== JOGO DA FORCA ===
1. Jogar (Programacao)
2. Jogar (Tecnologia)
3. Ver Ranking
4. Sair
Escolha uma opcao: 1

=== NOVA PARTIDA | Tema: PROGRAMACAO ===

      +---+
      |   |
          |
          |
          |
          |
    =========
    
Palavra: _ _ _ _ _ _ _ _
Chances restantes: 6/6
Digite uma letra: a
Boa! A letra 'a' esta na palavra.

Palavra: _ _ _ _ _ _ _ a
Chances restantes: 6/6
Digite uma letra: e
Que pena! A letra 'e' nao esta na palavra.

...

Parabens! Voce acertou a palavra: 'VARIAVEL'
Pontuacao obtida: 170 pontos.

Digite seu nome para salvar no ranking: Ana
Pontuacao salva com sucesso!

=== JOGO DA FORCA ===
1. Jogar (Programacao)
2. Jogar (Tecnologia)
3. Ver Ranking
4. Sair
Escolha uma opcao: 3

================ RANKING ================
 1o | Ana                |  170 pts | Palavra: variavel
 2o | Lucas              |  135 pts | Palavra: algoritmo
 3o | Marina             |   90 pts | Palavra: iteracao
=========================================