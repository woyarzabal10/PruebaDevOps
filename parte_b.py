def buscar_palabra_en_linea(linea_de_texto, palabra_buscada):
  cont = 0
  flag = True
  indice = 0

  while flag:
    encontro = linea_de_texto.find(palabra_buscada, indice)
    if encontro == -1:
      flag = False
    else:
      cont += 1
      indice = encontro + 1
    
  if cont > 0:
    print("La palabra encuentra " + str(cont) + " en el texto.")
  else:
    print("La palabra no se encuentra en el texto")
    
    
    

  

