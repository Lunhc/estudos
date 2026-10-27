# PEDRA, PAPEL E TESOURA
# ======================

# como rodar: python3 jogo.py

import random

OPCOES = {
    "1": "Pedra",
    "2": "Papel",
    "3": "Tesoura"
}

VENCE_DE = {
    "Pedra": "Tesoura",
    "Papel": "Pedra",
    "Tesoura": "Papel"
}

VITORIA_PARA_GANHAR = 3


def escolher_jogada_computador():
    return random.choice(list(OPCOES.values()))


def decidir_vencedor(jogador, computador):
    if jogador == computador:
        return "empates"

    if VENCE_DE[jogador] == computador:
        return "jogador"

    return "computador"


def pedir_jogada():
    while True:
        print("\nEscolha sua jogada:")
        for numero, nome in OPCOES.items():
            print(f"  [{numero}] {nome}")
        print("  [0] Sair")

        escolha = input("Sua escolha: ")

        if escolha == "0":
            return None

        if escolha in OPCOES:
            return OPCOES[escolha]

        print("Opção inválida. Tente novamente.")


def mostrar_resultado_rodada(jogador, computador, vencedor):
    print(f"\n Você jogou:        {jogador}")
    print(f" Computador jogou:  {computador}")

    if vencedor == "empates":
        print("Resultado: Empate!")
    elif vencedor == "jogador":
        print(f"Resultado: {jogador} vence {computador}. Você ganhou a rodada!")
    else:
        print(f"Resultado: {computador} vence {jogador}. O computador ganhou a rodada!")


def mostrar_placar(placar):
    print(
        f"\n Placar -> Você: {placar['jogador']} | "
        f"Computador: {placar['computador']} | "
        f"Empates: {placar['empates']}"
    )


# -------------------------------------------------
#               FLUXO PRINCIPAL
# -------------------------------------------------

def jogar():
    print("=" * 40)
    print("   ::: JOGO PEDRA, PAPEL E TESOURA :::")
    print("=" * 40)
    print(f"Quem fizer {VITORIA_PARA_GANHAR} pontos primeiro vence o jogo!")

    placar = {"jogador": 0, "computador": 0, "empates": 0}

    while (
        placar["jogador"] < VITORIA_PARA_GANHAR
        and placar["computador"] < VITORIA_PARA_GANHAR
    ):
        jogada_jogador = pedir_jogada()

        if jogada_jogador is None:
            print("Saindo do jogo...")
            return

        jogada_computador = escolher_jogada_computador()
        vencedor = decidir_vencedor(jogada_jogador, jogada_computador)

        placar[vencedor] += 1

        mostrar_resultado_rodada(jogada_jogador, jogada_computador, vencedor)
        mostrar_placar(placar)

    if placar["jogador"] > placar["computador"]:
        print("\nParabéns! Você venceu o jogo!")
    else:
        print("\nO computador venceu o jogo! Tente novamente.")


def main():
    try:
        while True:
            jogar()
            resposta = input("\nJogar novamente? (s/n): ").strip().lower()
            if resposta != "s":
                print("Obrigado por jogar!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nJogo encerrado. Até a próxima!")


if __name__ == "__main__":
    main()
