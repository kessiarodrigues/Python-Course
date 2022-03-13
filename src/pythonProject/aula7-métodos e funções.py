def soma(n1, n2):
    resp = n1 + n2
    return resp

retorno = soma(75,1289)

print (retorno)
---------------------------------------------------------------------------------------------------------

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False


print (tem_sete_itens("1234567"))        #OU ENTÃO MODELO DE BAIXO

#OU

if tem_sete_itens('1234567'):
    print ('tem sete itens')


