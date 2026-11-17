import os

# Lista responsável por armazenar os dados das plantações
plantacoes = []
opcao = '0'

# Mantém o menu em execução até o usuário escolher sair
while opcao != '5':
    
    os.system('cls')
    
    print('======= Bem-vindo ao AgroAlert! ======= ')
    print('1 - Cadastrar plantação')
    print('2 - Consultar plantações')
    print('3 - Verificar umidade do solo')
    print('4 - Orientações de irrigação')
    print('5 - Sair')
    
    opcao = input('Escolha uma opção: ')
    
    match opcao:
        case '1':
            print('===== Cadastro de plantação =====')
            nome = input('Nome da plantação: ')
            while nome == '':
                print('O nome não pode ficar vazio!')
                nome = input('Digite o nome da plantação novamente: ')
                
            cidade = input('Cidade: ')
            while cidade == '':
                print('Cidade não pode ficar vazia!')
                cidade = input('Digite a cidade novamente: ')
                
            estado = input('Estado: ')
            while estado == '':
                print('O estado não pode ficar vazio!')
                estado = input('Digite o estado novamente: ')
                
            cultivo = input('Tipo de cultivo: ')
            while cultivo == '':
                print('O cultivo não pode ficar vazio!')
                cultivo = input('Digite o cultivo novamente: ')
                
            
            
            # Armazena as informações da plantação cadastrada
            dados_plantacao = [nome, cidade, estado, cultivo]
            plantacoes.append(dados_plantacao)
            
            # Limpa os campos preenchidos e exibe o resumo do cadastro
            os.system('cls')
            
            print('===== Plantação cadastrada com sucesso! =====')
            print()
            print('Nome:', nome,)
            print('Cidade:', cidade)
            print('Estado:', estado)
            print('Cultivo:', cultivo)
            print('---------------------------------------------')
            
            
            
        case '2':
            print('===== Plantações cadastradas =====')
            
            if len(plantacoes) == 0:
                print('Nenhuma plantação cadastrada!')
            else:
                for plantacao in plantacoes:
                    print()
                    print ('Nome: ', plantacao[0])
                    print ('Cidade: ', plantacao[1])
                    print ('Estado: ', plantacao[2])
                    print ('Cultivo: ', plantacao[3])
                    print('------------------------------')
                                
        case '3':
            print('===== Verificação de umidade do solo =====')
            umidade = float(input('Digite a umidade do solo (%): '))
            
            # Verifica se a umidade está entre 0% e 100%
            while umidade < 0 or umidade > 100:
                print('Umidade inválida! Digite um valor entre 0 e 100')
                umidade = float(input('Digite a umidade novamente (%): '))
                
            if umidade < 30:
                print('Umidade Baixa')
            elif umidade <= 70:
                print('Umidade Moderada') 
            else:
                print('Umidade alta')
                      
            
        case '4':
            print('===== Orientação de irrigação =====')
            umidade_irrigacao = float(input('Digite a umidade do solo (%): '))
            
            while umidade_irrigacao < 0 or umidade_irrigacao > 100:
                print('Umidade inválida!')
                umidade_irrigacao = float(input('Digite novamente: '))
            print('Umidade informada: ', umidade_irrigacao)
            
            # Exibe orientações de irrigação conforme a umidade informada
            if umidade_irrigacao < 30:
                print('Atenção! Verifique a necessidade de irrigação')
            elif umidade_irrigacao <= 70:
                print('Umidade moderada. Continue monitorando o solo')
            else:
                print('Umidade alta. Evite irrigação desnecessária')
            
            
            
        case '5':
            print('Encerrando o AgroAlert')
        case _:
            print('Opção inválida!')
            
    if opcao != '5':
        input('\nPressione ENTER para voltar ao menu...')
     
    




            
        
            
             
        
            

