import guardaf1
import streamlit as st

st.title("Calculadora de média dos alunos🧮")
st.caption("É necessario no minimo 4 notas")
nome = st.text_input("Nome do aluno")
nota1 = st.number_input('Dgite a primeira nota:', min_value=0.0)
nota2 = st.number_input("Digite a segunda nota:", min_value=0.0)
nota3 = st.number_input("digite a terceira nota:", min_value=0.0)
nota4 = st.number_input("digite a quarta nota:", min_value=0.0)

botao = st.button("Enviar")

if botao:
    media = guardaf1.calcula_media(nota1,nota2,nota3,nota4)
    situacao = guardaf1.situacao_media(media)
    texto =f"O aluno:{nome}, está {situacao}, com a média:{media}"
    if situacao == "Aprovado":
        st.success(texto)
    elif situacao == "Recuperação":
        st.warning(texto)
    else:
        st.error(texto)
    
