NU_ANO_INGRESSO = 0 
NU_DIA_NASCIMENTO = 1
NU_MES_NASCIMENTO = 2
NU_ANO_NASCIMENTO = 3
TP_SEXO = 4 
TP_SITUACAO = 5

operacao = int(input())
qtd_dados = int(input())
dados = []

for _ in range(qtd_dados):
    dados.append([int(i) for i in input().split()])

def alunos_regulares(dados):
    porcent_regulares = 0
    porcent_outras_situ = 0

    for aluno in dados:
        if aluno[TP_SITUACAO] == 6 or aluno[TP_SITUACAO] == 2:
            regulares += 1
        else:
            outras_situ += 1
    
    porcent_regulares = (porcent_regulares * 100) / len(dados)
    porcent_outras_situ = (porcent_outras_situ * 100) / len(dados)

    return [porcent_regulares, porcent_outras_situ]


match operacao:
    case 1: 
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7: