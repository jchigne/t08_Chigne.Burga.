#operacion-CONCATENACION 06
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"

#coleguio de procedencia
a=(str.upper()[9]+str[15]+str[19]+str[4])
b=(str.upper()[12]+str[0]+str[18]+str[8]+str[0])
c=(str.upper()[0]+str[18]+str[6]+str[4]+str[3]+str[0]+str[19])
print("Colguio de procedencia:"+a+" "+b+" "+c)
