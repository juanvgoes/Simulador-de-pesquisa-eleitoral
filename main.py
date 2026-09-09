from ast import While
from time import sleep
#falta muita coisa ainda visse
lista = []
lista_porcentagem = []
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

    while True:
        decisao_repetir = input('Deseja adicionar outro candidato? [S/N] ')
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
    print(f'Vice: {lista[c][1]}')
    print(f'Partido: {lista[c][2]}')
    print(f'Votos até o momento: {lista[c][3]}')
    print('----------------------------------')

total_votos = 0
for c in range(len(lista)):
    total_votos += lista[c][3]

print(f'Total de votos: {total_votos}')

for c in range(len(lista)):
    porcentagem = (lista[c][3] / total_votos) * 100
    lista_porcentagem.append(porcentagem)
    lista[c].append(porcentagem)

i = c = 0
while i < len(lista):
    if lista[c][4] == lista_porcentagem[i]:
        print(f'{lista[c][0]} tem {lista[c][4]:.2f}% dos votos, e está em {i + 1} lugar')
        i += 1
        c = 0
    else:
        c += 1

