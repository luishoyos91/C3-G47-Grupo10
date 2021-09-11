#Leer una lista de estudiantes

lista = []
while(True):
    opcion =""
    nombre = input("Escriba el nombre =>")
    identidad = input("Escriba la identidad =>")
    estudiante = {"nombre":nombre, "identidad":identidad}
    lista.append(estudiante)
    while(opcion!="SI" and opcion!="NO"):
        opcion = input("Desea continuar? SI/NO =>").upper()
        if (opcion == "NO"):
            break
        break
print(estudiante)