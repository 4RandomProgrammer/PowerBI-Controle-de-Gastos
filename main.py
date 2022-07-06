#Ideia:
#Criar um programa que facilite o preenchimento da planilha de controle de gastos.
#A ideia inicial seria criar um programa que possa atualizar a planilha, cria-la caso não existir.
#Outras funções seriam ter uma interface gráfica(?) e abrir a planilha diretamente de controle de gastos.

import pandas as pd

planilha = None

#Função responsável por inicializar o programa
def init():
    #Importando a planilha
    try: 
        planilha = pd.read_excel(r'./Controle de Gastos.xlsx')

    except FileNotFoundError as error:
        #Caso a planilha não exista, cria-la vazia.
        print('Planilha não foi encontrada portanto criando uma nova planilha')
        planilha = pd.DataFrame(columns=['Data','Com o que foi gasto','Dinheiro Gasto'])
        planilha.to_excel('Controle de Gastos.xlsx')


#Função para adicionar uma linha DataFrame:
def addRow(date, rotulo, quantia):
    addedRow = {
        'Data':date,
        'Com o que foi gasto': rotulo,
        'Dinheiro Gasto': quantia
    }

    try:
        planilha = planilha.append(addedRow)
    except:
        print('Não foi possivel adicionar uma linha.')


#Main
