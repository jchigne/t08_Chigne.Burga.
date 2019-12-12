#Ejericicio-ITERACION 15
msg="I would like to escape from me"
contador_a=0
contador_e=0
contador_i=0
contador_o=0
contador_u=0

for letra in msg:
    if (letra == 'a'):
        contador_a+=1
    if (letra == 'e'):
        contador_e+=1
    if (letra == 'i'):
        contador_i+=1
    if (letra == 'o'):
        contador_o+=1
    if (letra == 'u'):
        contador_u+=1

# Contar cuantas vocales existen en la cadena
print("A: ",contador_a)
print("E: ",contador_e)
print("I: ",contador_i)
print("O: ",contador_o)
print("U: ",contador_u)
