import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
final_model = pickle.load(open("final_model.pkl", "rb"))

# ---------------- ENCODING MAPS ----------------
df1 = {
    'Comprehensive': 0,
    'Third Party Insurance': 1,
    'Zero Dep': 2,
    'Not Available': 3,
    'Third Party': 1
}

df2 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
df4 = {'Manual': 0, 'Automatic': 1}

df3 = {
    'First Owner': 1,
    'Second Owner': 2,
    'Third Owner:': 3,
    'Fourth Owner': 4,
    'Fifth Owner': 5
}

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #111827);
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}
.subtitle {
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 25px;
}
.box {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
}
.stButton>button {
    width: 100%;
    background: #22c55e;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    border: none;
}
.stButton>button:hover {
    background: #16a34a;
}
.result {
    background: rgba(34,197,94,0.15);
    padding: 15px;
    border-radius: 12px;
    font-size: 26px;
    font-weight: bold;
    color: #22c55e;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🚗 Used Car Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get an AI-based estimated resale price instantly</div>', unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([2, 1])

with col1:
    insurance_validity = st.selectbox(
        "Insurance Validity",
        ['Comprehensive', 'Third Party Insurance', 'Zero Dep', 'Not Available', 'Third Party']
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        ['Petrol', 'Diesel', 'CNG']
    )

    kms_driven = st.slider(
        "KM Driven",
        min_value=0,
        max_value=300000,
        value=40000,
        step=1000
    )

    ownsership = st.selectbox(
        "Ownership",
        ['First Owner', 'Second Owner', 'Third Owner:', 'Fourth Owner', 'Fifth Owner']
    )

    transmission = st.radio(
        "Transmission Type",
        ['Manual', 'Automatic'],
        horizontal=True
    )

    if st.button("🔮 Predict Price"):
        try:
            insurance_val = df1[insurance_validity]
            fuel_val = df2[fuel_type]
            owner_val = df3[ownsership]
            transmission_val = df4[transmission]

            test = [[insurance_val, fuel_val, kms_driven, owner_val, transmission_val]]
            yp = final_model.predict(test)[0]

            st.markdown(
                f'<div class="result">💰 Estimated Price: ₹ {round(yp,2)} Lakhs</div>',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    st.markdown("""
    <div class="box">
        <h2>📌 Why Use This App?</h2>
        <ul>
            <li>Instant car price prediction</li>
            <li>Powered by Machine Learning</li>
            <li>Modern & attractive UI</li>
            <li>Easy to use</li>
            <li>Great for college demo/project</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)