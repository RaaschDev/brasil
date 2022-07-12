import random
import datetime as dt

def verificaPlayersInativos(players):
    playersInativo = 0
    for player in players:
        if players[player]['Status'] == 'Inativo':
            playersInativo += 1
    return playersInativo

def calVencedorTimeOut(players):
    valorMax = 0
    for player in players:
        if valorMax < players[player]['Saldo']:
            valorMax = players[player]['Saldo']
    res = {}
    for key, player in players.items():
        if player['Saldo'] == valorMax:
            res[key] = valorMax
    if len(res) > 1:
        ordemplayer = 4
        for player in res:
            if players[player]['Ordem'] <= ordemplayer:
                ordemplayer = players[player]['Ordem']
                vencedor = player
    else:
        for player in res:
            vencedor = player
    return vencedor

def porcentoVitorias(numWinPlayer, resume):
    media = (numWinPlayer / len(resume['Vencedores'])) * 100
    return media

ordemplayers = ['Player1', 'Player2', 'Player3', 'Player4']
random.shuffle(ordemplayers)
resume = {'PartidasConcTimeOut': 0, 'Numturns': [], 'Vencedores': []}
for simulacaoNum in range(300):
    numRodada = 0
    concTimeOut = False
    players = {'Player1': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Impulsivo'},
               'Player2': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Exigente'},
               'Player3': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Cauteloso'},
               'Player4': {'Saldo': 300, 'Posicao': -1, 'Status': 'Ativo', 'Comportamento': 'Aleatorio'}}
    tab = ['Propriedade 01', 'Propriedade 02', 'Propriedade 03', 'Propriedade 04', 'Propriedade 05',
           'Propriedade 06', 'Propriedade 07', 'Propriedade 08', 'Propriedade 09', 'Propriedade 10',
           'Propriedade 11',
           'Propriedade 12', 'Propriedade 13', 'Propriedade 14', 'Propriedade 15', 'Propriedade 16',
           'Propriedade 17',
           'Propriedade 18', 'Propriedade 19', 'Propriedade 20']
    infoProp = {'Propriedade 01': {'Venda': 210, 'Aluguel': 42, 'Proprietario': None, 'Posicao': 0},
                'Propriedade 02': {'Venda': 210, 'Aluguel': 42, 'Proprietario': None, 'Posicao': 1},
                'Propriedade 03': {'Venda': 220, 'Aluguel': 44, 'Proprietario': None, 'Posicao': 2},
                'Propriedade 04': {'Venda': 220, 'Aluguel': 44, 'Proprietario': None, 'Posicao': 3},
                'Propriedade 05': {'Venda': 230, 'Aluguel': 46, 'Proprietario': None, 'Posicao': 4},
                'Propriedade 06': {'Venda': 230, 'Aluguel': 46, 'Proprietario': None, 'Posicao': 5},
                'Propriedade 07': {'Venda': 240, 'Aluguel': 48, 'Proprietario': None, 'Posicao': 6},
                'Propriedade 08': {'Venda': 240, 'Aluguel': 48, 'Proprietario': None, 'Posicao': 7},
                'Propriedade 09': {'Venda': 250, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 8},
                'Propriedade 10': {'Venda': 250, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 9},
                'Propriedade 11': {'Venda': 255, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 10},
                'Propriedade 12': {'Venda': 255, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 11},
                'Propriedade 13': {'Venda': 255, 'Aluguel': 50, 'Proprietario': None, 'Posicao': 12},
                'Propriedade 14': {'Venda': 260, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 13},
                'Propriedade 15': {'Venda': 260, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 14},
                'Propriedade 16': {'Venda': 260, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 15},
                'Propriedade 17': {'Venda': 265, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 16},
                'Propriedade 18': {'Venda': 265, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 17},
                'Propriedade 19': {'Venda': 265, 'Aluguel': 52, 'Proprietario': None, 'Posicao': 18},
                'Propriedade 20': {'Venda': 270, 'Aluguel': 54, 'Proprietario': None, 'Posicao': 19}}
    playersInativo = 0
    while playersInativo != 3:
        for player in ordemplayers:
            if players[player]['Status'] == 'Inativo':
                continue
            players[player]['Posicao'] += random.randrange(1, 7)
            if players[player]['Posicao'] >= 20: 
                players[player]['Saldo'] += 100
                players[player]['Posicao'] -= 20 
            if infoProp[tab[players[player]['Posicao']]]['Proprietario'] == None:
                if players[player]['Comportamento'] == 'Impulsivo':
                    if (players[player]['Saldo'] - infoProp[tab[players[player]['Posicao']]]['Venda']) >= 0:
                        players[player]['Saldo'] = players[player]['Saldo'] - \
                            infoProp[tab[players[player]['Posicao']]]['Venda']
                        infoProp[tab[players[player]['Posicao']]
                                 ]['Proprietario'] = player
                    else:
                        pass
                elif players[player]['Comportamento'] == 'Exigente':
                    if (players[player]['Saldo'] - infoProp[tab[players[player]['Posicao']]]['Venda']) >= 0:
                        if infoProp[tab[players[player]['Posicao']]]['Aluguel'] >= 50:
                            players[player]['Saldo'] = players[player]['Saldo'] - \
                                infoProp[tab[players[player]
                                             ['Posicao']]]['Venda']
                            infoProp[tab[players[player]['Posicao']]
                                     ]['Proprietario'] = player
                        else:
                            pass
                    else:
                        pass
                elif players[player]['Comportamento'] == 'Cauteloso':
                    if (players[player]['Saldo'] - infoProp[tab[players[player]['Posicao']]]['Venda']) >= 80:
                        players[player]['Saldo'] = players[player]['Saldo'] - \
                            infoProp[tab[players[player]['Posicao']]]['Venda']
                        infoProp[tab[players[player]['Posicao']]
                                 ]['Proprietario'] = player
                    else:
                        pass
                elif players[player]['Comportamento'] == 'Aleatorio':
                    if (players[player]['Saldo'] - infoProp[tab[players[player]['Posicao']]]['Venda']) >= 0:
                        if random.randrange(0, 2) == 1:
                            players[player]['Saldo'] = players[player]['Saldo'] - \
                                infoProp[tab[players[player]
                                             ['Posicao']]]['Venda']
                            infoProp[tab[players[player]['Posicao']]
                                     ]['Proprietario'] = player
                        else:
                            pass
                    else:
                        pass
                else:
                    print('Comportamento Não Definido.')
                    pass
            else:
                players[player]['Saldo'] = players[player]['Saldo'] - \
                    infoProp[tab[players[player]['Posicao']]]['Aluguel']
                players[infoProp[tab[players[player]['Posicao']]]['Proprietario']]['Saldo'] = \
                    players[infoProp[tab[players[player]['Posicao']]]['Proprietario']]['Saldo'] + \
                    infoProp[tab[players[player]['Posicao']]]['Aluguel']
            if players[player]['Saldo'] < 0:
                players[player]['Status'] = 'Inativo'
                for propriedade in infoProp:
                    if infoProp[propriedade]['Proprietario'] == player:
                        infoProp[propriedade]['Proprietario'] = None

            playersInativo = verificaPlayersInativos(players)
        numRodada += 1
        if numRodada > 1000:
            resume['PartidasConcTimeOut'] += 1
            concTimeOut = True
            break
    if playersInativo == 3:
        for playerAtual in players:
            if players[playerAtual]['Status'] == 'Ativo':
                resume['Vencedores'].append(playerAtual)

    elif concTimeOut == True:
        vencedorTimeOut = calVencedorTimeOut(players)
        resume['Vencedores'].append(vencedorTimeOut)

    resume['Numturns'].append(numRodada)

totalTurns = 0
for turns in resume['Numturns']:
    totalTurns += turns
medianTurn = totalTurns / len(resume['Numturns'])
print('Partidas Concluidas por TimeOut: ' + str(resume['PartidasConcTimeOut']))
print('Quantidade de turns em Média por Simulação: ' + str(int(medianTurn)))
numWinsP1, numWinsP2, numWinsP3, numWinsP4 = 0, 0, 0, 0
for resumeVencedor in resume['Vencedores']:
    if resumeVencedor == 'Player1':
        numWinsP1 += 1
    elif resumeVencedor == 'Player2':
        numWinsP2 += 1
    elif resumeVencedor == 'Player3':
        numWinsP3 += 1
    elif resumeVencedor == 'Player4':
        numWinsP4 += 1
    else:
        print('Vencedor Desconhecido!')
        pass
print('O Comportamento ' + players['Player1']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(
    porcentoVitorias(numWinsP1, resume)) + r'% das Vezes.')
print('O Comportamento ' + players['Player2']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(
    porcentoVitorias(numWinsP2, resume)) + r'% das Vezes.')
print('O Comportamento ' + players['Player3']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(
    porcentoVitorias(numWinsP3, resume)) + r'% das Vezes.')
print('O Comportamento ' + players['Player4']['Comportamento'] + ' Ganhou ' + "{:.2f}".format(
    porcentoVitorias(numWinsP4, resume)) + r'% das Vezes.')

def players_winmax():
    playerWinMax = max(set
                       (resume['Vencedores']),
                       key=resume['Vencedores'].count)
    return playerWinMax
def return_code(playerWinMax):
    print('Comportamento com Mais Vitórias: '
          + str(players[playerWinMax]
                ['Comportamento']))
    saida = {'ConcTimeOut': int(resume['PartidasConcTimeOut']),
             'QtdmedianTurn': int(medianTurn),
             'PorcentoVitoriaComportamento': {
        players['Player1']['Comportamento']: "{:.2f}".format(porcentoVitorias(numWinsP1, resume)) + r'%',
        players['Player2']['Comportamento']: "{:.2f}".format(porcentoVitorias(numWinsP2, resume)) + r'%',
        players['Player3']['Comportamento']: "{:.2f}".format(porcentoVitorias(numWinsP3, resume)) + r'%',
        players['Player4']['Comportamento']: "{:.2f}".format(porcentoVitorias(numWinsP4, resume)) + r'%'},
        'Vencedor': playerWinMax}
    print(saida)

