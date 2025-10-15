import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Carregar dados
enem_es_2024 = pd.read_csv('https://raw.githubusercontent.com/Ueliton-Oliveira/streamlit_1_enem/main/ENEM_ES_2024_modificado.csv')

# Sidebar
st.sidebar.title("Navegação do Painel")
selecao = st.sidebar.radio("Selecione uma visualização", [
    "Presença por Área",
    "Distribuição por Língua Estrangeira",
    "Notas Médias por Área"
])

# Capa colorida dividida em duas colunas (esquerda conteúdo, direita quadro)
col1, col2 = st.columns([3,1])

with col1:
    st.markdown("""
    <div style="background: linear-gradient(90deg, #2274A5 0%, #18BC9C 100%);
                border-radius: 12px; padding: 24px; color: white;">
    <h1>Painel de Análise do ENEM 2024 - Espírito Santo</h1>
    <h2>Sobre o projeto</h2>
    <p>
    Esta aplicação apresenta um MVP desenvolvido como parte da avaliação da disciplina de Cloud Computing na Pós-Graduação em Mineração de Dados do Instituto Federal do Espírito Santos (IFES) Campus-Serra.
    <br><br>
    <b>Objetivo:</b> Criar um painel interativo para análise e visualização dos resultados do ENEM 2024 no estado do Espírito Santo <span style="color:yellow; text-decoration: undernline;">(sem divisão de dependência administrativa):
    <ul>
      <li>Visualizar presenças e ausências nas áreas de conhecimento</li>
      <li>Visualizar quantidade de alunos para cada Língua Estrangeira</li>
      <li>Visualizar os resultados nas áreas e redação</li>
      <li>Visualizar notas médias por área, município e código de escola</li>
    </ul>
    </p>
    <p>
    <span style="color:yellow; display:block; margin-top:12px; margin-bottom:12px;">
    Observação importante: O código da escola indica a escola onde o aluno concluiu o Ensino Médio. Os gráficos mostram a média dos resultados dos alunos que finalizaram o Ensino Médio em cada escola, identificada pelo respectivo código. A base de dados do INEP não fornece o nome da escola, motivo pelo qual apenas o código é apresentado.
    </span>
    </p>            
    <b>Fonte de Dados:</b><br>
    Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)<br>
    Microdados do ENEM 2024: CN, CH, LC, MT, Redação
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: #18BC9C; border-radius: 12px; padding: 20px;
                color: white; font-weight: bold; text-align: center;">
        Disciplina:<br>Cloud Computing<br><br>
        Professor:<br>Maxwell Monteiro<br><br>
        Aluno:<br>Uéliton José de Oliveira
    </div>
    """, unsafe_allow_html=True)

# Função para filtrar df baseado em filtros selecionados
def filtrar_df(df, municipio, codigo_escola):
    if municipio != 'Todos':
        df = df[df['NOME MUN. PROVA'] == municipio]
    if codigo_escola != 'Todos':
        df = df[df['CÓD. ESCOLA'].astype(str) == codigo_escola]
    return df    


if selecao == "Presença por Área":
    colunas_presenca = ['PRESENÇA EM CN', 'PRESENÇA EM CH', 'PRESENÇA EM LC', 'PRESENÇA EM MT']
    tabela_presenca_plot = enem_es_2024[colunas_presenca].apply(pd.Series.value_counts).fillna(0).astype(int).reset_index()
    tabela_presenca_plot = tabela_presenca_plot.rename(columns={'index': 'Status de Presença'})
    tabela_presenca_melted = tabela_presenca_plot.melt(id_vars='Status de Presença', var_name='Matéria', value_name='Quantidade de Alunos')
    mapeamento_status = {'Faltou': 'Faltou', 'Presente': 'Presente', 'Eliminado': 'Eliminado'}
    tabela_presenca_melted['Status de Presença'] = tabela_presenca_melted['Status de Presença'].map(mapeamento_status)
    total_por_materia = tabela_presenca_melted.groupby('Matéria')['Quantidade de Alunos'].transform('sum')
    tabela_presenca_melted['Percentual'] = (tabela_presenca_melted['Quantidade de Alunos'] / total_por_materia) * 100

    fig = px.bar(
        tabela_presenca_melted,
        x='Status de Presença',
        y='Quantidade de Alunos',
        color='Matéria',
        barmode='group',
        title='Contagem de Presença por Matéria',
        labels={'Status de Presença': 'Status de Presença', 'Quantidade de Alunos': 'Número de Estudantes'},
        hover_data={'Quantidade de Alunos': True, 'Matéria': True, 'Status de Presença': True, 'Percentual': ':.2f%'}
    )
    fig.update_layout(xaxis_title='Status de Presença', yaxis_title='Número de Estudantes')
    st.plotly_chart(fig, use_container_width=True)

elif selecao == "Distribuição por Língua Estrangeira":
    contagem_lingua = enem_es_2024['LÍNGUA ESTRANGEIRA'].value_counts().reset_index()
    contagem_lingua.columns = ['Língua Estrangeira', 'Quantidade de Alunos']
    fig = px.pie(
        contagem_lingua,
        values='Quantidade de Alunos',
        names='Língua Estrangeira',
        title='Distribuição de Alunos por Língua Estrangeira',
        hole=0.7
    )
    fig.update_traces(textinfo='percent+value', hoverinfo='label+value+percent')
    st.plotly_chart(fig, use_container_width=True)

elif selecao == "Notas Médias por Área":
    colunas_notas = ['NOTA EM CN', 'NOTA EM CH', 'NOTA EM LC', 'NOTA EM MT', 'NOTA FINAL REDAÇÃO']

    municipios = ['Todos'] + sorted(enem_es_2024['NOME MUN. PROVA'].dropna().unique().tolist())
    municipio = st.selectbox('Selecione o município:', municipios)

    # Lista de códigos de escola filtrada pelo município selecionado
    if municipio == 'Todos':
        codigos_escola = ['Todos'] + sorted(enem_es_2024['CÓD. ESCOLA'].dropna().astype(str).unique().tolist())
    else:
        codigos_municipio = enem_es_2024.loc[enem_es_2024['NOME MUN. PROVA'] == municipio, 'CÓD. ESCOLA'].dropna().astype(str).unique()
        codigos_escola = ['Todos'] + sorted(codigos_municipio.tolist())

    codigo_escola = st.selectbox('Selecione o código da escola:', codigos_escola)

    df_filtrado = filtrar_df(enem_es_2024, municipio, codigo_escola)
    notas_medias = df_filtrado[colunas_notas].mean().round(2).tolist() if not df_filtrado.empty else [0]*len(colunas_notas)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=colunas_notas, y=notas_medias, text=notas_medias, textposition='outside'))
    titulo = 'Notas Médias por Matéria'
    if municipio != 'Todos': titulo += f' - {municipio}'
    if codigo_escola != 'Todos': titulo += f' (Escola: {codigo_escola})'

    fig.update_layout(
        title=titulo,
        xaxis_title='Matéria',
        yaxis_title='Nota Média',
        yaxis=dict(range=[0, 1000]),
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )
    st.plotly_chart(fig, use_container_width=True)

    if municipio == 'Todos' and codigo_escola == 'Todos':
        colunas_para_agrupar = ['NOME MUN. PROVA'] + colunas_notas
        notas_medias_por_municipio = enem_es_2024[colunas_para_agrupar].groupby('NOME MUN. PROVA').mean().reset_index()
        notas_medias_melted = notas_medias_por_municipio.melt(id_vars='NOME MUN. PROVA', var_name='Área do Conhecimento', value_name='Nota Média')
        fig2 = px.bar(
            notas_medias_melted,
            x='NOME MUN. PROVA',
            y='Nota Média',
            color='Área do Conhecimento',
            title='Notas Médias por Área do Conhecimento e Município',
            labels={'NOME MUN. PROVA': 'Município', 'Nota Média': 'Nota Média'},
            hover_data={'Nota Média': ':.2f'}
        )
        fig2.update_layout(xaxis_title='Município', yaxis_title='Nota Média', xaxis={'categoryorder': 'total descending'})
        st.plotly_chart(fig2, use_container_width=True)

# Destaques automáticos para gestores
media_geral_CN = enem_es_2024['NOTA EM CN'].mean()
media_geral_CH = enem_es_2024['NOTA EM CH'].mean()
media_geral_LC = enem_es_2024['NOTA EM LC'].mean()
media_geral_MT = enem_es_2024['NOTA EM MT'].mean()
media_geral_redacao = enem_es_2024['NOTA FINAL REDAÇÃO'].mean()
st.markdown(f"<div style='color: #2274A5;'><b>Destaques:</b> Média CN: {media_geral_CN:.2f} | CH: {media_geral_CH:.2f} | LC: {media_geral_LC:.2f} | MT: {media_geral_MT:.2f} | Redação: {media_geral_redacao:.2f}</div>", unsafe_allow_html=True)





