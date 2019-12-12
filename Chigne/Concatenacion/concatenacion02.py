#operacion-CONCATENACION 02
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"

#input
#Pais y departamento
pais=(str.upper()[16]+str[4]+str[18]+str[21])
departamento=(str.upper()[11]+str[0]+str[12]+str[1]+str[0]+str[25]
              +str[4]+str[17]+str[4])
print("soy de:"+pais ," y vivo en el departamento de:"+departamento)
