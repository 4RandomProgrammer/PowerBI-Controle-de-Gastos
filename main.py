#Ideia:
#Criar um programa que facilite o preenchimento da planilha de controle de gastos.
#A ideia inicial seria criar um programa que possa atualizar a planilha, cria-la caso não existir.
#Outras funções seriam ter uma interface gráfica(?) e abrir a planilha diretamente de controle de gastos.

import pandas as pd
import datetime



#Função responsável por inicializar o programa
def init():
    #Importando a planilha
    try: 
        planilha = pd.read_excel(r'./Controle de Gastos.xlsx')


    except:
        
        #Caso a planilha não exista, cria-la vazia.
        print('Planilha não foi encontrada portanto criando uma nova planilha')
        planilha = pd.DataFrame(columns=['Data','Com o que foi gasto','Dinheiro Gasto'])

        update()
    
    return planilha



#Função para adicionar uma linha DataFrame:
def addRow(planilha ,date, rotulo, quantia):

    addedRow = {
        'Data': date.strftime("%x"),
        'Com o que foi gasto': rotulo,
        'Dinheiro Gasto': quantia
    }

    try:
        planilha = planilha.append(addedRow,ignore_index=True)
        update()

    except Exception as e:
        print(e)
        print('Não foi possivel adicionar uma linha.')

    else:
        print("Linha adcionada com sucesso!")

#Função para escrever a planilha do execel
def update():
    try:
        planilha.to_excel('Controle de Gastos.xlsx')
    except:
        print("Erro ao Atualizar")
    

#Main
if __name__ == "__main__":
    
    planilha = init()

    while True:

        print('O que você deseja fazer?')
        print('1 - Adicionar linha de Gastos')
        print('2 - Remover coluna')
        print('3 - Abrir dashboard')
        print('4 - Sair do programa')

        try:
            read = int(input())
            
            if read == 1:
                while True:
                    try:
                        quantia = float(input("Digite o valor gasto: "))

                        rotulo = str(input("Digite com o que foi gasto: "))

                        dia = int(input("Digite o dia: "))
                        mes = int(input("Digite o mes: "))
                        ano = int(input("Digite o ano: "))

                        data = datetime.date(ano,mes,dia)


                        addRow(planilha,data, rotulo, quantia)


                    except Exception as e:
                        print(e)
                        print("Valor Inválido!")

                    else:
                        break


            elif read == 4:
                print('Obrigado por utilizar o programa!')
                break
            else:
                print("Opção ainda não implementada KK")

        except:
            print('Opção Inválida tente novamente!')
