# Contextualização do problema pode ser encontrada no link abaixo:
# https://share.note.sx/3bpf97pd

import scipy

# Função Objetivo: L = 65x_{1} + 72x_{2} +70x_{3} + 75x_{4} + 55x_{5} + 50x_{6} + 40x_{7}
coeficientes_l = [-65, -72, -70, -75, -55, -50, -40]

# Faixa da quantidade de caixas de cada material:
all_bounds = [
    (0, 150),   # (A = x_{1})
    (0, 100),   # (M = x_{2})
     (0, 80),   # (F = x_{3})
     (0, 50),   # (T = x_{4})
     (0, 200),  # (B = x_{5})
     (0, 200),  # (S = x_{6})
     (0, 200)   # (D = x_{7})
]

# Restrições do número da quantidade de caixas no caminhão:
# R(15): x_{1} + x_{2} + x_{3} + x_{4} + x_{5} + x_{6} + x_{7} \leq 600
coeficientes_restricao_num_caixas = [1, 1, 1, 1, 1, 1, 1]
inequacao_restricao_num_caixas = 600

# Restricao Peso Caixas
# R(16): 20x_{1} + 18x_{2} + 17x_{3} + 12x_{4} + 25x_{5} + 8x_{6} + 20x_{7} \leq 800
coeficientes_restricao_peso_caixas = [20, 18, 17, 12, 25, 8, 20]
inequacao_restricao_peso_caixas = 800

# Todas as restricoes:
all_coeficientes = [coeficientes_restricao_num_caixas, coeficientes_restricao_num_caixas]
all_inequacoes = [inequacao_restricao_num_caixas, inequacao_restricao_peso_caixas]
#Limites das Variáveis


# Resolvendo o problema através dea progressão linear:
resultado = scipy.optimize.linprog(coeficientes_l, A_ub=all_coeficientes, b_ub=all_inequacoes, bounds=all_bounds, method='highs')
print(f"Status: {resultado.message}")
print(f"Valor ótimo de x_1: {int(resultado.x[0])}")
print(f"Valor ótimo de x_2: {int(resultado.x[1])}")
print(f"Valor ótimo de x_3: {int(resultado.x[2])}")
print(f"Valor ótimo de x_4: {int(resultado.x[3])}")
print(f"Valor ótimo de x_5: {int(resultado.x[4])}")
print(f"Valor ótimo de x_6: {int(resultado.x[5])}")
print(f"Valor ótimo de x_7: {int(resultado.x[6])}")
print(f"Valor máximo de L (lucro): R$ {int(-resultado.fun)}")