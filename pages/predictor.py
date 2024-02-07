import streamlit as st
import time
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import requests

# Replace with your endpoint and prediction key
ENDPOINT = "https://mammoscanpro.cognitiveservices.azure.com/"
PREDICTION_KEY = "ebde9caa48dd4a73b40ffb62864872d1"

# Create a prediction client
credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

st.set_page_config(page_title="MammoScan Pro")

bcauses = """
The exact causes of benign, breast lumps, while scary, often aren't cancerous. Common causes include hormonal shifts like periods, pregnancy, or menopause, as well as tissue changes, infections, or injury scars. Certain medications and even excess caffeine might play a role. Remember, men can also get breast lumps due to hormone imbalances. If you notice a lump, don't panic, but consult a doctor for a proper diagnosis and peace of mind.
"""
bsymptoms = """
Benign can have significant symptoms on breast function and overall health.Breast changes like lumps, pain, nipple discharge, size/shape variations, or skin abnormalities can indicate benign breast disease. Be it self-discovery or during clinical exams/mammograms, these signs warrant consulting a healthcare professional. Early detection allows for proper diagnosis and treatment options like cyst drainage, surgery, or medication, depending on the specific case and potential discomfort. """
btreat = """
The treatment of benign depends on several factors, most breast lumps are harmless and require no treatment. However, if you have a specific type that raises future cancer risk, your doctor might suggest removing it surgically or taking preventive medication. Painful or uncomfortable lumps, or those indicating infection, can be treated with procedures like cyst drainage, surgery, or antibiotics. Remember, early consultation with your doctor ensures proper diagnosis and the best course of action for your specific case.
"""

mcauses = """While the exact cause of breast cancer remains elusive, several key factors increase your risk. Genetics play a role, with family history and specific gene mutations raising concerns. Lifestyle choices like age, weight, alcohol intake, and physical activity also contribute. Finally, hormonal influences, such as early periods, late menopause, and hormone therapy use, can be additional risk factors. Understanding these elements empowers individuals to make informed decisions about their health and seek appropriate screening if needed.
"""
msymptoms = """Be alert for these potential signs of breast cancer: painless lumps, unusual nipple discharge, dimpling or redness on the skin, changes in breast size or shape, inverted or retracted nipples, and new or persistent pain. Early detection is crucial, so don't hesitate to consult a healthcare professional if you notice any of these symptoms. Remember, this information is not a substitute for professional medical advice.
"""
mtreat = """
When facing malignant breast cancer, treatment options depend on individual factors. Surgery, from lumpectomy to mastectomy, can remove tumors and potentially affected lymph nodes. Radiation therapy follows surgery to target remaining cancer cells. Chemotherapy uses powerful drugs to shrink tumors and kill cancer cells throughout the body. For hormone-responsive cancers, hormonal therapy blocks hormones that fuel their growth. Additionally, targeted therapy might be used to attack specific mutations found in the cancer cells.
"""
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
st.title("MammoScan Pro")
st.text(
    "Upload an image of a close up of a cancerous ultrasound scan and we will tell you what type it is."
)
# read images.zip as a binary file and put it into the button
with open("test.zip", "rb") as fp:
    btn = st.download_button(
        label="Download test images",
        data=fp,
        file_name="test.zip",
        mime="application/zip",
    )
image = st.file_uploader(
    "Upload Image", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=False
)

if image is not None:
    disp = False
    
    with image:
        st.image(image, caption="Your Ultrasound Scan", width=350)
        image_data = image.read()
        results = predictor.classify_image("26b113fb-9f57-4484-be50-33144495cd7e", "Iteration1", image_data)
    disp = True
    
    c = st.image("loader.gif")
    time.sleep(3)
    c.empty()
    # Process and display the results
    if results.predictions:
        st.subheader("Prediction Results:")
        name="unknown"
        predict=0
        for prediction in results.predictions:
            if prediction.probability > predict and prediction.probability > 0.5:
                predict = prediction.probability
                name = prediction.tag_name

    if name!="unknown":
        st.text(f"Detected {name} with high confidence")
        if name == "benign":
            st.write(
                """
                Breast lumps, cysts, or tumors (benign breast disease) are common, though not always linked to cancer. While most are harmless, they can raise future cancer risk. To ensure peace of mind and proper diagnosis, consulting a healthcare professional is crucial. Regularly getting familiar with your breasts through self-exams helps detect changes early, allowing for informed treatment options.                """
            )
            st.image("images/glioma.webp", caption="Benign", width=350)
            st.write("More Info")

            tab1, tab2, tab3 = st.tabs(
                ["Causes", "Symptoms", "Treatment"]
            )
            with tab1:
                st.write(bcauses)
                st.write(
                    "More Info can be found on the [Cleveland Clinic website](https://my.clevelandclinic.org/health/diseases/6270-benign-breast-disease)"
                )
            with tab2:
                st.write(bsymptoms)
                st.write(
                    "More Info can be found on the [Cleveland Clinic website](https://my.clevelandclinic.org/health/diseases/6270-benign-breast-disease)"
                )
            with tab3:
                st.write(btreat)
                st.write(
                    "More Info can be found on the [Cleveland Clinic website](https://my.clevelandclinic.org/health/diseases/6270-benign-breast-disease)"
                )
            doctor()

        elif (
            name == "malignant"
        ):
            st.write(
                """
                Malignant breast cancer, a serious threat, arises when cells in the breast tissue divide uncontrollably, forming tumors that can spread. While not every lump is cancerous, early detection is crucial. Knowing the causes, symptoms, and treatment options empowers individuals to take charge of their health.                """
            )
            st.image("images/Meningioma.jfif", caption="Malignant", width=350)
            st.write("Known Carried Diseases")
            btab1, btab2, btab3 = st.tabs(
                ["Causes", "Symptoms", "Treatment"]
            )
            with btab1:
                st.write(mcauses)
                st.write(
                    "More Info can be found on the [American Cancer Society Website](https://www.cancer.org/cancer/breast-cancer.html)"
                )
            with btab2:
                st.write(msymptoms)
                st.write(
                    "More Info can be found on the [American Cancer Society Website](https://www.cancer.org/cancer/breast-cancer.html)"
                )
            with btab3:
                st.write(mtreat)
                st.write(
                    "More Info can be found on the [American Cancer Society Website](https://www.cancer.org/cancer/breast-cancer.html)"
                )
            doctor()

    else:
        st.text("Feel safe! No breast cancer detected")
    