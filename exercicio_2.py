preco = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_final = preco - (preco*(desconto/100))

print(f"O preço final do produto é R$ {valor_final}")
