#Operador OR
entrada_1 = False
entrada_2 = False

resultado = entrada_1 or entrada_2
print(resultado)

#-----------------------------------------
entrada_3 = True
entrada_4 = False

resultado_2 = entrada_3 or entrada_4
print(resultado_2)

#-----------------------------------------
entrada_5 = ((2*2+3) == 6)
entrada_6 = ((2+2) != 4)
entrada_7 = ((1+9) != 10)

print(f"{entrada_5} or {entrada_6} or {entrada_7} = {entrada_5 or entrada_6 or entrada_7}")

#-----------------------------------------
entrada_8 = True
entrada_9 = False
entrada_10 = True

print((entrada_8 and entrada_9) or entrada_10)
