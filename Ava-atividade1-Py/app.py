
import random
from collections import Counter
from legenda import candidatos


total_de_Eleitores = 1001

# faz um loop aleatorio de votação com 1000 votos
votos_random = [random.randint(1,6) for i in range(total_de_Eleitores)]
votos_total = Counter(votos_random)
#print(votos_total)

print("========================================================================")
print("Resultado da eleição: \n")

for codigo, nome in candidatos.items():
    print(f"{nome}: {votos_total.get(codigo, 0)} votos")
print("========================================================================")

votos_nulos = votos_total.get(5, 0)  # Votos nulos
total_votos = sum(votos_total.values())  # Total de votos
if total_votos > 0:
    porcentagem_nulos = (votos_nulos / total_votos) * 100
else:
    porcentagem_nulos = 0

print(f"\nPorcentagem de Votos Nulos: {porcentagem_nulos:.2f}%")

# Cálculo da porcentagem de votos em branco
votos_branco = votos_total.get(6, 0)  # Votos em branco
total_votos = sum(votos_total.values())  # Total de votos
if total_votos > 0:
    porcentagem_branco = (votos_branco / total_votos) * 100  
else:
    porcentagem_branco = 0

print(f"Porcentagem de Votos em Branco: {porcentagem_branco:.2f}%")
print("========================================================================")


# Encontrando o candidato vencedor
vencedor_codigo = max(candidatos.keys() - {5, 6}, key=lambda x: votos_total.get(x, 0))
vencedor_nome = candidatos[vencedor_codigo]
print("\n")
print(f"Candidato Vencedor: {vencedor_nome} com {votos_total.get(vencedor_codigo, 0)} votos")

print("========================================================================")


#testando se obteve retorno de 100% 
total_votos = sum(votos_total.values())
print(f"Total de votos: {total_votos}")






