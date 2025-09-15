def calcula_media (n1, n2,n3, n4):
    return(n1+n2+n3+n4)/4

def situacao_media(media):
    if media >= 7:
        return "aprovado"
    elif media  >= 5.0 :
        return"recuperação"
    else:
        return'reprovado'
    
def programa_terminal():
    nome = input ('Qual o nome do aluno')
    nota1 = float (input ("informe a nota 1"))
    nota2 = float (input("informe a nota 2"))
    nota3 = float (input("informe a nota 3"))
    nota4 = float (input ("infome a nota 4"))

    media = calcula_media(nota1,nota2,nota3,nota4)
    situacao = situacao_media(media)

    print(f"{nome}  esta {situacao} com media:{media}")

if __name__ == "__main__":
    programa_terminal()    