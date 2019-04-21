lista = ['A', 'C', 'G', 'C', 'A', 'T', 'G', 'T', 'C', 'A', 'A', 'A', 'A', 'T', 'C', 'G']
maxi = 1
maior = []
for z in range(0,len(lista)):
    for x in range(0,len(lista)):
        if lista[z:x]:
            #print(lista[z:x])
            if len(lista[z:x])== 1:
                #print("Palindromo MONO")
                pass
            else:
                lista1 = lista[z:x]
                if(lista[z:x] == lista1[::-1]):
                    #print(lista[z:x],lista1[::-1])
                    if(len(lista[z:x])>maxi):
                        maxi = len(lista[z:x])
                        maior = lista[z:x]
print("O maior palindromo e: ",maior)
