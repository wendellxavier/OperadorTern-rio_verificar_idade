idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    msg = 'Pode acessar' if maior_de_idade else 'Não pode acessar'
    print(msg)