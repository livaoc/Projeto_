#Projeto final para o curso de iniciação em Python do Programa DiversificaDev



def adicionar_obra(lista_de_obras, obra):
          ## Adiciona uma nova obra (filme, series, livros, animes, desenhos) à uma lista
    lista_de_obras.append(obra)
    print("Obra adicionada com sucesso!")
    return lista_de_obras

lista_de_obras = []
lista_de_notas = []
continuar = True


def deletar_obra(lista_de_obras, lista_de_notas, index):
      ## Parte do programa referente a deletar uma obra da lista criada a partir do seu número do index
    try:
        lista_de_obras.pop(index - 1)        ## Foi utilizado também os comandos co index! Do mesmo jeito dá pra fazer o código sem os utilizar
        lista_de_notas.pop(index - 1)
    
    except IndexError:
        print("Inválido!! Digite um número que seja válido!")
    return lista_de_obras, lista_de_notas

def exibir_menu():
     ## Personaliza as opções ao iniciar o programa
    print("Escolha uma opção:\n" \
          "1 - Inserir nova obra\n" \
          "2 - Listar obras e notas\n"\
          "3 - Deletar obra da lista\n"\
          "4 - Encerrar o programa"
          )

def dar_nota():
      ## Parte do código referente a inserir uma nota ou não à obra
    while True:
        dar_nota = input ("Deseja dar uma nota para a obra?\n \t1 - Sim\n \t2 - Não\n")
        if dar_nota == "1":
            while True:
                try:        ## Primeiramente tentei usar o argumento "if not nota.isnumeric()", mas não era possivel incluir linhas floats
                            ## Aí fui procurar no google, onde me deparei com esse comando. Ele funciona para resolver exceções e erros. Achei super útil e quis implementar!
                            ## É usado também mais acima no código (def deletar_obras), e mais abaixo também dentro do loop principal para a execução do programa
                    nota = float(input ("Dê a nota desejada de 0 a 10: "))
                    if 0<=nota<=10:
                        print("Nota anotada!")
                        return nota
                    else:
                        print("Nota acima de 10 e menor que 0 não conta!!")

                except ValueError:
                    print("Digite um número!! Letras não valem como nota!")

        elif dar_nota == "2":
            print("Você quem manda!")
            return None

        else:
            print("Inválido. Escolha uma das opções citadas!")

def listar_obras(lista_de_obras, lista_de_notas):
       ## Existe as obras e suas devidas notas
    print("-" * 50)
    print("\t\t\tLista de obras e suas notas")
    print("-" * 50)
    for i in range(len(lista_de_obras)):
        obra = lista_de_obras[i]
        nota = lista_de_notas[i]
        nota_decisao = f"{nota:.1f}" if nota is not None else "-------"  ## Aqui foi um jeito que aprendi de fazer um if/else de forma mais curta e direta. 
                                                                     ## Está definindo se tem uma nota ou não pra obra!        
        print(f"{i+1} -> {obra} \t\t {nota_decisao}")
    print("-" * 50)


#Loop principal, com usos de If else, assim como try/except, para lidar com todas opções imaginaveis 
while continuar:
    exibir_menu()
    opcao = input ("insira o que deseja fazer: ")

    if opcao == "1":
        obra = input ('Insira uma nova obra: ')
        lista_de_obras = adicionar_obra(lista_de_obras, obra)
        nota = dar_nota()
        lista_de_notas.append(nota)
    
    elif opcao == "2":
        listar_obras(lista_de_obras, lista_de_notas)
    
    elif opcao == "3":
        try:
            obra = input('Insira o número da obra que deseja deletar: ')
            obra = int(obra)
            lista_de_obras, lista_de_notas = deletar_obra(lista_de_obras, lista_de_notas, obra)
        
        except ValueError:
            print("Digite uma das opções citadas!!")


    elif opcao == "4":
        continuar == False
        print("Lista finalizada por agora! Até mais!")
        break
    
    else:
        print("Opção invalida. Tente novamente.")
    print('\n')


    # Algo que eu gostaria de ter implementado no programa mas não pude por causa do meu tempo limitado nestes ultimos dias e hoje (segunda feira, data final pra entrega):
    # Deixar o usuario classificar se a obra que adicionou na lista é um livro, serie, filme, anime, desenho, manhwa, etc.
    # Assim, o usuario poderia acessar uma lista com todas suas obras, ou acessar cada obra de cada tipo (mostrar uma lista só com as obras que são livros, só as que são filmes, etc). Ele poderia escolher o que exibir e onde adicionar cada obra
    # Pra isso eu suponho que tem que fazer um código para o usuario inserir a obra escolhida *também* dentro de outras listas -> a obra ficaria dentro da lista geral (lista_de_obras), assim como dentro de outras listas mais específicas
