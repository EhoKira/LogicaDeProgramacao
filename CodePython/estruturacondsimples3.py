#Estrutura Condicional Simples "IF"
print("Para a pergunta a seguir, responda apenas com sim ou não:")
resposta = input("Seu time de futebol venceu a última partida que ele disputou?\n")

if((resposta=="sim")or(resposta=="Sim")):
    print("Que Maravilhoso!")
    print("Você deve estar feliz.")

if((resposta=="não")or(resposta=="Não")):
    print("Que infelicidade!")
    print("Você deve estar chateado.")

print("FIM DAS PERGUNTAS")