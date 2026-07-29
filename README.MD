# Sistema de Gerenciamento de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python. Além do cadastro e controle de livros, permite registrar empréstimos e consultar o histórico, simulando o funcionamento básico de uma biblioteca real por meio de um menu interativo no terminal.

O projeto conta com duas versões: a original, em terminal, e uma versão web com interface visual, feita com Streamlit.

## 🔗 Demo ao vivo

Teste a versão web direto no navegador, sem instalar nada:

**➡️ [Acessar demonstração](https://sistema-biblioteca-esjmzyvu3cjkbek6ing7lw.streamlit.app/)**

> Como o app está no plano gratuito do Streamlit, ele pode hibernar após um tempo sem uso. Se aparecer uma tela pedindo pra reativar, basta clicar no botão e aguardar alguns segundos.

## Funcionalidades

- Adicionar novos livros ao acervo
- Listar todos os livros cadastrados
- Remover livros
- Atualizar a quantidade de exemplares
- Registrar empréstimos de livros
- Exibir o histórico de empréstimos
- Menu interativo e navegável pelo terminal

## Tecnologias utilizadas

- Python
- Streamlit (versão web)

## Como executar

1. Clone o repositório:

\`\`\`
git clone https://github.com/GbrieuZ/sistema-biblioteca.git
\`\`\`

2. Acesse a pasta do projeto:

\`\`\`
cd sistema-biblioteca
\`\`\`

3. Execute a versão que quiser:

**Versão terminal:**

\`\`\`
python terminal/biblioteca.py
\`\`\`

**Versão web (Streamlit):**

\`\`\`
pip install streamlit
streamlit run web/app.py
\`\`\`

## O que este projeto demonstra

- Implementação de um CRUD completo em Python
- Controle de estado (acervo, empréstimos e histórico)
- Lógica de negócio aplicada a um problema real
- Organização de código em funções e construção de menus interativos

---

Projeto desenvolvido como parte dos meus estudos em desenvolvimento de software durante minha transição de carreira para a área de TI.
