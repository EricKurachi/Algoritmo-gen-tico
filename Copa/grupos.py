import random

def main():
    pontos_selecao_1 = 457
    pontos_selecao_2 = 465

    gols_s_1 = 0
    gols_s_2 = 0

    g = 0

    if g == 0:
        r = random.randint(1, 100)
        if r <= 87:
            g += 1

    if g == 1:
        r = random.randint(1, 100)
        if r <= 81:
            g += 1

    if g == 2:
        r = random.randint(1, 100)
        if r <= 88:
            g += 1

    if g == 3:
        r = random.randint(1, 100)
        if r <= 50:
            g += 1

    if g == 4:
        r = random.randint(1, 100)
        if r <= 53:
            g += 1

    if g == 5:
        r = random.randint(1, 100)
        if r <= 75:
            g += 1

    if g == 6:
        r = random.randint(1, 100)
        if r <= 50:
            g += 1

    for i in range (0, g):
        soma = pontos_selecao_1 + pontos_selecao_2
        gol = random.randint(1, soma)
        if gol <= pontos_selecao_1:
            gols_s_1 += 1
        else:
            gols_s_2 += 1

    print("o numero de gols foi: {}".format(g))
    print("{}x{}".format(gols_s_1, gols_s_2))
    raw_input('hey')



if __name__ == "__main__":
    main()