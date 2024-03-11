#Estrutura Condicional Encadeada "IF-ELSE-IF"

#Entrada de dados:
nota = float(input("Digite a nota do aluno:\n"))

#Processamento dos dados:
if(nota>=9):
    print("Conceito final: A")
elif(nota>=7):
    print("Conceito final: B")
elif(nota>=6):
    print("Conceito final: C")
elif(nota>=5):
    print("Conceito final: D")
else:
    print("Conceito final: F")

print("FIM DO PROGRAMA!")