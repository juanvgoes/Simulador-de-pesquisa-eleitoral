from time import sleep
#falta muita coisa ainda visse
lista = []
encerrar = False

print('Pesquisa eleitoral')
print('Defina abaixo as informações necessárias')

i = 1
while True:
    while True:
        candidato = input(f'[Obrigatório] Nome do candidato {i}: ')
        if (candidato.replace(' ', '')).isalpha():
            break
        else:
            if (candidato.replace(' ', '')).isalnum() or (candidato.replace(' ', '')).isnumeric():
                print('VALOR INVALIDO, NÃO É PERMITIDO NÚMEROS NO NOME DO CANDIDATO')
            else:
                print('VALOR INVALIDO, É NECESSÁRIO PREENCHER O NOME DO CANDIDATO')
    vice = input(f'Qual o vice de {candidato}? ')
    partido = input(f'Qual o partido de {candidato}? ')

    while True:
        try:
            votos = int(input(f'[obrigatório] Quantos votos {candidato} tem até o momento? '))
            break
        except ValueError:
            print('VALOR INVALIDO, É NECESSÁRIO PREENCHER O NÚMERO DE VOTOS DO CANDIDATO')
            sleep(1)
            continue
        
    if vice.strip() == '':
        vice = 'Sem vice'

    if partido.strip() == '':
        partido = 'Sem partido'

    lista.append([candidato, vice, partido, votos])

    decisao_repetir = input('Deseja adicionar outro candidato? [S/N] ')

    while True:
        if decisao_repetir.lower().strip() == 's' or decisao_repetir.lower().strip() == 'sim':
            print('\n-------------------------------\n')
            break
        elif decisao_repetir.lower().strip() == 'n' or decisao_repetir.lower().strip() == 'não':
            encerrar = True
            break
        else:
            print('Digite um valor válido, apenas sim (ou S) ou não (ou N)')

    if encerrar:
        break        
    i += 1


print('As informações recebidas foram as seguites:')
for c in range(len(lista)):
    print(f'Candidato(a): {lista[c][0]}')
    for c in range(3):
        print(f'Vice: {lista[c][1]}')
        print(f'Partido: {lista[c][2]}')
        print(f'Votos até o momento: {lista[c][3]}')
    print('----------------------------------')

