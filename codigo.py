import math


faturamento = 3000 # tipo: int -> numero inteiro
custo = 700.02 #tipo: float -> numero decimal

novas_vendas = 100 # tipo: int -> numero inteiro
faturamento += novas_vendas
imposto = faturamento * 0.1 # tipo: float -> numero decimal
lucro = faturamento - custo - imposto


marge_lucro = lucro / faturamento * 100
print("faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", round (lucro, 2))
print("A margem de lucro foi de ", round (marge_lucro, 2))

# Coeficientes da equação do 2º grau: ax^2 + bx + c = 0
a = 16
b = 2
c = -4

# Calculando o discriminante
delta = b**2 - 4*a*c

# Verificando se as raízes são reais
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"A equação possui uma raiz real: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes da equação são: {raiz1} e {raiz2}")

    
    # Comprimentos dos catetos do triângulo retângulo
cateto_oposto = 4
cateto_adjacente = 12

# Calculando a hipotenusa
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Calculando os ângulos em radianos
angulo_oposto = math.asin(cateto_oposto / hipotenusa)
angulo_adjacente = math.acos(cateto_adjacente / hipotenusa)

# Convertendo os ângulos para graus
angulo_oposto_graus = math.degrees(angulo_oposto)
angulo_adjacente_graus = math.degrees(angulo_adjacente)

print(f"O ângulo oposto é: {angulo_oposto_graus} graus")
print(f"O ângulo adjacente é: {angulo_adjacente_graus} graus")
print("O ângulo reto é: 90 graus")