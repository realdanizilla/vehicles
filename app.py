# importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# carregando a base de dados e criando um dataframe
car_data = pd.read_csv(
    'C:\\Users\\daniz\\OneDrive\\Documentos\\Cursos\\TripleTen Data Science\\Sprint 5 Programação\\Projeto\\vehicles\\vehicles.csv')  # lendo os dados
df_car_data = car_data

# Criar o header
st.header("Web App - Veículos dos EUA", divider="blue")

# Criando containers para os gráficos
hist_container = st.container()
scatter_container = st.container()
df_container = st.container()

# criar um botão para o histograma
hist_button = st.button('Criar histograma')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(
        car_data,
        x="price",
        range_x=[0, 60000],
        title="Histograma de preço dos veículos",
        labels={"price": "Preço", "count": "Quantidade"}
    )

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar um botão para o gráfico de dispersão
scatter_button = st.button("Criar Gráfico de Dispersão")

if scatter_button:
    # escrever uma mensagem
    st.write("Criando um gráfico de dispersão do preço dos carros e sua quilometragem")

    # criar a scatterplot
    fig2 = px.scatter(
        car_data,
        x="price",
        y="odometer",
        range_x=[0, 100000],
        range_y=[0, 500000],
        trendline="ols",
        trendline_color_override="red",
        title="Gráfico de Dispersão Preço x Quilometragem dos veículos",
        labels={"odometer": "Quilometragem", "price": "Preço"}
    )

    # exibir a scatter interativa
    st.plotly_chart(fig2, use_container_width=True)

# Criar caixa de seleção do histograma
check_box_hist = st.checkbox("Criar Histograma")

# Criar caixa de seleção do gráfico de dispersão
check_box_scatter = st.checkbox("Criar Gráfico de Dispersão")

# Criar caixa de seleção da tabela
check_box_df = st.checkbox("Criar Tabela de Dados")


def create_histogram(container):
    """Cria o histograma"""

    if check_box_hist:
        # escrever uma mensagem
        st.write("Criando histograma de preços dos veículos")

        # criar um histograma
        fig3 = px.histogram(
            car_data,
            x="price",
            range_x=[0, 60000],
            title="Histograma de preço dos veículos",
            labels={"price": "Preço", "count": "Quantidade"}
        )

        # exibir um gráfico Plotly interativo
        container.plotly_chart(fig3, use_container_width=True)


def create_df(container):
    """Cria a tabela de dados"""

    if check_box_df:
        # escrever uma msg
        st.write("Criando tabela de dados")

        # criar a tabela
        container.dataframe(df_car_data)


def create_scatter(container):
    """Cria o grafico de dispersão"""

    if check_box_scatter:
        # escrever uma mensagem
        st.write(
            "Criando um gráfico de dispersão do preço dos carros e sua quilometragem")

        # criar a scatterplot
        fig4 = px.scatter(
            car_data,
            x="price",
            y="odometer",
            range_x=[0, 100000],
            range_y=[0, 500000],
            trendline="ols",
            trendline_color_override="red",
            title="Gráfico de Dispersão Preço x Quilometragem dos veículos",
            labels={"odometer": "Quilometragem", "price": "Preço"}
        )

        # exibir a scatter interativa
        container.plotly_chart(fig4, use_container_width=True)


def create_graphs():
    """Chama as funções para criação de gráficos"""

    create_histogram(hist_container)
    create_scatter(scatter_container)
    create_df(df_container)


# Criar botão para criar graficos a partir das checkboxes
st.button(
    "Criar gráficos selecionados",
    on_click=create_graphs,
    use_container_width=False
)
