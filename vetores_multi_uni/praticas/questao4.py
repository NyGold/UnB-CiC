def paron(lista):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = []
    
    for palavra in lista:
        num_vogais = 0
        
        for letra in palavra:
            if letra in vogais:
                num_vogais += 1
                
        if num_vogais % 2 == 0:
            res.append(palavra)
    
    return res