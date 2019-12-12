#operacion-CONCATENACION 09
#    0         10        20        30
#    0123456789012345678901234567890123456789
str="abcdefghijklmnñopqrstuvwxyz0123456789@.%"

#oro
a=(str[29]+str[28]+str[39])
b=(str[15]+str[18]+str[15])
c=(str.upper()[16]+str[4]+str[18]+str[21])
d=(str.upper()[11]+str[0]+" "+str.upper()[11]+str[8]+str[1]+str[4]+str[18]+
   str[20]+str[0]+str[3])

#output
print("El "+a+" de "+b+" del "+c+" esta en la reguion "+"'"+d+"'")
