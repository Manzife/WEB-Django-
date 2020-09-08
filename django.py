#criar um ordenador que recebe os alimentos desejados e devolve em um ordem por tipo de local

# Pedir pro usuário qual alimento, a quantidade, e se tem alguma observação
item = input("Olá, qual é o item que você quer acrescentar na lista?: ")

#definindo set com o nome dos alimentos 
lista_verduras = {"abobrinha", "beringela", "tomate"}
lista_frutas = {"maça", "banana", "abacate"}
lista_panificação = {"pão", "bolo", "pizza"}

frutas = []
verduras = []
panificação = []


#verificando em qual tipo categoria está o item 
if item in lista_verduras:
    verduras.append(item)
    print(" rodou verduras " + item)

elif item in lista_frutas:
    frutas.append(item)
    print ("rodou frutas: " + item)

elif item in lista_panificação:
    panificação.append(item)
    print("rodou panificação: " + item)
    

# Ver em que categoria se enquadra esse item 

resposta = list(input("digite sim para confirmar ou digite não para trocar o item, \n se for mais de um item coloque no formato 'banana, 'abacate' : "))

#função que vai ordernar as frutas pedidas

                
def ordenar(v = verduras,f = frutas, p =  panificação):
    global ordem
    ordem = v + f + p 
        

def sua_lista(ordem):
    ordenar(verduras,frutas,panificação)
    print("você tem em sua lista de compras: " "\n" + "frutas" + frutas + "\n" + "verduras" + "verduras na seguinte oredem ideal" + ordem )
    global resposta
    resposta = input("digite sim para confirmar ou digite não para trocar o item, \n se for mais de um item coloque no formato 'banana, 'abacate' : ")
    print(resposta)


def corrigir(r = resposta, v = verduras, f = frutas, p = panificação):
    
    if resposta != "sim":
        for i in resposta:
            if i in verduras:
                del(verduras[i])
            if i in frutas:
                del(frutas[i])
            if i in panificação: 
                del[panificação[i]]
            else: 
                print("esse item ainda não está no supermercado")

    else:     
        #vai retornar erro se for não 
        #ordenar
        print("sua ordem de compras é: " + ordem )
    
corrigir(resposta,verduras,frutas,panificação)
