import streamlit as st
import pickle
import pandas as pd

final_model=pickle.load(open('final_model.pkl','rb'))

df1={'Comprehensive':0,'Third Party Insurance':1,'Zero Dep':2 ,'Not Available':3,'Third Party':1}
df2={'Petrol':0, 'Diesel':1,'CNG':2}
df4={'Manual':0, 'Automatic':1}
df3={'First Owner':1,'Second Owner':2,'Third Owner:':3,'Fourth Owner':4,'Fifth Owner':5}


# final_model=pickle.load(open('final_model.pkl','rb'))
st.title(" Used Car Price Predictor")
insurance_validity = st.selectbox(
    "Insurance Validity",
    ['Comprehensive', 'Third Party Insurance', 'Zero Dep', 'Not Available', 'Third Party']
)

fuel_type = st.selectbox(
    "Fuel Type",
    ['Petrol', 'Diesel', 'CNG']
)

kms_driven = st.text_input("KM Driven")

ownsership = st.selectbox(
    "Ownership",
    ['First Owner', 'Second Owner', 'Third Owner:', 'Fourth Owner', 'Fifth Owner']
)

transmission = st.selectbox(
    "Transmission Type",
    ['Manual', 'Automatic']
)

# Predict Button
if st.button("Predict"):
    insurance_validity = df1[insurance_validity]
    fuel_type = df2[fuel_type]
    kms_driven = int(kms_driven)
    ownsership = df3[ownsership]
    transmission = df4[transmission]

    test = [[insurance_validity, fuel_type, kms_driven, ownsership, transmission]]

    yp = final_model.predict(test)[0]

    st.write("Predicted Car Price is", round(yp, 2), "Lakhs")