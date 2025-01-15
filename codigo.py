import math


faturamento = 3000 # tipo: int -> numero inteiro
custo = 700.02 #tipo: float -> numero decimal

novas_vendas = 100 # tipo: int -> numero inteiro
faturamento = faturamento + novas_vendas 
imposto = faturamento * 0.1 # tipo: float -> numero decimal
lucro = faturamento - custo - imposto


marge_lucro = lucro / faturamento * 100
print("faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", round (lucro, 2))
print("A margem de lucro foi de ", round (marge_lucro, 2))

teve_lucro = lucro > 0 # tipo: bool -> booleano 