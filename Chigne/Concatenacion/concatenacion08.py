#operacion-CONCATENACION 08
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"

#La pelicula y su protagonista
a=(str.upper()[5]+str[18]+str[15]+str[26]+str[4]+str[13]+"'"+str.upper()[8]*2+"'")
b=(str.upper()[4]+str[11]+str[19]+str[0])
print("La pelicula:"+a+" y su protagonista es:"+b)
