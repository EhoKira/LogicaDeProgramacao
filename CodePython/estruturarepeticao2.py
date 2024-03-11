#Estrutura de Repetição "WHILE"

#Criando a variável de controle do laço, contando 5 repetições
contador = 1
#Criando uma variável para acumular os valores das idades digitadas:
acumulador = 0
#Criando o laço de repetição para receber 5 idades e somá-las:
while(contador<=5):
    #Recebendo a idade do usuário
    idade = int(input(f"Digite a idade do usuário n°{contador}: "))
    #Somando a idade do usuário ao valor atual da variável acumuldor
    acumulador = acumulador + idade
    #Incrementando a variável contador para controle do laço
    contador = contador + 1
#Calculando a média das idades:
media = acumulador/5 #ou acumulador/(contador-1)
print(f"A média das idades digitadas é igual à: {media}")