#w = se rescriben los datos
#a = guarda los datos 
#r = leer datos

with open ('datos.txt', 'a') as txt:
    txt.write("Buenas tardes \n")
    txt.write("Hola python \n")
    texto = input("Digite un texto: ")
    txt.write(texto + '\n')
    num1 = int(input("Digite un numero: "))
    num2 = int(input("Digite un numero: "))
    resultado = num1 + num2
    txt.write(str(resultado) + '\n')

with open ('datos.txt', 'r') as txt:
    lectura = txt.read()
    print(lectura)