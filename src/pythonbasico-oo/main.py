from veiculo import Veiculo
from carro import Carro


caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

fuscão_preto = Veiculo('preto', 4, 'Volkswagen', 40)



print ('CAMINHÃO ROSA')
print ('Cor: ', caminhao_rosa.cor)
print ('Marca: ', caminhao_rosa.marca)
print ('Tanque', caminhao_rosa.tanque)


print ('FUSCÃO PRETO')
print ('Cor: ', fuscão_preto.cor)
print ('Marca: ', fuscão_preto.marca)
print ('Tanque', fuscão_preto.tanque)
fuscão_preto.abastecer(35)
print ('Tanque', fuscão_preto.tanque)


