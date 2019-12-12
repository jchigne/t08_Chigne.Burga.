#operacion-CONCATENACION 03
#    0         10        20        30
#    0123456789012345678901234567890123456
str="abcdefghijklmnñopqrstuvwxyz0123456789"

#input
#Nro de DNI Y estado civil
DNI=(str[34]+str[30]+str[29]+str[31]+str[29]+str[33]+str[27]+str[28])
civil=(str.upper()[19]+str[15]+str[20]+str[4]+str[18]+str[15])
print("Mi numero de DNI es:"+DNI+" Y mi estado civil:"+civil)
