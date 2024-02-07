import streamlit as st

from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="MammoScan Pro", page_icon="💊", layout="wide")
st.markdown(
    """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;                
            }
            [data-testid="stSidebarNav"]::before {
                content: "MammoScan Pro";
                margin-left: 20px;
                margin-top: 20px;

                font-size: 30px;
                text-align: center;
                position: relative;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

st.title("Welcome to MammoScan Pro")

st.write(
    "This project is made with the goal to help people identify types of Breast Cancer by Slowing or stopping the growth of cancer and by preventing a return of cancer."
)

aps = st.button("Find Out!")
if aps:
    switch_page("predictor")

st.write("""This project was initiated because of the significant importance of breast cancer as a pressing issue. Breast cancer, including benign, and malignant,  affects countless individuals and their families around the world. It is a devastating disease that can have profound effects on physical, emotional, and cognitive well-being. Understanding the causes, effects, and available treatments for these breast cancer is crucial for raising awareness, promoting early detection, and improving patient outcomes.

By exploring the causes of these cancer, we can work towards identifying risk factors and developing preventive strategies. Understanding the effects of breast cancer helps us recognize the impact it has on individuals' lives, guiding efforts to provide appropriate support and care for patients. Additionally, knowledge of the available treatments helps healthcare professionals and patients make informed decisions about managing and combating these cancers effectively.""")

st.header("Types of Breast Cancer")
st.dataframe(
    data={
        "Cancer Types": [
            "Benign",
            "Malignant",
        ],
    },
    width=1000,
)
st.subheader("Benign")
st.write(
    """
Benign (non-cancerous) breast conditions are very common, and most women have them. In fact, most breast changes are benign. Unlike breast cancers, benign breast conditions are not life-threatening. But some are linked with a higher risk of getting breast cancer later on.

Some benign breast changes may cause signs or symptoms (such as breast lumps, pain, or nipple discharge), while others might be found during a mammogram. Most types of benign breast disease don't require treatment. However, your healthcare provider may recommend treatment if you have atypical hyperplasia or a different kind of benign breast disease that increases your future risk of breast cancer. 
 """
)
st.image("images/Benign.png", caption="Benign", width=350)

st.subheader("Malignant")
st.write(
    """
Malignant breast cancer is a cancerous tumor that grows in or around breast tissue. It can be aggressive because it can damage and invade surrounding tissue.

Malignant tumors are usually poorly defined and irregular with lobules. A doctor will perform a biopsy to determine the severity or aggressiveness of a suspected malignant tumor. 

About 80% of breast cancer cases are invasive. Malignant tumors can spread cancer cells throughout the body through the lymphatic system or blood, a process known as metastasis. 

"""
)
st.image("images/Malignant.png", caption="Malignant", width=350)

st.header("Progression of Breast Cancer")
st.image("images/progression.png", caption="Progession of Breast Cancer", width=350)


st.header("Model")
st.write(
    "We used a dataset from Kaggle to train our model. The dataset is [linked here](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset?resource=download).
)
st.write("The relevent graphs and info are shown below.")
st.subheader("Run One")
st.caption("Performance")
st.image("images/results.png")
