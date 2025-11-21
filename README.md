Aqui está um **README.md completo**, organizado e pronto pra colocar no GitHub ou entregar com o projeto.


---

# 🪨📄✂️ Jokenpô em Python

### Versão com Recursividade 

Este projeto implementa o clássico jogo **Jokenpô (Pedra, Papel e Tesoura)** em Python.
O jogo possui 3 modalidades, placar usando uma **matriz**, entrada validada e repetição usando **recursividade**, sem utilizar `while` ou `main()`.

---

## 🎮 Modos de Jogo

O usuário pode escolher entre:

1. **Humano x Humano**
2. **Humano x Computador**
3. **Computador x Computador**

Cada jogada é comparada e o vencedor determinado automaticamente.

---

## 🔁 Recursividade

A função `jogar_partida()` chama a si mesma sempre que o usuário deseja continuar o jogo:

```python
if continuar == "s":
    return jogar_partida(opcao, nomes, placar)
```

Assim, não é necessário usar loops (`while`), atendendo aos requisitos do trabalho.

---

## 📊 Placar

O placar é armazenado em uma matriz:

```python
placar = [[vitorias_jogador1, vitorias_jogador2, empates]]
```

Exemplo:

| Jogador 1 | Jogador 2 | Empates |
| --------- | --------- | ------- |
| 3         | 1         | 2       |

---

## 🧠 Lógica de Vencedor

A regra usada é:

* Pedra > Tesoura
* Tesoura > Papel
* Papel > Pedra

Implementada por:

```python
elif (jogada1 == 1 and jogada2 == 3) or \
     (jogada1 == 2 and jogada2 == 1) or \
     (jogada1 == 3 and jogada2 == 2):
```

---

## 🗂 Estrutura do Programa

O código é dividido em funções:

* `mostrar_menu()` → mostra opções e valida entrada
* `obter_jogada()` → valida jogada do jogador
* `jogada_computador()` → gera jogada aleatória
* `determinar_vencedor()` → decide quem venceu
* `mostrar_placar()` → exibe placar formatado
* `jogar_partida()` → **função recursiva principal**

---

## ▶️ Como Executar

1. Instale o Python 3.
2. Salve o arquivo como `jokenpo.py`.
3. Execute no terminal:

```
python jokenpo.py
```

4. Escolha a modalidade e jogue!

---

## 👨‍💻 Desenvolvido por

* **Thiago Oliveira**


---


