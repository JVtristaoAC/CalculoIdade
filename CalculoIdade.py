

from pickletools import int4

# Criando a variável idade que vai ser igual o input do usuário
idade = input('insira a sua idade: ')
# mostrando na tela a idade definida
print('Essa é a sua idade: ', idade)

# criando funções:
def decada(NVidade):
   NVidade = int(idade) + 10
   print('sua idade vai ser:' , str(NVidade))

def quadrado(NVidade):
    NVidade = int(idade) ** 2
    print('sua idade vai ser:' , str(NVidade))

def dobro(NVidade):
    NVidade = int(idade) * 2
    print('sua idade vai ser:' , str(NVidade))

# Criando a variável funcao que vai ser igual o input do usuário
funcao = input('O que deseja Fazer com sua idade: ')

# Mesmo esquema do switch, com o diferencial que se chama match
match funcao:
    case 'decada':
        decada(idade)
        
    case 'quadrado':
        quadrado(idade)
        
    case 'dobro':
        dobro(idade)

    # por padrão    
    case _:
        print('comando não reconhecido')

# Mesma função mais em if else

# if funcao == 'decada':
#     decada(idade)
    
# elif funcao == 'quadrado':
#     quadrado(idade)

# elif funcao == 'dobro':
#     dobro(idade)

# else:
#     print('comando não reconhecido')


# mt importante a tabeação além de deixar mt lindo como diria o zen do python bonito é melhor que feio