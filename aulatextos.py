faturamento = 4000 # tipo: int -> numero inteiro
Custo = 300 #tipo: float -> numero decimal
lucro = faturamento - Custo

print(f"faturamento da empresa: {faturamento}, Custo: {Custo}, lucro: {lucro}")

email_cliente = "walney.consultor@gmail.com"

# maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)
# minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# "@"
print(email_cliente.find("@")) # quando não encontra o caracter retorna -1

# tamanho do texto
print(len(email_cliente))

print(email_cliente[4])
print(email_cliente[-1])

#pegar um pedaço do texto
print(email_cliente[0:26])

#trocar um pedaço do texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")

