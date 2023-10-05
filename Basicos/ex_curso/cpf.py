while True:
    cpf_inserido = input('Digite o CPF: ').replace('.', '')
    if cpf_inserido == cpf_inserido[0] * len(cpf_inserido):
        print('CPF inválido')
        continue
    nove_digitos = cpf_inserido[:9]
    cpf_size = len(cpf_inserido)
    verification_cpf = cpf_inserido.isnumeric()
    if verification_cpf is False:
        print('CPF inválido! O CPF não pode conter letras!')
        continue
    if cpf_size != 11:
        print('CPF inválido! O CPF deve ter 12 algarismos')
        continue
    i_1 = 0
    m_1 = 10
    soma_1 = 0
    num_CPF = []
    while i_1 <=8:
        num_CPF.append(int(cpf_inserido[i_1]))
        num_CPF[i_1] = num_CPF[i_1] * m_1
        soma_1 += num_CPF[i_1]
        i_1+=1
        m_1-=1
    res_1 = (soma_1 *10)%11

    first_digit = res_1 if res_1<=9 else 0
    print(f'O primeiro digito do CPF é {first_digit}')

    i_2 = 0
    m_2 = 11
    soma_2 = 0
    num_CPF_2 = []
    while i_2<=8:
        num_CPF_2.append(int(cpf_inserido[i_2]))
        num_CPF_2[i_2] = num_CPF_2[i_2] * m_2
        soma_2 += num_CPF_2[i_2]
        i_2+=1
        m_2-=1
    soma_2 += (first_digit * 2)
    res_2 = (soma_2 *10) % 11
    second_digit = res_2 if res_2<=9 else 0

    print(f'O segundo digito é {second_digit}')

    cpf_final = f'{nove_digitos}{first_digit}{second_digit}'

    if cpf_final == cpf_inserido:
        print(f'O CPF {cpf_final} é válido!')
    else:
        print('CPF inválido!')

    


      
