#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional) baixo <4, razoável >6, boa >7



def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas do aluno (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notas_alunos = dict()
    total = sum(num)
    notas_alunos['total'] = len(num)
    notas_alunos['maior'] = max(num)
    notas_alunos['menor'] = min(num)
    notas_alunos['media'] = total/len(num)
    if sit:
        if notas_alunos['media'] >= 7:
            notas_alunos['situacao'] = 'BOA'
        elif notas_alunos['media'] >= 5:
            notas_alunos['situacao'] = 'RAZOÁVEL'
        elif notas_alunos['media'] == 4:
            notas_alunos['situacao'] = 'BAIXO'
        else:
            notas_alunos['situacao'] = 'RUIM'

    return notas_alunos



#Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)





