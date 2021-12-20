def pesquisa_binaria(lista, item):
  # baixo e alto acompanham a parte da lista que você está procurando
  baixo = 0
  alto = len(lista) - 1
  #enquanto não se achar o elemento...
  while baixo <= alto:
    #... verifica-se o elemento central
    meio = (baixo + alto) / 2
    chute = lista[meio]
    #acha o item
    if chute == item:
      return meio
    # chute muito alto
    if chute > item:
      alto = meio - 1
    # chute muito baixo
    else:
      baixo = meio + 1
   # o  item não existe
   return None
