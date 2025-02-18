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

# Estilos CSS
st.markdown("""
<style>
    /* Estilo geral */
    .main {
        padding: 20px;
    }
    
    /* Título principal */
    .title {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 40px;
        color: #ffffff;
        text-align: center;
    }
    
    /* Cards de KPI */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 40px;
    }
    
    .kpi-box {
        background: linear-gradient(145deg, #1e1e1e, #2d2d2d);
        border-radius: 15px;
        padding: 25px;
        width: 23%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .kpi-title {
        font-size: 18px;
        color: #888;
        margin-bottom: 15px;
    }
    
    .kpi-value {
        font-size: 32px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 10px;
    }
    
    .kpi-status {
        font-size: 14px;
        color: #00ff00;
    }
    
    /* Equipamentos */
    .equipment-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        margin-top: 40px;
    }
    
    .equipment-box {
        background: linear-gradient(145deg, #1e1e1e, #2d2d2d);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .equipment-title {
        font-size: 20px;
        color: #ffffff;
        margin-bottom: 15px;
        text-align: center;
    }
    
    .equipment-status {
        margin-top: 15px;
        padding: 10px;
        background: rgba(0,0,0,0.2);
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Página Overview
if pagina == "Overview":
    st.markdown('<h1 class="title">🏭 Overview da Estação</h1>', unsafe_allow_html=True)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="kpi-box">
            <div class="kpi-title">Status Geral</div>
            <div class="kpi-value" style="color: #00FF00;">NORMAL</div>
            <div class="kpi-status">↑ Operacional</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="kpi-box">
            <div class="kpi-title">Produção Diária</div>
            <div class="kpi-value">1500 bbl</div>
            <div class="kpi-status">↑ 2%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Pressão Média</div>
            <div class="kpi-value">{dados['pressao'].mean():.1f} PSI</div>
            <div class="kpi-status">↔ Estável</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-title">Temperatura Média</div>
            <div class="kpi-value">{dados['temperatura'].mean():.1f}°C</div>
            <div class="kpi-status">↑ Normal</div>
        </div>
        """, unsafe_allow_html=True)

    # Equipamentos
    st.markdown('<h2 style="margin-top: 50px;">Monitoramento de Equipamentos</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="equipment-box">
            <div class="equipment-title">Compressor Principal</div>
            <img src="https://media.giphy.com/media/KfYPg04GkiOre/giphy.gif" style="width: 100%; border-radius: 8px;">
            <div class="equipment-status">
                • Pressão: 120 PSI<br>
                • Temperatura: 75°C<br>
                • Vibração: Normal<br>
                <span style="color: #00ff00;">● Operacional</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="equipment-box">
            <div class="equipment-title">Bomba de Injeção</div>
            <img src="https://media.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif" style="width: 100%; border-radius: 8px;">
            <div class="equipment-status">
                • Vazão: 500 m³/h<br>
                • Pressão: 85 PSI<br>
                • Vibração: Elevada<br>
                <span style="color: #ffff00;">● Atenção</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="equipment-box">
            <div class="equipment-title">Separador Trifásico</div>
            <img src="https://media.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif" style="width: 100%; border-radius: 8px;">
            <div class="equipment-status">
                • Nível: 65%<br>
                • Temperatura: 65°C<br>
                • Pressão: 45 PSI<br>
                <span style="color: #00ff00;">● Operacional</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Gráfico de tendência
    st.markdown('<h2 style="margin-top: 50px;">Tendência em Tempo Real</h2>', unsafe_allow_html=True)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Pressão', 'Temperatura', 'Vazão']
    )
    st.line_chart(chart_data)

    # Alertas e Notificações
    st.markdown('<h2 style="margin-top: 50px;">Alertas Recentes</h2>', unsafe_allow_html=True)
    alertas = [
        "⚠️ Vibração elevada na Bomba de Injeção - Há 5 min",
        "✅ Manutenção preventiva do Compressor concluída - Há 1h",
        "ℹ️ Troca de filtros programada para amanhã"
    ]
    for alerta in alertas:
        st.info(alerta)
        
