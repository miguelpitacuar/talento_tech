
#1 ejercicio resolver la ecuacio
resultado=((3+2)/(2*5))**2
print("resultado de la ecuasion es  {}".format(resultado))

# 2 ejercicio

#   unajugeteria tiene mucho exito en dos de sus productos payasos y muyecas 3
# payaso pesa = 112g
# muñleca pesa =75 g
peso_payaso=112
peso_muñeca=75

cant_payasos = int(input("Por favor, ingresa la cantidad de payasos: "))
cant_muñecas = int(input("Por favor, ingresa la cantidad de muñecas: "))

peso_total_payasos=cant_payasos*peso_payaso
peso_total_muñecas=cant_muñecas*peso_muñeca

suma_pesos=peso_total_payasos+peso_total_muñecas
print(f"el peso total de la venta es de  {suma_pesos}")


#cera un progama que tenga variable "te quiero amigo" 

texto="te quiero solo como amigo"
print (texto)
print ("------------------")
print("total de caracteres" ,len (texto))
print ("------------------")
print("2 primeras letras son " + texto[0:2])
print ("------------------")
print("los ultimos 3 caracteres son "+texto[22:25])
print ("------------------")
print ("cadena cada dos caracteres ")
for i  in range(0,len(texto),2):
    print(texto[i]+" = "+str(i))
    
print ("------------------") 
print("sentido inverso") 
for i in range(len(texto) - 1, -1, -1):
    print(texto[i] +" = "+ str(i))

print ("------------------") 
print("un sentido y sentido inverso")

print(texto[0:25])
print(texto[25::-1])

print ("------------------")
print ("cadena separada por una coma ")
for i  in range(0,len(texto)):
    print(texto[i]+",",end='')