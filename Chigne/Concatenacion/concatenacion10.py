#operacion-CONCATENACION 10
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"

#Ganador del balon de oro
a=(str.upper()[11]+str[8]+str[15]+str[13]+str[4]+str[11])
b=(str.upper()[12]+str[4]+str[19]*2+str[8])
print("El balon de oro es para:"+a+" "+b+" :D")
