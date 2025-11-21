# ==========================================================
#  JOGO DE JOKENPÔ - VERSÃO COM RECURSIVIDADE 
# ==========================================================
import random

# ----------------------------------------------------------
# FUNÇÕES AUXILIARES
# ----------------------------------------------------------
def mostrar_menu():
    """Exibe o menu inicial e retorna a opção escolhida."""
    print("********************* JOKENPÔ *********************")
    print("As regras são:")
    print("Pedra ganha da Tesoura / Tesoura ganha do Papel / Papel ganha da Pedra")
    print("***************************************************")
    print("1 - Humano x Humano")
    print("2 - Humano x Computador")
    print("3 - Computador x Computador")
    print("***************************************************")
    try:
        opcao = int(input("Escolha a modalidade: "))
        if opcao in [1, 2, 3]:
            return opcao
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")
            return mostrar_menu()  # chamada recursiva
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return mostrar_menu()  # chamada recursiva


def obter_jogada(jogador):
    """Solicita jogada de um jogador humano."""
    print(f"\n{jogador}, escolha sua jogada:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    try:
        jogada = int(input("Digite o número da sua jogada: "))
        if jogada in [1, 2, 3]:
            return jogada
        else:
            print("Jogada inválida! Tente novamente.")
            return obter_jogada(jogador)  # recursão
    except ValueError:
        print("Entrada inválida! Digite apenas 1, 2 ou 3.")
        return obter_jogada(jogador)  # recursão


def jogada_computador():
    """Gera jogada aleatória do computador."""
    return random.randint(1, 3)


def determinar_vencedor(jogada1, jogada2):
    """Determina o vencedor com base nas jogadas."""
    if jogada1 == jogada2:
        return 0
    elif (jogada1 == 1 and jogada2 == 3) or \
         (jogada1 == 2 and jogada2 == 1) or \
         (jogada1 == 3 and jogada2 == 2):
        return 1
    else:
        return 2


def nome_jogada(num):
    """Converte número em texto (Pedra, Papel, Tesoura)."""
    return ["", "Pedra", "Papel", "Tesoura"][num]


def mostrar_placar(placar, nomes):
    """Exibe o placar geral usando a matriz."""
    print("\n=========== PLACAR GERAL ===========")
    print(f"{nomes[0]}: {placar[0][0]} vitórias")
    print(f"{nomes[1]}: {placar[0][1]} vitórias")
    print(f"Empates: {placar[0][2]}")
    print("====================================\n")


# ----------------------------------------------------------
# FUNÇÃO RECURSIVA DO JOGO
# ----------------------------------------------------------
def jogar_partida(opcao, nomes, placar):
    """Executa uma rodada e chama recursivamente para continuar o jogo."""

    print("\n=========== NOVA PARTIDA ===========")

    # Coleta das jogadas
    if opcao == 1:
        jogada1 = obter_jogada(nomes[0])
        jogada2 = obter_jogada(nomes[1])
    elif opcao == 2:
        jogada1 = obter_jogada(nomes[0])
        jogada2 = jogada_computador()
        print(f"{nomes[1]} escolheu: {nome_jogada(jogada2)}")
    else:
        jogada1 = jogada_computador()
        jogada2 = jogada_computador()
        print(f"{nomes[0]} escolheu: {nome_jogada(jogada1)}")
        print(f"{nomes[1]} escolheu: {nome_jogada(jogada2)}")

    # Determina o vencedor
    resultado = determinar_vencedor(jogada1, jogada2)

    if resultado == 0:
        print("Empate!")
        placar[0][2] += 1
    elif resultado == 1:
        print(f"{nomes[0]} venceu!")
        placar[0][0] += 1
    else:
        print(f"{nomes[1]} venceu!")
        placar[0][1] += 1

    # Mostra o placar atualizado
    mostrar_placar(placar, nomes)

    # Pergunta se deseja continuar
    continuar = input("Deseja jogar novamente? (s/n): ").lower()
    if continuar == "s":
        return jogar_partida(opcao, nomes, placar)  # chamada recursiva
    else:
        print("\n========= PLACAR FINAL =========")
        mostrar_placar(placar, nomes)

        if placar[0][0] > placar[0][1]:
            print(f" {nomes[0]} foi o grande vencedor!")
        elif placar[0][1] > placar[0][0]:
            print(f" {nomes[1]} foi o grande vencedor!")
        else:
            print(" O jogo terminou empatado!")

        print("\nDesenvolvido por: Thiago Oliveira e [Seu Nome Aqui]")
        print("=====================================")


# ----------------------------------------------------------
# PROGRAMA EXECUTA DIRETAMENTE (SEM MAIN)
# ----------------------------------------------------------
opcao = mostrar_menu()

# Definição de nomes
if opcao == 1:
    nome1 = input("Digite o nome do jogador 1: ")
    nome2 = input("Digite o nome do jogador 2: ")
elif opcao == 2:
    nome1 = input("Digite o nome do jogador: ")
    nome2 = "Computador"
else:
    nome1 = "Computador 1"
    nome2 = "Computador 2"

nomes = [nome1, nome2]

# Matriz do placar
placar = [[0, 0, 0]]

# Primeira partida (recursiva)
jogar_partida(opcao, nomes, placar)
