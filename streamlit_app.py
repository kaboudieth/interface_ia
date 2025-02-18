import streamlit as st
import pandas as pd

exemple = "./exemple.csv"


def main() -> None:
    st.title("Interface IA")
    st.header("Uploader vos données")
    data = st.file_uploader("Uploader un dataset", type=["csv"])
    
    if data is not None:
        try:
            # Tentative de lecture du fichier CSV
            data_preview = pd.read_csv(data)
            st.success("Fichier CSV chargé avec succès!")
            st.write("Aperçu des données chargées (5 premières lignes):")
            st.dataframe(data_preview.head())
        except Exception as e:
            # S'il y a une erreur dans le formatage du fichier CSV, afficher une alerte
            st.error(f"Une erreur s'est produite lors du chargement du fichier. Vérifiez le format du fichier CSV. \nDetails de l'erreur: {e}")
    
    st.write("ou utiliser l'exemple ci-dessous")
    col1, col2 = st.columns([0.2, 0.8])
    with col1:
        st.download_button(label="Télécharger", data=exemple,
                           file_name="exemple.csv")
    with col2:
        exemple_check = st.checkbox("Utiliser l'exemple")
    if exemple_check:
        data = exemple
    if data:
        data = pd.read_csv(data)

    st.header("Paramétrer votre modèle")
    st.subheader("Choix du modèle")
    categorie = st.selectbox("Choisir le type de modele", [
                             "Regression", "Classification"])
    if categorie == "Regression":
        model = st.selectbox("Choisir le modèle", [
                             "Regression linéaire", "Regression polynomiale"])
    elif categorie == "Classification":
        model = st.selectbox("Choisir le modèle", [
                             "K mean", "KNN"])

    st.subheader("Choix des paramètres")
    if model == "Regression linéaire":
        param = st.slider("Choisir le paramètre", 0, 10)

    st.header("Visualiser les résultats")


if __name__ == "__main__":
    main()
