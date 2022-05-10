from time import sleep


total = 0
masculino = 0
feminino = 0

homem_aprovado = 0
mulher_aprovado = 0

homem_reprovado = 0
mulher_reprovado = 0

homem_exame = 0
mulher_exame = 0

aprovados = 0
reprovados = 0
exame = 0

tem_proximo = "s"

while tem_proximo == "s":
    alunos = input("Digite o nome do aluno:\n> ")
    aluno = alunos.title()
    
    sexos = input("Escolha o Sexo do Aluno M/F:\n> ")
    sexo = sexos.upper()
   
    while sexo != "M" and sexo != "F":
        print("Escolha apenas M para masculino ou F para feminino")
        sexos = input("Escolha o Sexo do Aluno M/F:\n> ")
        sexo = sexos.upper()

    if sexo == "M":
        masculino += 1
        total += 1
        
    elif sexo == "F":
        feminino += 1
        total += 1
    nota_primeiro = -1
    while type(nota_primeiro) != float or nota_primeiro < 0 or nota_primeiro > 10:
        try:
            nota_primeiro = float(input("Digite a primeira nota (0/10 com decimais separados por ponto):\n> "))
            
        except:
            print("Digite um numero de 0 a 10")
    
    nota_segundo = -1
    while type(nota_segundo) != float or nota_segundo < 0 or nota_segundo > 10:
        try:
            nota_segundo = float(input("Digite a segunda nota (0/10 com decimais separados por ponto):\n> "))
            
        except:
            print("Digite um numero de 0 a 10")
    
    nota_terceiro = -1
    while type(nota_terceiro) != float or nota_terceiro < 0 or nota_terceiro > 10:
        try:
            nota_terceiro = float(input("Digite a terceira nota (0/10 com decimais separados por ponto):\n> "))
            
        except:
            print("Digite um numero de 0 a 10")
    media = (nota_primeiro + nota_segundo + nota_terceiro) / 3
    print(nota_primeiro, nota_segundo, nota_terceiro)      
    print(media)

    if media >= 7:
        print("aluno aprovado")
        aprovados += 1
        if sexo == "M":
            homem_aprovado += 1
            
        elif sexo == "F":
            mulher_aprovado += 1
    elif media >= 4 and media < 7:
        print("o aluno ficou de exame")
        exame += 1
        if sexo == "M":
            homem_exame += 1
            
        elif sexo == "F":
            mulher_exame += 1

    else:
        print("infelizmente ele foi reprovado")
        reprovados += 1
        if sexo == "M":
            homem_reprovado += 1
            
        elif sexo == "F":
            mulher_reprovado += 1
            
    proximo_aluno = input("Ir para proximo aluno? S/N:\n> ")
    proximo = proximo_aluno.upper()
    while proximo != "S" and proximo != "N":
        print("Escolha apenas S para sim ou N para nao")

        proximo_aluno = input("Ir para proximo aluno? S/N:\n> ")
        proximo = proximo_aluno.upper()

    if proximo == "S":
        tem_proximo = "s"
    elif proximo == "N":
        tem_proximo = "n"
        print("total de alunos cadastrados:", total)
        print("Percentual de alunos aprovados:", (aprovados * 100 / total), "%")
        print("percentual de alunos de exame:", (exame * 100 / total), "%")
        print("Percentual de alunos reprovados:", (reprovados * 100 / total), "%")
        
        print("total de homens aprovados:", homem_aprovado)
        print("total de mulheres aprovadas:", mulher_aprovado)
       
        print("total de homens de exame:", homem_exame)
        print("total de mulheres de exame:", mulher_exame)
       
        print("total de homens reprovados:", homem_reprovado)
        print("total de mulheres reprovados:", mulher_reprovado)

        sleep(1.5)
        
        encerrar = input("Deseja encerrar o programa? S/N:\n> ")
        fechar = encerrar.upper()
        
        while fechar != "S" and fechar != "N":
            print("Escolha S para sim ou N para não")
            encerrar = input("Deseja encerrar o programa? S/N:\n> ")
            fechar = encerrar.upper()

        if fechar == "S":
            print("o programa será encerrado")
            sleep(2)
            break
        
        elif fechar == "N":
            mais_alunos = input("Adicionar mais alunos? S/N:\n> ")
            add_aluno = mais_alunos.upper()
            
            while add_aluno != "N" and add_aluno != "S":
                mais_alunos = input("Adicionar mais alunos? Digite S para sim ou N para nao S/N:\n> ")
                add_aluno = mais_alunos.upper()
                
            if add_aluno == "N":
                print("o programa será encerrado")
                sleep(2)
                break
            elif add_aluno == "S":
                print("Adicionando mais alunos")
                tem_proximo = "s"




