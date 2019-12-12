#operacion-CONCATENACION 05
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"

#sexo y Fecha de nacimiento
sexo=(str[12]+str[0]+str[19]+str[2]+str[21]+str[11]+str[8]+str[13]+str[15])
fecha=(str[28]+str[32]+" "+str[3]+str[4]+" "+str[3]+str[8]+str[2]+str[8]+str[4]+str[12]+str[1]+
       str[18]+str[4]+" "+str[3]+str[2]+" "+str[28]+str[36]*3)
print("Sexo:"+sexo+" Y fecha de nacimiento:"+fecha)
