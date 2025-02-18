import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Loja Virtual", layout="wide")

# Título e descrição
st.title("🏪 Mega Store")
st.markdown("### Encontre os melhores produtos aqui!")

# Função para criar um card de produto
def produto_card(nome, preco, descricao, imagem_url):
    col1, col2 = st.columns([1, 2])
    with col1:
        # Aqui você substituiria pelo URL real da imagem
        st.image(imagem_url, width=200)
    with col2:
        st.subheader(nome)
        st.write(f"💰 Preço: R$ {preco:.2f}")
        st.write(descricao)
        if st.button(f"Comprar {nome}", key=nome):
            st.success(f"Produto {nome} adicionado ao carrinho!")

# Dados dos produtos (em uma situação real, viria de um banco de dados)
produtos = [
    {
        "nome": "Smartphone Ultra X",
        "preco": 1999.99,
        "descricao": "Smartphone último modelo com câmera de 108MP e tela AMOLED",
        "imagem": "https://placehold.co/200x200?text=Smartphone"
    },
    {
        "nome": "Notebook Pro",
        "preco": 4599.99,
        "descricao": "Notebook com processador de última geração e SSD de 512GB",
        "imagem": "https://placehold.co/200x200?text=Notebook"
    },
    {
        "nome": "Fone Bluetooth",
        "preco": 299.99,
        "descricao": "Fone sem fio com cancelamento de ruído ativo",
        "imagem": "https://placehold.co/200x200?text=Fone"
    }
]

# Sidebar com filtros
st.sidebar.title("Filtros")
preco_max = st.sidebar.slider("Preço máximo", 0, 5000, 5000)

# Container principal
st.write("## Produtos Disponíveis")

# Mostrar produtos filtrados
for produto in produtos:
    if produto["preco"] <= preco_max:
        st.write("---")
        produto_card(
            produto["nome"],
            produto["preco"],
            produto["descricao"],
            produto["imagem"]
        )

# Rodapé
st.markdown("---")
st.markdown("### 📞 Contato")
st.write("Email: contato@megastore.com")
st.write("Telefone: (11) 99999-9999")