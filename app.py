import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Monitoramento - Estação de Petróleo", layout="wide", initial_sidebar_state="expanded")

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

# Gerando dados
dados = pd.DataFrame(gerar_dados_sensor())

# Sidebar para navegação
st.sidebar.title("🛢️ Navegação")
pagina = st.sidebar.radio("", [
    "Overview",
    "Monitoramento de Bombas",
    "Pressão e Temperatura",
    "Manutenção Preditiva",
    "Alarmes"
])

# Página Overview
if pagina == "Overview":
    st.title("🏭 Overview da Estação")
    
    # Status geral - KPIs principais
    st.markdown("""
    <style>
    .kpi-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
        text-align: center;
    }
    .equipment-box {
        background-color: #2E2E2E;
        padding: 15px;
        border-radius: 10px;
        margin: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="kpi-box">
            <h3>Status Geral</h3>
            <h2 style="color: #00FF00;">NORMAL</h2>
            <p>↑ Operacional</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="kpi-box">
            <h3>Produção Diária</h3>
            <h2>1500 bbl</h2>
            <p>↑ 2%</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="kpi-box">
            <h3>Pressão Média</h3>
            <h2>{dados['pressao'].mean():.1f} PSI</h2>
            <p>↔ Estável</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="kpi-box">
            <h3>Temperatura Média</h3>
            <h2>{dados['temperatura'].mean():.1f}°C</h2>
            <p>↑ Normal</p>
        </div>
        """, unsafe_allow_html=True)

    # Equipamentos com GIFs/imagens
    st.subheader("Monitoramento de Equipamentos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="equipment-box">
            <h4>Compressor Principal</h4>
        </div>
        """, unsafe_allow_html=True)
        # GIF de um compressor industrial
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDd5Y2k4Y2JyOWF1OWF4bWh6bHp6YnB0YmRxNHBnOWF1dmpxbG92cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KfYPg04GkiOre/giphy.gif", 
                 caption="Status: 🟢 Operacional")
        st.markdown("""
        - Pressão: 120 PSI
        - Temperatura: 75°C
        - Vibração: Normal
        """)

    with col2:
        st.markdown("""
        <div class="equipment-box">
            <h4>Bomba de Injeção</h4>
        </div>
        """, unsafe_allow_html=True)
        # GIF/imagem de uma bomba industrial
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmZ5ZWZ0Y2wzNXB6ZHZ0ZDdwbXN2NnB5aHBnM2t5Ym8yeHdqYjNwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7btQ8jDTPGDpgc6I/giphy.gif", 
                 caption="Status: 🟡 Atenção")
        st.markdown("""
        - Vazão: 500 m³/h
        - Pressão: 85 PSI
        - Vibração: Elevada
        """)

    with col3:
        st.markdown("""
        <div class="equipment-box">
            <h4>Separador Trifásico</h4>
        </div>
        """, unsafe_allow_html=True)
        # Imagem de um separador
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWhyY3RqMzF1NWd6ZWY2ZWR0M2wxbDY5Y2Zwd2J0cDdnNzBxdWp6ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7btQ8jDTPGDpgc6I/giphy.gif", 
                 caption="Status: 🟢 Operacional")
        st.markdown("""
        - Nível: 65%
        - Temperatura: 65°C
        - Pressão: 45 PSI
        """)

    # Gráfico de tendência em tempo real
    st.subheader("Tendência em Tempo Real")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Pressão', 'Temperatura', 'Vazão']
    )
    st.line_chart(chart_data)

    # Alertas e Notificações
    st.subheader("Alertas Recentes")
    alertas = [
        "⚠️ Vibração elevada na Bomba de Injeção - Há 5 min",
        "✅ Manutenção preventiva do Compressor concluída - Há 1h",
        "ℹ️ Troca de filtros programada para amanhã"
    ]
    for alerta in alertas:
        st.info(alerta)
