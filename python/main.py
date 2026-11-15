plantacoes = []
opcao = '0'

while opcao != '5':
    
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
                
            print('Plantação', nome, 'cadastrada com sucesso!')
            print('Cidade:', cidade)
            print('Estado:', estado)
            print('Cultivo:', cultivo)
            
            dados_plantacao = [nome, cidade, estado, cultivo]
            plantacoes.append(dados_plantacao)
            
        case '2':
            print('===== Plantações cadastradas =====')
            if len(plantacoes) == 0:
                print('Nenhuma plantação cadastrada!')
            else:
                for plantacao in plantacoes:
                    print ('Nome: ', plantacao[0])
                    print ('Cidade: ', plantacao[1])
                    print ('Estado: ', plantacao[2])
                    print ('Cultivo: ', plantacao[3])
                                
        case '3':
            print('===== Verificação de umidade do solo =====')
            umidade = float(input('Digite a umidade do solo (%): '))
            print('Umidade informada: ', umidade)
            
        case '4':
            print('Você selecionou orientações de irrigação')
        case '5':
            print('Encerrando o AgroAlert')
        case _:
            print('Opção inválida!')
    




            
        
            
             
        
            

