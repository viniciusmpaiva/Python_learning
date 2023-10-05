perguntas = [
    {
        'Pergunta': 'Quanto é 10*10? ',
        'Opções': ['1000','100','10','1'],
        'Resposta': '100',    
    },

    {
        'Pergunta': 'Qual capital do estado de São Paulo?',
        'Opções': ['São Paulo','Rio de Janeiro','Campinas','Florianoplois'],
        'Resposta': 'São Paulo',    
    },

    {
        'Pergunta': 'Quanto é 20/5?',
        'Opções': ['2','10','25','4'],
        'Resposta': '4'    
    },
]

def opcao(perg,ordem_perguntas):
    pergunta_atual = perg[ordem_perguntas]['Pergunta']
    print(f'{pergunta_atual}\n')
    print('Opções')
    for i, value in enumerate(perg[ordem_perguntas]['Opções']):
        print(f'{i}) {value}')

    try:
        escolha =int(input('Escolha uma opção: '))
    except:
        print('Opção Inválida!')
        return
    try:
        resposta = perg[ordem_perguntas]['Opções'][escolha] 
    except:
        print('Opção Inválida!')
        return    
    return resposta
    

numero_pergunta = 0
acertou = 0 
while numero_pergunta<=2:
    resposta = opcao(perguntas,numero_pergunta)
    if resposta is None:
        print('=-'*30)
        print('\n')
        continue
    if resposta == perguntas[numero_pergunta]['Resposta']:
        print('Acertou!')
        acertou+=1
    else:
        print('Errado!')
    numero_pergunta+=1
    print('=-'*30)
    print('\n')
            
print(f'Você acertou {acertou} de 3 perguntas!')


