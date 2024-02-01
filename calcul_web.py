from calcul import Calcul
import streamlit as st

st.title("Bienvenue a Notre Calculatrice")

valeur1 = st.number_input(
    'Enter a number', min_value=0, max_value=100, key="m1")
valeur2 = st.number_input(
    'Enter a number', min_value=0, max_value=100, key="m2")

mon_calcul = Calcul(valeur1, valeur2)

if st.button('Addition'):
    st.write(f"addition:{mon_calcul.calcul_somme()}")
if st.button('Soustraction'):
    st.write(f"Soustraction:{mon_calcul.cacul_soustraction()}")
if st.button('Division'):
    st.write(f"Division:{mon_calcul.cacul_division()}")
if st.button('Multiplication'):
    st.write(f"Multiplication:{mon_calcul.cacul_multiplication()}")
