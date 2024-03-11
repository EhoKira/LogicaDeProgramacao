#Estrutura de Repetição "FOR"

#Entrada de dados:
num = int(input("Digite um número para o cálculo da sua tabuada: "))
print('-'*13)
print(f"Tabuada do {num}:")
print('-'*13)
for i in range(1,11,1):
    print(f"{num} x {i} = {num*i}")
print('-'*13)