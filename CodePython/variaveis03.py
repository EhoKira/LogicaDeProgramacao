#Entrada de dados:
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
idade = int(input("Digite a sua idade: "))

#Processamento:
imc = peso/(altura*altura)

#Saída de dados:
print(f"O seu IMC é igual à: {imc:.2f} e sua idade é igual à: {idade}")
#f (fstring) apresenta um texto fixo mais um conteúdo de uma variável.
#.2f vai fazer uma conversão na variavel, apresentando a variável com duas casas decimais.
