import streamlit as st
import statistics
from datetime import datetime

st.set_page_config(
    page_title="Lucky Jet Analyzer",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Lucky Jet Analyzer")
st.write("Analyse statistique des résultats")

texte = st.text_area(
    "Entre les derniers coefficients séparés par des espaces",
    placeholder="1.12 1.45 2.03 1.08 3.21 1.76 5.42"
)

if st.button("🔎 ANALYSER"):

    try:
        coefficients = [
            float(x.replace(",", "."))
            for x in texte.split()
            if float(x.replace(",", ".")) > 0
        ]

        if len(coefficients) < 5:
            st.warning("Entre au moins 5 coefficients.")

        else:
            moyenne = statistics.mean(coefficients)
            mediane = statistics.median(coefficients)

            petits = sum(x < 2 for x in coefficients)
            moyens = sum(2 <= x < 5 for x in coefficients)
            hauts = sum(x >= 5 for x in coefficients)

            total = len(coefficients)

            st.subheader("📊 Analyse")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Moyenne", f"{moyenne:.2f}x")
                st.metric("Médiane", f"{mediane:.2f}x")

            with col2:
                st.metric("< 2x", f"{petits}/{total}")
                st.metric("≥ 5x", f"{hauts}/{total}")

            st.subheader("📈 Répartition")

            st.write(f"🔵 Moins de 2x : {petits}")
            st.write(f"🟡 Entre 2x et 5x : {moyens}")
            st.write(f"🔴 5x ou plus : {hauts}")

            st.subheader("🎯 Analyse expérimentale")

            if petits / total > 0.65:
                message = "Beaucoup de coefficients inférieurs à 2x dans l'historique."
            elif hauts / total > 0.20:
                message = "Plusieurs coefficients élevés ont été observés."
            else:
                message = "Aucune tendance statistique claire."

            st.info(message)

            st.caption(
                "⚠️ Cette analyse statistique ne permet pas de garantir "
                "le prochain coefficient ni son heure."
            )

    except ValueError:
        st.error(
            "Format incorrect. Exemple : "
            "1.20 2.35 1.05 4.20"
        )
