import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Monitoramento - Estação de Petróleo", layout="wide", initial_sidebar_state="expanded")

# Sidebar para navegação
st.sidebar.title("🛢️ Navegação")
pagina = st.sidebar.radio("", [
    "Overview",
    "Monitoramento de Bombas",
    "Pressão e Temperatura",
    "Manutenção Preditiva",
    "Alarmes"
])

# Dados simulados
def gerar_dados_sensor():
    now = datetime.now()
    dates = [now - timedelta(hours=x) for x in range(24)]
    return {
        'timestamp': dates,
        'pressao': np.random.normal(100, 10, 24),
        'temperatura': np.random.normal(80, 5, 24),
        'vazao': np.random.normal(500, 50, 24),
        'vibracao': np.random.normal(2.5, 0.5, 24)
    }

dados = pd.DataFrame(gerar_dados_sensor())

# Página Overview
if pagina == "Overview":
    st.title("🏭 Overview da Estação")
    
    # Status geral
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Status Geral", "Normal", "↑ Operacional")
    with col2:
        st.metric("Produção Diária", "1500 bbl", "↑ 2%")
    with col3:
        st.metric("Pressão Média", f"{dados['pressao'].mean():.1f} PSI")
    with col4:
        st.metric("Temperatura Média", f"{dados['temperatura'].mean():.1f}°C")

    # Layout de equipamentos
    st.subheader("Layout da Estação")
    col1, col2 = st.columns([2,1])
    with col1:
        # Aqui você pode adicionar uma imagem do layout da estação
        st.image("https://via.placeholder.com/800x400?text=Layout+da+Estacao")
    with col2:
        st.write("### Status dos Equipamentos")
        st.write("🟢 Bomba Principal: Operacional")
        st.write("🟢 Separador: Operacional")
        st.write("🟡 Compressor: Atenção")
        st.write("🟢 Válvulas: Operacional")

# Página Monitoramento de Bombas
elif pagina == "Monitoramento de Bombas":
    st.title("⚙️ Monitoramento de Bombas")
    
    # Seletor de equipamento
    equipamento = st.selectbox("Selecione o equipamento", 
                             ["Bomba Principal", "Bomba Secundária", "Bomba de Injeção"])
    
    col1, col2 = st.columns(2)
    with col1:
        # Gráfico de vibração
        fig_vib = px.line(dados, x='timestamp', y='vibracao',
                         title="Nível de Vibração")
        st.plotly_chart(fig_vib, use_container_width=True)
    
    with col2:
        # Gráfico de vazão
        fig_vazao = px.line(dados, x='timestamp', y='vazao',
                           title="Vazão")
        st.plotly_chart(fig_vazao, use_container_width=True)

# Página Pressão e Temperatura
elif pagina == "Pressão e Temperatura":
    st.title("🌡️ Pressão e Temperatura")
    
    # Gráficos de pressão e temperatura
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados['timestamp'], y=dados['pressao'],
                            name="Pressão (PSI)"))
    fig.add_trace(go.Scatter(x=dados['timestamp'], y=dados['temperatura'],
                            name="Temperatura (°C)", yaxis="y2"))
    
    fig.update_layout(
        title="Monitoramento de Pressão e Temperatura",
        yaxis=dict(title="Pressão (PSI)"),
        yaxis2=dict(title="Temperatura (°C)", overlaying="y", side="right")
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Página Manutenção Preditiva
elif pagina == "Manutenção Preditiva":
    st.title("🔧 Manutenção Preditiva")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Próximas Manutenções")
        st.write("🔸 Bomba Principal: 15 dias")
        st.write("🔸 Separador: 30 dias")
        st.write("🔸 Compressor: 2 dias")
        
    with col2:
        st.subheader("Histórico de Falhas")
        # Gráfico de pizza para tipos de falhas
        dados_falhas = pd.DataFrame({
            'Tipo': ['Mecânica', 'Elétrica', 'Instrumentação', 'Outros'],
            'Quantidade': [15, 8, 12, 5]
        })
        fig = px.pie(dados_falhas, values='Quantidade', names='Tipo',
                    title="Distribuição de Falhas")
        st.plotly_chart(fig, use_container_width=True)

# Página Alarmes
elif pagina == "Alarmes":
    st.title("⚠️ Alarmes")
    
    # Tabela de alarmes
    alarmes = pd.DataFrame({
        'Timestamp': pd.date_range(start='2024-02-18', periods=5, freq='H'),
        'Equipamento': ['Compressor', 'Bomba Principal', 'Separador', 'Válvula', 'Bomba Secundária'],
        'Tipo': ['Alta Temperatura', 'Vibração', 'Nível Alto', 'Posição', 'Pressão'],
        'Severidade': ['Alta', 'Média', 'Baixa', 'Baixa', 'Média'],
        'Status': ['Ativo', 'Resolvido', 'Ativo', 'Em análise', 'Resolvido']
    })
    
    st.dataframe(alarmes, use_container_width=True)
