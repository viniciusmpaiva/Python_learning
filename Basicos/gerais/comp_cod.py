#CONSTANTE = variaveis que não vão mudar - Convensão:
#LETRA MAUIÚSCULA: 
RADAR_1 = 60
LOCAL_1 = 100
RADAR_ALNCANCE = 1
#Não colocar muitas condições no mesmo if
#EVitar dar muita complexidade ao código (muitas coisas dentro das outras)
velocidade = 61
local_carro = 100

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_r1 = local_carro >= (LOCAL_1 - RADAR_ALNCANCE) and \
        local_carro <=(LOCAL_1 + RADAR_ALNCANCE) 
carro_multado_r1 = carro_passou_r1 and velocidade_carro_passou_radar_1
if velocidade_carro_passou_radar_1:
        print('Velocidade carro passou do radar 1')

if carro_passou_r1:
        print('Carro passou radar 1')

if carro_multado_r1:
        print('carro multado em radar 1')