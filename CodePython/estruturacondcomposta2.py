#Estrutura Condicional Composta "IF-ELSE"

#Cabeçalho:
print('-'*43)
print("Responda a pergunta a seguir com sim ou não")
print('-'*43)

#Entrada de dados:
resposta = input("Seu time venceu a última partida que ele disputou?\n")

#Processamento  e Saída de dados:
if((resposta=='sim') or (resposta=='Sim')):
    print("Que Amazing! Você deve estar very happy!")
else:
    print("Que Infelicidade! Você deve estar very upset!")

print("FIM DO PROGRAMA!")
