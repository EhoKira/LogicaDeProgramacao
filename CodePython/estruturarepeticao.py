#Estrutura de Repetição "WHILE"

#Recebendo o número do usuário:
numero = input("Digite um número para o cálculo de sua tabuada:\n")
#Convertendo o número para inteiro:
numero = int(numero)
#Criando a variável de controle do laço de repetição:
contador = 1
while(contador<=10):
    #Exibindo o valor a tabuada:
    print(f"{numero} x {contador} = {numero*contador}")
    contador = contador + 1 #incremento de +1
print("Fim de Programa!")