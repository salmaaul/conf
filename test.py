import streamlit as st

# Electron configuration for atoms
electron_config = {
    "Hidrogen": "1s1",
    "Helium": "1s2",
    "Lithium": "1s2 2s1",
    "Berilium": "1s2 2s2",
    "Boron": "1s2 2s2 2p1",
    "Karbon": "1s2 2s2 2p2",
    "Nitrogen": "1s2 2s2 2p3",
    "Oksigen": "1s2 2s2 2p4",
    "Fluorin": "1s2 2s2 2p5",
    "Neon":"1s2 2s2 2p6",
    "Natrium":"1s2 2s2 2p6 3s1",
    "Magnesium":"1s2 2s2 2p6 3s2",
}

st.title("Electron Configuration")
st.write("Select an atomic number:")

atomic_number = st.selectbox("Atomic Name", list(electron_config.keys()))

st.write("Electron Configuration:")
st.write(electron_config[atomic_number])