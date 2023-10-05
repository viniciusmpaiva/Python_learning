def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom Dia')
falar_boa_noite = criar_saudacao('Boa Noite')
#closure
for nome in ['Maria','João','Vinicius','Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
