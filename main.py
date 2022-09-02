import parte_a
import parte_b

with open('texto.txt', 'r') as file:
    texto = file.read().replace('\n', '')

lista = texto.split("/")

print(len(lista)) 

opcion = 0


try:
    opcion = int(input("1- Parte A. \n2- Parte B.\n3- Salir\n"))
    
    if opcion == 1:
      buscar = input("Ingrese la palabra que desea buscar. \n")
      parte_a.leer_archivo(lista, buscar)
    elif opcion == 2:
      try:
        linea_texto = int(input("Ingrese linea de texto a buscar (indice de lista). \n"))
        buscar = input("Ingrese la palabra que desea buscar. \n")
        parte_b.buscar_palabra_en_linea(lista[linea_texto], buscar)
      except:
        print("Debe ingresar un numero")
  
except:
  print("Debe ingresar un numero")



