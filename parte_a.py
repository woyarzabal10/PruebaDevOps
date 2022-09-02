def leer_archivo(lista, palabra):
  for i in lista:
    
    if i.find(palabra) != -1:
      print("La palabra se encuentra en el texto")
      return
  print("No se encontro la palabra")

  

  