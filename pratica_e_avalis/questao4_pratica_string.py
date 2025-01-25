palavra = input()


def palavra_composta(palavra):
    return palavra[:2] + palavra[-2:]


nova_palavra = palavra_composta(palavra)
print(nova_palavra)