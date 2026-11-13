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

_inimigos = random.randint(3, 5)
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