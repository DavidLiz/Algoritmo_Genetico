# BIBLIOTECAS
from array import array
from typing import List
import numpy as np
import random
from numpy.core import numeric
from numpy.core.numeric import cross 

print("ALGORITMO GENÉTICO: OTIMIZAÇÃO DOS PARÂMETROS DE UMA CAIXA PRETA")
print("Algortimo feito por David Li Zhao(18202656) para a disciplina de Inteligência Artifical da Universidade Federal de Santa Catarina")
print("Técnicas utilizadas: Mutação Simples e Crossover por Elitismo")
print("")

# VARIÁVEIS
max_poss = 2**36
n = 0
pop_sum = 0
pop_b = []
pop_d = []
pop_fit = []
pop = [[0 for _ in range(3)]for _ in range(100)]
crossover = []
prob = []
cont = True
ind_max = [0,0,0]
total_ger = 0

# ------------------------------------------------------------------------- PRIMEIRA GERAÇÃO ------------------------------------------------------------------------- #
# GERA A PRIMEIRA POPULAÇÃO
while(n<100):
    r = (random.randint(0, max_poss))
    b = '%0*d' % (36, int(bin(r)[2:]))
    pop_d.append(r)
    pop_b.append(b)
    n=n+1
n = 0

# SINAL DE SAÍDA
for number in range(len(pop_d)):
    pop_targ = pop_b[number]
    saida = 9 + (int(pop_targ[1])*int(pop_targ[4])) - (int(pop_targ[22])*int(pop_targ[13])) + (int(pop_targ[23])*int(pop_targ[3])) - (int(pop_targ[20])*int(pop_targ[9])) + (int(pop_targ[35])*int(pop_targ[14])) - (int(pop_targ[10])*int(pop_targ[25])) + (int(pop_targ[15])*int(pop_targ[16])) + (int(pop_targ[2])*int(pop_targ[32])) + (int(pop_targ[27])*int(pop_targ[18])) + (int(pop_targ[11])*int(pop_targ[33])) - (int(pop_targ[30])*int(pop_targ[31])) - (int(pop_targ[21])*int(pop_targ[24])) + (int(pop_targ[34])*int(pop_targ[26])) - (int(pop_targ[28])*int(pop_targ[6])) + (int(pop_targ[7])*int(pop_targ[12])) - (int(pop_targ[5])*int(pop_targ[8])) + (int(pop_targ[17])*int(pop_targ[19])) - (int(pop_targ[0])*int(pop_targ[29])) - (int(pop_targ[22])*int(pop_targ[3])) + (int(pop_targ[20])*int(pop_targ[14])) + (int(pop_targ[25])*int(pop_targ[15])) + (int(pop_targ[30])*int(pop_targ[11])) + (int(pop_targ[24])*int(pop_targ[18])) + (int(pop_targ[6])*int(pop_targ[7])) + (int(pop_targ[8])*int(pop_targ[17])) + (int(pop_targ[0])*int(pop_targ[32]))
    pop_fit.append(saida)

# INTEGRA TODAS AS LISTAS
for number in range(len(pop_fit)):
    pop[number][0] = pop_d[number]
    pop[number][1] = pop_b[number]
    pop[number][2] = pop_fit[number]

# ORDENA LISTA PELO FITNESS
pop = sorted(pop,key=lambda x: x[2])

# ------------------------------------------------------------------------- PRÓXIMAS GERAÇÕES ------------------------------------------------------------------------- #
while(cont):
    prob.clear()
    # SELECIONA OS 20% MAIS APTOS
    for number in range(80, 100):
        crossover.append(pop[number][1])

    # APLICA CROSSOVER
    while(n<len(crossover)):
        r = (random.randint(0, 36))
        corte_dir_1 = crossover[n][r:36]
        corte_dir_2 = crossover[n+1][r:36]
        corte_esq_1 = pop_b[n][0:r]
        corte_esq_2 = pop_b[n+1][0:r]
        filho_1 = (corte_esq_1+corte_dir_2)
        filho_2 = (corte_esq_2+corte_dir_1)

        # APLICA MUTAÇÃO NO FILHO 1
        for number in range(0,36):
            r2 = (random.randint(0, 115))
            if(r2 == 1):
                if(filho_1[number] == "1"):
                    filho_1 = filho_1[0:number]+"0"+filho_1[(number+1):36]
                if(filho_1[number] == "0"):
                    filho_1 = filho_1[0:number]+"1"+filho_1[(number+1):36]

        # APLICA MUTAÇÃO NO FILHO 2
        for number in range(0,36):
            r2 = (random.randint(0, 115))
            if(r2 == 1):
                if(filho_2[number] == "1"):
                    filho_2 = filho_2[0:number]+"0"+filho_2[(number+1):36]
                if(filho_2[number] == "0"):
                    filho_2 = filho_2[0:number]+"1"+filho_2[(number+1):36]

        # SUBSTITUI OS INDIVÍDUOS MENOS APTOS PELOS FILHOS DOS INDIVÍDUOS MAIS APTOS
        pop[n][0] = int(filho_1,2)
        pop[n+1][0] = int(filho_2, 2)
        pop[n][1] = filho_1
        pop[n+1][1] = filho_2
        n = n+2
    n=0

    # CALCULA O SINAL DE SAÍDA PARA OS NOVOS INDIVÍDUOS (FILHOS GERADOS)
    for number in range(len(crossover)):
        pop_targ = pop[number][1]
        saida = 9 + (int(pop_targ[1])*int(pop_targ[4])) - (int(pop_targ[22])*int(pop_targ[13])) + (int(pop_targ[23])*int(pop_targ[3])) - (int(pop_targ[20])*int(pop_targ[9])) + (int(pop_targ[35])*int(pop_targ[14])) - (int(pop_targ[10])*int(pop_targ[25])) + (int(pop_targ[15])*int(pop_targ[16])) + (int(pop_targ[2])*int(pop_targ[32])) + (int(pop_targ[27])*int(pop_targ[18])) + (int(pop_targ[11])*int(pop_targ[33])) - (int(pop_targ[30])*int(pop_targ[31])) - (int(pop_targ[21])*int(pop_targ[24])) + (int(pop_targ[34])*int(pop_targ[26])) - (int(pop_targ[28])*int(pop_targ[6])) + (int(pop_targ[7])*int(pop_targ[12])) - (int(pop_targ[5])*int(pop_targ[8])) + (int(pop_targ[17])*int(pop_targ[19])) - (int(pop_targ[0])*int(pop_targ[29])) - (int(pop_targ[22])*int(pop_targ[3])) + (int(pop_targ[20])*int(pop_targ[14])) + (int(pop_targ[25])*int(pop_targ[15])) + (int(pop_targ[30])*int(pop_targ[11])) + (int(pop_targ[24])*int(pop_targ[18])) + (int(pop_targ[6])*int(pop_targ[7])) + (int(pop_targ[8])*int(pop_targ[17])) + (int(pop_targ[0])*int(pop_targ[32]))
        pop[number][2] = saida

    # ORDENA LISTA PELO FITNESS
    pop = sorted(pop,key=lambda x: x[2])

    # ARMAZENA O INDIVÍDUO MAIS APTO DE TODA A POPULAÇÃO
    if(pop[99][2]>ind_max[2]):
        ind_max[0] = pop[99][0]
        ind_max[1] = pop[99][1]
        ind_max[2] = pop[99][2]

    # SOMATÓRIA (f(xi))
    for number in range(len(pop_d)):
        pop_d[number] = pop[number][0]
    pop_sum = sum(pop_d)

    # PROBABILIDADE DE SELEÇÃO 
    var = 0
    for number in range(len(pop)):
        prob.append((pop_d[number]/pop_sum)*100)

        # CRITÉRIO DE PARADA
        if(int(prob[number]) > 0.99):
            var = var+1
        if(var>=70):
            cont = False 
    
    total_ger = total_ger + 1
    crossover.clear()

# INDICADORES
print("--------------------- INDICADORES ---------------------")
print("")
print("- O algoritmo produziu", total_ger+1, "gerações e", (total_ger*100)+100, "indivíduos")
print("- O melhor genótipo encontrado foi: ", ind_max[1])
print("- O maior sinal de saída encontrado foi: ",ind_max[2])
print("- Houve uma perda de 70% da variabilidade genética")
print("")

print("--------------------- MELHOR POSIÇÃO PARA OS BOTÕES ---------------------")
print("")
pos_ini = 0
pos_fim = 4
for number in range(0,9):
    print("BOTÃO", number+1, ": ", int(ind_max[1][pos_ini:pos_fim], 2))
    pos_ini = pos_ini + 4
    pos_fim = pos_fim + 4

    