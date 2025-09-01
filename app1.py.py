import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Painel Educacional - ENEM 2024",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E40AF;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subheader {
        font-size: 1.5rem;
        color: #374151;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    .info-box {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1E40AF;
        margin-bottom: 1.5rem;
    }
    .highlight {
        background-color: #FFFBEB;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho principal
st.markdown('<div class="main-header">🎓 Painel de Análise do ENEM 2024 - Espírito Santo</div>', unsafe_allow_html=True)

# Informações do projeto
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="info-box">
        <h3>📊 Sobre o Projeto</h3>
        <p>Esta aplicação apresenta um <span class="highlight">MVP (Produto Mínimo Viável)</span> desenvolvido como parte 
        da avaliação da disciplina de Cloud Computing para produtos de dados na Pós-graduação em Mineração de Dados.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: #EFF6FF; padding: 1.5rem; border-radius: 10px; text-align: center;">
        <h4>👨‍🏫 Professor</h4>
        <p><strong>Maxwell Monteiro</strong></p>
        <h4>👨‍🎓 Aluno</h4>
        <p><strong>Uéliton José de Oliveira</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Objetivo do projeto
st.markdown('<div class="subheader">🎯 Objetivo do Projeto</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #F0FDF4; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #10B981;">
    <p>O objetivo principal é criar um <strong>painel interativo</strong> para análise e visualização dos resultados 
    do ENEM 2024 no estado do Espírito Santo. A aplicação permitirá:</p>
    <ul>
        <li>📈 Análise comparativa das notas por área de conhecimento</li>
        <li>🏫 Visualização do desempenho por escola e município</li>
        <li>📊 Identificação de padrões e tendências educacionais</li>
        <li>🎯 Benchmarking com médias estaduais e nacionais</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Fonte dos dados
st.markdown('<div class="subheader">📁 Fonte dos Dados</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #FEF3C7; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #F59E0B;">
    <p>Os dados utilizados neste projeto são <strong>públicos e oficiais</strong>, obtidos através do:</p>
    <p>🏛️ <strong>Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)</strong></p>
    <p>📊 <strong>Microdados do ENEM 2024</strong> contendo:</p>
    <ul>
        <li>🔬 Ciências da Natureza</li>
        <li>🌍 Ciências Humanas</li>
        <li>📝 Linguagens e Códigos</li>
        <li>🧮 Matemática</li>
        <li>✍️ Redação</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Navegação
st.markdown('<div class="subheader">🚀 Como Navegar</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #EDE9FE; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #8B5CF6;">
    <p>Utilize o <strong>menu abaixo</strong> para explorar as diferentes seções da aplicação:</p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="background-color: white; padding: 1rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <strong>📊 Dashboard</strong><br>Visão geral dos resultados
        </div>
        <div style="background-color: white; padding: 1rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <strong>🏫 Por Escola</strong><br>Análise por instituição
        </div>
        <div style="background-color: white; padding: 1rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <strong>🏙️ Por Município</strong><br>Comparativo regional
        </div>
        <div style="background-color: white; padding: 1rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <strong>📈 Tendências</strong><br>Evolução histórica
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.9rem;">
    <p>Desenvolvido com Streamlit | Dados: INEP/MEC | 2024</p>
</div>
""", unsafe_allow_html=True)


