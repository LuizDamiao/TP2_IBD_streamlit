import streamlit as st
import pandas as pd

st.set_page_config(page_title="TP2 IBD")

with st.container():
    st.title("TRABALHO PRÁTICO 2 - IBD")
    st.write("ALUNOS: Philipe Dutra Cunha, Luiz Gustavo Ferreira Damião, Lucas Andre dos Santos, Jackson Fernando Abath de Oliveira")
    st.write("MATRICULAS: 2021031734, 2021031670, 2022093032, 2023550470")
    st.write("---")


with st.container():
    st.subheader("CONSULTA 1 SELEÇÃO E PROJEÇÃO:")
    st.write("TEMA: OS 20 MAIORES TERRENOS CADASTRADOS E REGULARIZADOS EM REGISTRO")
    tabela1 = pd.read_csv("consulta1.csv")
    st.bar_chart(tabela1, x="Denominacao", y="Area", color="#FF6347", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 2 SELEÇÃO E PROJEÇÃO:")
    st.write("TEMA: OS 10 PAISES DE NACIONALIDADE DE ESTRANGEIROS COM MAIS POSSES")
    tabela2 = pd.read_csv("consulta2.csv")
    st.bar_chart(tabela2,x="Nacionalidade", y="Qtd", color="#ffaa00", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 1 JUNÇÃO DE DUAS RELAÇÕES:")
    st.write("TEMA: AS 10 CIDADES COM A MAIOR AREA DE TERRENOS NÃO REGULARIZADOS EM REGISTRO")
    tabela3 = pd.read_csv("consulta3.csv")
    st.bar_chart(tabela3, x="Municipio", y="Area", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 2 JUNÇÃO DE DUAS RELAÇÕES:")
    st.write("TEMA: ORDEM DOS ESTADOS COM MAIOR AREA DE CADASTRO RURAL")
    tabela4 = pd.read_csv("consulta4.csv")
    st.bar_chart(tabela4, x="UF", y="Area", color="#DEB887", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 3 JUNÇÃO DE DUAS RELAÇÕES:")
    st.write("TEMA: OS 20 MENORES TERRENOS CADASTRADOS E SUA LOCALIZACAO")
    tabela5 = pd.read_csv("consulta5.csv")
    st.bar_chart(tabela5, x="Denominacao", y="Area", color="#D8BFD8", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 2 JUNÇÃO DE TRES OU MAIS RELAÇÕES:")
    st.write("TEMA: OS 10 MAIORES TERRENOS PUBLICOS")
    tabela6 = pd.read_csv("consulta7.csv")
    st.bar_chart(tabela6, x="Denominacao", y="Area", color="#FFE4B5", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 3 JUNÇÃO DE TRES OU MAIS RELAÇÕES:")
    st.write("TEMA: ESTADOS COM MAIOR AREA DE TERRENOS DE ESTRANGEIROS")
    tabela7 = pd.read_csv("consulta8.csv")
    st.bar_chart(tabela7, x="UF", y="Area", color="#B0E0E6", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 1 AGREGAÇÃO SOBRE JUNÇAO DE DUAS OU MAIS RELAÇÕES:")
    st.write("TEMA: ESTADOS QUE MAIS POSSUEM TERRENOS PUBLICOS")
    tabela7 = pd.read_csv("consulta9.csv")
    st.bar_chart(tabela7, x="UF", y="Qtd", color="#ffaa00", width=0, height=0, use_container_width=True)
    st.write("---")

    st.subheader("CONSULTA 2 AGREGAÇÃO SOBRE JUNÇAO DE DUAS OU MAIS RELAÇÕES:")
    st.write("TEMA: ESTADOS COM MAIS TERRENOS DE ESTRANGEIROS")
    tabela8 = pd.read_csv("consulta10.csv")
    st.bar_chart(tabela8, x="UF", y="Estrangeiros", color="#FFDAB9", width=0, height=0, use_container_width=True)
    st.write("---")
