total = 0
masculino = 0
feminino = 0

homem_aprovado = 0
mulher_aprovado = 0

homem_reprovado = 0
mulher_reprovado = 0

homem_exame = 0
mulher_exame =0

aprovados = 0
reprovados = 0
exame = 0

tem_proximo = "s"

  


while tem_proximo == "s" :
    alunos = input("Digite o nome do aluno: ")
    aluno = alunos.title()
    
    sexos = input("Escolha o Sexo do Aluno M/F: ")
    sexo = sexos.upper()
   
    while sexo != "M" and  sexo != "F":
        print("Escolha apenas M para masculino ou F para feminino")
        sexos = input("Escolha o Sexo do Aluno M/F: ")
        sexo = sexos.upper()

    if sexo == "M":
        masculino += 1
        total += 1
        
    elif sexo == "F":
        feminino += 1
        total += 1

        
    nota_primeiro = -1
    while type(nota_primeiro) !=float or nota_primeiro <0 or nota_primeiro >10:
        try:
            nota_primeiro = float(input("Digite a primeira nota (0/10 com decimais separados por ponto): "))
            
        except:
            print("Digite um numero de 0 a 10")
    
    nota_segundo = -1
    while type(nota_segundo) !=float or nota_primeiro <0 or nota_primeiro >10:
        try:
            nota_segundo = float(input("Digite a segunda nota (0/10 com decimais separados por ponto): "))
            
        except:
            print("Digite um numero de 0 a 10")
    
    nota_terceiro = -1
    while type(nota_terceiro) !=float or nota_primeiro <0 or nota_primeiro >10:
        try:
            nota_terceiro = float(input("Digite a terceira nota (0/10 com decimais separados por ponto): "))
            
        except:
            print("Digite um numero de 0 a 10")



    media = (nota_primeiro + nota_segundo + nota_terceiro) /3  
    print(nota_primeiro, nota_segundo, nota_terceiro)      
    print(media)

    if  media >=7:
        print("aluno aprovado")
        aprovados += 1
        if sexo == "M":
            homem_aprovado +=1
            
        elif sexo == "F":
            mulher_aprovado +=1
           

    elif media >=4 and media <7:
        print("o aluno ficou de exame")
        exame += 1
        if sexo == "M":
            homem_exame +=1
            
        elif sexo == "F":
            mulher_exame +=1

    else:
        print("infelizmente ele foi reprovado")
        reprovados += 1
        if sexo == "M":
            homem_reprovado +=1
            
        elif sexo == "F":
            mulher_reprovado +=1
            
    proximo_aluno = input("Ir para proximo aluno? S/N:" )
    proximo = proximo_aluno.upper()
    while proximo != "S" and  proximo != "N":
        print("Escolha apenas S para sim ou N para não")

        proximo_aluno = input("Ir para proximo aluno? S/N:" )
        proximo = proximo_aluno.upper()

    if proximo == "S":
        tem_proximo = "s"
        
        
    elif proximo == "N":
        tem_proximo = "n"
        print("aprovados:", aprovados)
        print("Percentual de alunos aprovados:",int(aprovados * 100 / total),"%")
        print("percentual de alunos de exame:",int(exame * 100 / total),"%")
        print("Percentual de alunos reprovados:",int(reprovados * 100 / total),"%")
        
        print("total de homens aprovados:", homem_aprovado)
        print("total de mulheres aprovadas:", mulher_aprovado)
       
        print("total de homens de exame:", homem_aprovado)
        print("total de mulheres de exame:", homem_aprovado)
       
        print("total de homens reprovados:", homem_reprovado)
        print("total de mulheres reprovados:", mulher_reprovado)

        





        
    

    