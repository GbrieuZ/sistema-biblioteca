import streamlit as st

# Configuracao da pagina (titulo da aba do navegador e icone)
st.set_page_config(page_title="Biblioteca Simples", page_icon="📚", layout="centered")

# ------------------------------------------------------------------
# ESTADO DA APLICACAO
# No Streamlit o script roda inteiro de novo a cada clique. Por isso
# guardamos os dados no st.session_state, que sobrevive entre as
# interacoes. Ele e o equivalente as suas variaveis globais
# livros = {} e historico = [] do programa de terminal.
# ------------------------------------------------------------------
if "livros" not in st.session_state:
    st.session_state.livros = {}
if "historico" not in st.session_state:
    st.session_state.historico = []

# Atalhos pra escrever menos daqui pra baixo
livros = st.session_state.livros
historico = st.session_state.historico

# Titulo principal
st.title("📚 Biblioteca Simples")
st.caption("Sistema de gerenciamento de livros — versão web")

# As abas substituem o menu de numeros do terminal
aba_add, aba_listar, aba_remover, aba_atualizar, aba_emprestimo, aba_historico = st.tabs(
    ["➕ Adicionar", "📋 Listar", "🗑️ Remover", "✏️ Atualizar", "🤝 Empréstimo", "📜 Histórico"]
)

# ------------------------------------------------------------------
# ABA 1 — ADICIONAR LIVRO  (era a opcao 1 do terminal)
# ------------------------------------------------------------------
with aba_add:
    st.subheader("Adicionar livro ao sistema")

    titulo = st.text_input("Título do livro")
    autor = st.text_input("Nome do autor")
    quantidade = st.number_input("Quantidade de exemplares", min_value=1, step=1, value=1)

    if st.button("Adicionar livro"):
        # As mesmas validacoes que voce tinha no terminal
        if not titulo or not autor:
            st.error("Preencha o título e o autor.")
        elif titulo.isdigit() or autor.isdigit():
            st.error("Título e autor não podem ser apenas números.")
        elif titulo in livros:
            st.warning(f"O livro '{titulo}' já está cadastrado.")
        else:
            livros[titulo] = {"autor": autor, "exemplares": int(quantidade)}
            st.success(f"Livro '{titulo}' adicionado com sucesso!")

# ------------------------------------------------------------------
# ABA 2 — LISTAR LIVROS  (opcao 2)
# ------------------------------------------------------------------
with aba_listar:
    st.subheader("Livros cadastrados")

    if not livros:
        st.info("Não há livros cadastrados no sistema.")
    else:
        # Monta uma tabela ja ordenada por titulo
        tabela = [
            {"Título": t, "Autor": d["autor"], "Exemplares": d["exemplares"]}
            for t, d in sorted(livros.items())
        ]
        st.dataframe(tabela, use_container_width=True, hide_index=True)

# ------------------------------------------------------------------
# ABA 3 — REMOVER LIVRO  (opcao 3)
# ------------------------------------------------------------------
with aba_remover:
    st.subheader("Remover livro")

    if not livros:
        st.info("Não há livros cadastrados no sistema.")
    else:
        # selectbox = lista suspensa; substitui o "digite o nome" do terminal
        escolha = st.selectbox("Escolha o livro para remover", sorted(livros.keys()))
        if st.button("Remover livro"):
            livros.pop(escolha)
            st.success(f"Livro '{escolha}' removido da lista!")
            st.rerun()  # recarrega a tela pra o item sumir da lista

# ------------------------------------------------------------------
# ABA 4 — ATUALIZAR LIVRO  (opcao 4)
# ------------------------------------------------------------------
with aba_atualizar:
    st.subheader("Atualizar livro")

    if not livros:
        st.info("Não há livros cadastrados no sistema.")
    else:
        escolha = st.selectbox(
            "Escolha o livro para atualizar", sorted(livros.keys()), key="att_escolha"
        )
        dados_atuais = livros[escolha]
        st.write(
            f"Autor atual: **{dados_atuais['autor']}**  |  "
            f"Exemplares atuais: **{dados_atuais['exemplares']}**"
        )

        novo_nome = st.text_input("Novo nome", value=escolha)
        nova_qtd = st.number_input(
            "Nova quantidade", min_value=0, step=1, value=dados_atuais["exemplares"]
        )

        if st.button("Salvar alterações"):
            if not novo_nome:
                st.error("O nome não pode ficar vazio.")
            elif novo_nome != escolha and novo_nome in livros:
                st.error("Já existe um livro com este nome.")
            else:
                # Mesma logica do terminal: tira o registro antigo,
                # altera a quantidade e regrava com o novo nome
                dados = livros.pop(escolha)
                dados["exemplares"] = int(nova_qtd)
                livros[novo_nome] = dados
                st.success(
                    f"'{escolha}' atualizado para '{novo_nome}' "
                    f"com {int(nova_qtd)} exemplares."
                )
                st.rerun()

# ------------------------------------------------------------------
# ABA 5 — EMPRESTIMO  (opcao 5)
# ------------------------------------------------------------------
with aba_emprestimo:
    st.subheader("Registrar empréstimo")

    if not livros:
        st.info("Não há livros cadastrados no sistema.")
    else:
        escolha = st.selectbox(
            "Livro para emprestar", sorted(livros.keys()), key="emp_escolha"
        )
        estoque = livros[escolha]["exemplares"]
        st.write(f"Exemplares disponíveis: **{estoque}**")

        if estoque == 0:
            st.warning("Este livro está sem exemplares no estoque.")
        else:
            # O max_value ja impede pedir mais do que existe no estoque
            qtd = st.number_input(
                "Quantidade a emprestar", min_value=1, max_value=estoque, step=1, value=1
            )
            if st.button("Confirmar empréstimo"):
                livros[escolha]["exemplares"] -= int(qtd)
                historico.append({"Título": escolha, "Exemplares": int(qtd)})
                st.success(
                    f"Empréstimo realizado! Restam "
                    f"{livros[escolha]['exemplares']} exemplares."
                )
                st.rerun()

# ------------------------------------------------------------------
# ABA 6 — HISTORICO  (opcao 6)
# ------------------------------------------------------------------
with aba_historico:
    st.subheader("Histórico de empréstimos")

    if not historico:
        st.info("Você ainda não realizou nenhum empréstimo.")
    else:
        st.dataframe(historico, use_container_width=True, hide_index=True)
