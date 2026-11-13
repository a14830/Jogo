import random

print("=== SIMULADOR DE BATALHA ===")
jogador = {
    "vida": 300,
    "ataque": 20,
    "pocoes": 2,
    "pontos": 0
}

tipos_inimigos = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500}
]

qtd_inimigos = random.randint(3, 5)
inimigos = []

for i in range(qtd_inimigos):
    escolhido = random.choice(tipos_inimigos)
    novo_inimigo = {
        "nome": escolhido["nome"],
        "vida": escolhido["vida"],
        "ataque": escolhido["ataque"],
        "pontos": escolhido["pontos"]
    }
    inimigos.append(novo_inimigo)

    fugiu = False

while jogador["vida"] > 0:
    inimigos_vivos = []
    for inimigo in inimigos:
        if inimigo["vida"] > 0:
            inimigos_vivos.append(inimigo)
    if len(inimigos_vivos) == 0:
        break

    print("\n========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nInimigos vivos:")
        for i in range(len(inimigos_vivos)):
            inimigo = inimigos_vivos[i]
            print(f"{i + 1} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")

        escolha = input("Escolha o número do inimigo: ")

    elif opcao == "2":
        derrotados = len(inimigos) - len(inimigos_vivos)
        print("\n--- Estado do Jogador ---")
        print(f"Vida atual: {jogador['vida']}")
        print(f"Pontuação: {jogador['pontos']}")
        print(f"Inimigos derrotados: {derrotados}")
        print(f"Inimigos ainda vivos: {len(inimigos_vivos)}")
        print(f"Poções disponíveis: {jogador['pocoes']}")

    elif opcao == "3":
        print("\n--- Inimigos Vivos ---")
        if len(inimigos_vivos) == 0:
            print("Não existem inimigos vivos.")
        else:
            for inimigo in inimigos_vivos:
                print(f"{inimigo['nome']} - Vida: {inimigo['vida']} - Ataque: {inimigo['ataque']}")

    elif opcao == "4":
        if jogador["pocoes"] == 0:
            print("Você não tem poções disponíveis!")
        elif jogador["vida"] >= 100:
            print("\nVocê não pode usar poção porque já tens 100 ou mais pontos de vida!\n")
        else:
            jogador["pocoes"] -= 1
            jogador["vida"] += 25
            if jogador["vida"] > 100:
                jogador["vida"] = 100
            print(f"usou uma poção! Vida atual: {jogador['vida']}")

    elif opcao == "5":
        fugiu = True
        print("\n=============================")
    if fugiu == True:
        print("FUGA! Terminou a partida por fuga, A fuga não é uma vitória.")
    elif jogador["vida"] == 0:
        print("DERROTA! Você ficou sem pontos de vida.")
    else:
        print("VITÓRIA! Derrotou todos os inimigos!")
        print(f"Pontuação final: {jogador['pontos']}")
