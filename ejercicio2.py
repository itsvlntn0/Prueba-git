from xml.dom.minidom import Document


def lectura():
    with open('gestiondatos.txt','r') as txt:
        datos = txt.readlines()
        return datos 

def insertar():
    with open('gestiondatos.txt','a')as txt:
        documento = input("Digite su numero de documento: ")
        nombre = input("Digite sus nombres: ")
        apellido = input("Digite sus apellidos: ")
        correo = input("Digite su correo: ")
        celular = input("Digite su numero telefonico: ")
        cont = 0 
        lista = []

        if len(lista) > 0:

            for i in lista:
                if i.strip() == documento:
                    cont+=1
                    if cont>0:
                        print("El registro ya existe")

                else:
                    txt.write (documento +'\n')
                    txt.write (nombre +'\n')
                    txt.write (apellido +'\n')
                    txt.write (correo +'\n')
                    txt.write (celular +'\n')
                    lista = lectura()

        else:
                    txt.write (documento +'\n')
                    txt.write (nombre +'\n')
                    txt.write (apellido +'\n')
                    txt.write (correo +'\n')
                    txt.write (celular +'\n')    

insertar()


                    
def buscar ():

    i = 0
    lista =[]
    lista = insertar()

    nombre = input("Que nombre desea consultar: ")

    for i in lista:
        if i.strip()==nombre:
            x= 1
            indoc = lista.index(nombre+ '\n')
            print("\nLos datos del nombre buscado son: ")
            print("Documento: " + lista[indoc].strip())
            print("Nombres: " + lista[indoc + 1].strip())
            print("Apellidos: " + lista[indoc + 2].strip())
            print("Correo: " + lista[indoc + 3].strip())
            print("Celular: " + lista[indoc + 4].strip())
        
        if x == 0:
            print("El nombre no existe")

        
