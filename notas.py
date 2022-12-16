
#Implemente esse pseudocódigo num script de python e carregue ele no seu repositório da prova com o nome notas.py. 
#Calcule o md5sum  do seu script e coloque esse número também como resposta desta pergunta.


lista_de_notas = []  #No primeiro ponto temos a criação de uma lista para alocar os valores (notas), adicionados pelo usuário.

for nota in range(10):#Range(10) estabelece que a lista necessita conter 10 valores dentro dela.
 nota=float(input("Insira sua nota de prova: ")) #Aqui é a interface com usuário. É para adicionar as notas das provas. 
  
 if nota < 0 or nota > 10:#Aqui estabelesce que as notas não devem estar fora do intervalo de 0 a 10, [0,10]. 
  print("A nota precisa ser menor ou igual a 10!")# Se o intervalo não for respeitado essa parte acaba por rodar. Ele mostrará ao usuário a mensagem
  nota=float(input("insira sua nota na prova: ")) # A mensagem é exposta é o usuário pode continuar colocando suas notas. 
 else:
  lista_de_notas.append(nota) #Se a nota estiver nos parâmetros estabelescidos, ela vem para esse "bloco". As notas são adicionadas na lista
  média_da_disciplina=sum(lista_de_notas)/10 #Aqui a média das 10 notas inseridas é calculada.

print("A média final da disciplina é: ", média_da_disciplina)  #A média final é estabelecida.

#código md5sum = 7ed118f4abe2699ef5d694567d3241d0