def menu_principal():
    print("\n-------------- MENU --------------")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Remover livro")
    print("4 - Atualizar quantidade de livros")
    print("5 - Registrar empréstimo")
    print("6 - Exibir histórico de empréstimos")
    print("0 - sair")
    print("----------------------------------")
    
livros ={}
historico = []

def main():
    while True:
        menu_principal()

        try:
            selecao = int(input("\nEscolha uma opção: "))
            if selecao < 0 or selecao > 6:
                input("Erro: Opção inválida! Tente novamente. (ENTER para continuar)")
            
            elif selecao == 0:
                print("Encerrando programa")
                break

            elif selecao == 1: # Entrada dos dados (nome/autor/quantidade)
                print('\n-----Adicionar livro ao sistema-----')
                
                try:            
                    titulo_livro = input("\nQual o título do livro: ")
                    nome_autor = input("Qual o nome do autor do livro: ")
                    qntd_exemplares = int(input("Qual a quantidade de exemplares: "))

                    if titulo_livro.isdigit() or nome_autor.isdigit():
                        input("Não insira números para o título e autor. Tente novamente. (ENTER para continuar)")
                        continue
                    
                    elif qntd_exemplares <= 0:
                        input("A quantidade de exemplares deve ser maior que zero. Tente novamente. (ENTER para continuar)")
                        continue

                    
                    elif not titulo_livro or not nome_autor or not qntd_exemplares:
                        input("Preencha todos os itens. Tente novamente.")
                        continue

                except ValueError:
                    input("Erro: A quantidade deve ser um número inteiro e não pode ficar vazia. Tente novamente. (ENTER para continuar)")
                    continue      

                print(f"\nLivro {titulo_livro} adicionado com sucesso!")
                input("\nPressione ENTER para voltar ao menu")
                
                livros[titulo_livro] = {
                    "autor": nome_autor,
                    "exemplares": qntd_exemplares
                }   
        
            elif selecao == 2: # Lista dos livros ordenadas 
                print("\n-----Lista de livros cadastrados-----")
                livros_ordenados = dict(sorted(livros.items()))

                if not livros:
                        print("Não há livros cadastrados no sistema.")
                        input("Pressione ENTER para voltar ao menu")

                for chave, valor in livros_ordenados.items():
                    print(f"Nome do livro: {chave} | Autor: {valor['autor']} | Quantidade: {valor['exemplares']}")
                input("Pressione ENTER para voltar ao menu")
        
            elif selecao == 3: # Remover os livros listados
                print("\n-----Remover livro do sistema-----")
                livros_ordenados = dict(sorted(livros.items()))
                if not livros:
                    print("Não há livros cadastrados no sistema.")
                    input("Pressione ENTER para voltar ao menu")

                else:
                    print("Títulos disponíveis")

                    for chave, valor in livros_ordenados.items():
                        print(f"Nome do livro: {chave} | Autor: {valor['autor']} | Quantidade: {valor['exemplares']}")

                    remover = input("\nEscolha um título para remover: ")
                    if remover not in livros_ordenados:  
                        input("Este livro não existe na lista! Tente novamente. (ENTER para continuar)")
                    
                    if remover in livros_ordenados:                     
                        livros_ordenados = livros.pop(remover)
                        print(f"Livro {remover} excluído da lista!")
                        input("Pressione ENTER para voltar ao menu")          
            
            elif selecao == 4: # Atualizar os livros listados
                print("\n-----Atualizar livro no sistema-----")
                livros_ordenados = dict(sorted(livros.items()))
                if not livros:
                    print("Não há livros cadastrados no sistema.")
                    input("Pressione ENTER para voltar ao menu")

                else:
                    print("Títulos disponíveis")

                    for chave, valor in livros_ordenados.items():
                        print(f"Nome do livro: {chave} | Autor: {valor['autor']} | Quantidade: {valor['exemplares']}")

                    att = input("\nEscolha um título para atualizar o NOME e a QUANTIDADE: ")
                    if att not in livros:
                        input("Erro, este livro não exite! (ENTER para continuar)")
                        continue

                    print(f"\nVocê selecionou o título: {att} que possui {livros[att]['exemplares']} quantidades")
                    att_nome = input("\nDigite o novo nome: ")
                    
                    if att_nome != att and att_nome in livros:
                        input("Erro: Já existe um livro com este nome. Tente novamente. (ENTER para continuar)")
                    else:
                        try:
                            att_qtd = int(input("Digite a nova quantidade: "))

                            dados = livros.pop(att) # apaga a chave do dict (nome do livro neste caso)
                            # e mantem os demais valores salvos dentro do dict
                            dados['exemplares'] = att_qtd # altera os "exemplares salvos" pelo novo valor (att_qtd)
                            livros[att_nome] = dados # aqui o novo nome é adicionado na chave e é atribuido em seu valor
                            # a variável dados, que nesse caso foi editada os 'exemplares' e manteve o 'autor' salvo s/alterar

                            print(f"\nLivro {att} atualizado para {att_nome} com {att_qtd} exemplares.")
                            
                        except ValueError:
                            input("Erro: A quantidade deve ser um número inteiro. Tente novamente. (ENTER para continuar)")
                            continue
                        input("Pressione ENTER para voltar ao menu")


            elif selecao == 5: # Empréstimo de livro
                print("\n-----Empréstimo de livro-----")
                
                livros_ordenados = dict(sorted(livros.items()))
                if not livros:
                    print("\nNão há livros cadastrados no sistema.")
                    input("\nPressione ENTER para voltar ao menu") 
                    continue

                else:
                    print("Títulos disponíveis")

                    for chave, valor in livros_ordenados.items():
                        print(f"Nome do livro: {chave} | Autor: {valor['autor']} | Quantidade: {valor['exemplares']}")
                    input("Pressione ENTER para continuar")
                
                emp_titulo = input("\nDigite o nome do livro que você quer pegar emprestado: ")
                emp_qtd = int(input("Digite a quantidade de exemplares que você quer: "))

                if emp_titulo in livros: # se houver o titulo digitado no dict livros
                    estoque = livros[emp_titulo]['exemplares'] # vou armazenar o valor do dict (exemplares),
                    # com o nome que eu selecionar dentro do dict, na variavel estoque
                    if estoque >= emp_qtd: # Verifica se a quantidade em estoque é suficiente para atender o pedido
                        livros[emp_titulo]['exemplares'] -= emp_qtd # caso sim, subtrair o valor digitado dos exemplares salvos
                        dados_historico = {
                            'Título': emp_titulo,
                            'Exemplares': emp_qtd
                            }
                        historico.append(dados_historico)
                        print(f"\nEmpréstimo do livro realizado com sucesso. Restam {livros[emp_titulo]['exemplares']} exemplares no estoque.")
                        input("Pressione ENTER para voltar ao menu.a")
                    else: 
                        input("Não há essa quantidade no estoque. Pressione ENTER e tente novamente!")
                        continue
                else:
                    print("\nErro: Livro não encontrado.")
                    input("Pressione ENTER para voltar ao menu.")

            else:
                selecao == 6 # Consulta no histórico de empréstimos
                print("\n-----Histórico de Empréstimos-----")
                if not historico:
                    print("\nVocê não realizou nenhum empréstimo.")
                    input("Pressione ENTER para voltar ao menu")  
                    continue
                else:
                    print(historico)

        except ValueError:
            input("Erro: Escolha uma opção válida! Tente novamente. (ENTER para continuar)")
            continue

if __name__ == "__main__":
    main()
