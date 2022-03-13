print ('------CONTROLE DE CONVIDADOS------')



convidados = input ('Quantos convidados serão?: ')
lista_convidados = []
i = 1
while i <= int(convidados):                         #FOR I IN RANGE(INT(CONVIDADOS)):
    nome = input ('Nome do convidado # '+ str(i) +': ')
    lista_convidados.append (nome)
    i +=1

print ('\n------LISTA------')
for convidado in lista_convidados:
    print (convidado)