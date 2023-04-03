import pandas as pd

# Carrega o arquivo Excel
df = pd.read_excel('D:\dados_projetos\dados_calculo_imc.xlsx')

# Seleciona as colunas com os pesos e alturas
pesos = df['Peso']
altura = df['Altura']

# Solicita o nome do usuário
nome_usuario = input('Digite seu nome: ')

# Calcula o IMC para cada peso e altura usando a função zip()
for peso, altura in zip(pesos, altura):
    imc = peso / altura ** 2
    print( nome_usuario + " com {:.1f} kg e altura de {:.2f}, o seu IMC é: {:.2f}".format(peso, altura, imc))
    print(f"Seu peso ideal é: {imc*altura**2:.1f} kg")