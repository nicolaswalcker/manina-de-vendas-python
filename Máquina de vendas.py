def maquina(a, b, c, d, e):
    '''função principal da maquina (main)
    o início do programa, a lista aparece com os produtos
    aquele 'if' ali diz se o produto ta indisponível, retornando False, ele chama a função compraNovamente de novo
    no 'nome, preco' ele associa a variavel nome e preço a x da função obternome
    no dinero ele vai descontar o dinheiro na função receberdinheiro
    e no final da função maquina, ela chama a função compraNovamente para repetir o processo de compra.'''
    limpaTela()
    mostrarlista(a, b, c, d, e)
    x=int(input('Escolha um produto: '))
    if verestoque(a, b, c, d, e, x) == False:
        print('\nProduto indisponível')
        compraNovamente(a, b, c, d, e, x)
    nome, preco = obternome(x)
    dinero=receberdinheiro(preco)
    if (dinero-preco) ==0:
        print('Não há troco')
    elif (dinero-preco) > 0:
        print('\nValor pago: R${}'.format(dinero))
        print('Seu troco: R${0:.2f}\n'.format(dinero - preco))
        print('Pegue seu troco:')
    troco(dinero-preco)
    compraNovamente(a, b, c, d, e, x)



def mostrarlista(a, b, c, d, e):
    '''essa função é para a lista de produtos aparecer
    os elses são quando os produtos estão indisponíveis, aparecerem na lista para o cliente'''
    print('-'*35)
    if verestoque(a, b, c, d, e, 1):
        print('1 - Biscoito - R$2,50')
    else:
        print('1 - Biscoito - Indisponível')         #
    if verestoque(a, b, c, d, e, 2):
        print('2 - Suco - R$1,99')
    else:
        print('2 - Suco - Indisponível')
    if verestoque(a, b, c, d, e, 3):
        print('3 - Salgadinho - R$0,99')
    else:
        print('3 - Salgadinho - Indisponível')
    if verestoque(a, b, c, d, e, 4):
        print('4 - Achocolatado - R$4,99')
    else:
        print('4 - Achocolatado - Indisponível')
    if verestoque(a, b, c, d, e, 5):
        print('5 - Leite - R$3,50')
    else:
        print('5 - Leite - Indisponível')
    print('-'*35)


def obternome(n):
    '''aqui ele verifica qual o cliente escolheu e retorna o nome e o preço'''
    if n==1:
        print('\nVocê escolheu Biscoito')
        print('Preço: R$ 2,50\n')
        return 'Biscoito', 2.50
    elif n==2:
        print('\nVocê escolheu Suco')
        print('Preço: R$ 1,99\n')
        return 'Suco', 1.99
    elif n==3:
        print('\nVocê escolheu Salgadinho')
        print('Preço: R$ 0,99\n')
        return 'Salgadinho', 0.99
    elif n==4:
        print('Você escolheu Achocolatado\n')
        print('Preço: R$ 4,99\n')
        return 'Achocolatado', 4.99
    elif n==5:
        print('\nVocê escolheu Leite')
        print('Preço: R$ 3,50\n')
        return 'Leite', 3.50

def troco(n):
    '''a função troco que foi a mais demorada, pega o valor dado pelo cliente e verifica os valores
    este round é para a maquina não "roubar" alguns centavos do cliente, arredondando valores muito pequenos'''
    n=round(n,2)
    if n >=100:
        print('R$ 100,00')
        return troco(n-100)

    elif n >=50:
        print('R$ 50,00')
        return troco(n-50)

    elif n >=20:
        print('R$ 20,00')
        return troco(n-20)

    elif n >= 10:
        print('R$ 10,00')
        return troco(n-10)

    elif n >= 5:
        print('R$ 5,00')
        return troco(n-5)

    elif n >= 2:
        print('R$ 2,00')
        return troco(n-2)

    elif n >= 1:
        print('R$ 1,00')
        return troco(n-1)

    elif n >= 0.50:
        print('R$ 0,50')
        return troco(n-0.50)

    elif n >= 0.25:
        print('R$ 0,25')
        return troco(n-0.25)

    elif n >= 0.10:
        print('R$ 0,10')
        return troco(n-0.10)

    elif n >= 0.05:
        print('R$ 0,05')
        return troco(n-0.05)

    elif n >= 0.01:
        print('R$ 0,01')
        return troco(n-0.01)

    elif n==0:
        return False



def receberdinheiro(p, i=0):
    '''Essa função que é a importante, ela pede o dinheiro e verifica se foi o suficiente.
    e se não for, ela pede novamente, até chegar uma quantidade maior do produto'''
    if i < p:
        din = float(input('Coloque o dinheiro: '))
        return receberdinheiro(p, i+din)
    else:
        return i

def verestoque(a, b, c, d, e, n):
    '''essa função, verifica o estoque, a parte mais importante da maquina
    retornando verdadeiro se houver estoque e falso se não houver'''
    if n == 1:
        if a > 0:
            return True
        else:
            return False
    elif n == 2:
        if b > 0:
            return True
        else:
            return False
    elif n == 3:
        if c > 0:
            return True
        else:
            return False
    elif n == 4:
        if d > 0:
            return True
        else:
            return False
    elif n== 5:
        if e > 0:
            return True
        else:
            return False


def compraNovamente(a, b, c, d, e, x):
    '''por fim, a função que pergunta se o cliente quer comprar novamente
    coloquei os dois s e S por precaução.
    o mesmo caso no n e N'''
    rep=input('\nDeseja fazer outra compra? (S/N):')
    if rep == 's' or rep == 'S':
        if x == 1:
            return maquina(a-1, b, c, d, e)
        elif x == 2:
            return maquina(a, b-1, c, d, e)
        elif x == 3:
            return maquina(a, b, c-1, d, e)
        elif x == 4:
            return maquina(a, b, c, d-1, e)
        elif x == 5:
            return maquina(a, b, c, d, e-1)
        else:
            maquina(a, b, c, d, e)
    elif rep == 'n' or rep == 'N':
        print('\nObrigado pela compra!\nVolte sempre!')
        return

from os import system, name

def limpaTela():
    if name == 'nt':
	    system('cls')
    else:
	    system('clear')


maquina(5, 5, 5, 5, 5)

