# MammoScan Pro :pill: :computer:

## Website Link: https://mammoscanpro.streamlit.app/

## Details : 
**Name** : Esita Budhia</br>

**Country of Residence** : India</br>

**College Name** : Amity University Kolkata

**Graduation Year**: 2024

**Experience Level** : Student</br>

## Theme : 
Creating a brighter future for Breast health by leveraging cutting-edge technology and compassionate care. Unleash the potential of AI to drive impactful solutions and foster a healthier tomorrow for all.

## Problem Statement:
The existing methods of diagnosing breast cancers through Ultrasound scans often involve time-consuming and error-prone manual analysis by medical professionals. Additionally, there is a need for a secure and privacy-centric approach to handling sensitive patient data during the diagnostic process. The key points of the problem statement are as follows:

* **Manual Ultrasound Analysis**: Current methods for diagnosing breast cancers using Ultrasound scans rely heavily on manual analysis by medical experts. This process can be time-consuming, leading to delays in diagnosis and treatment planning.
* **Accuracy and Efficiency**: There is a demand for a more accurate and efficient cancer identification process to enable early detection and timely intervention, which significantly impacts patient outcomes and survival rates.
* **Lack of Comprehensive Information**: Patients often receive limited information about their specific breast cancer type, its characteristics, potential risks, and treatment options. Providing comprehensive insights is essential for informed decision-making and patient empowerment.
* **Data Privacy Concerns**: With increasing concerns about data privacy and security in healthcare, there is a critical need to ensure that patient data, including Ultrasound scans, is handled securely and not stored for privacy reasons.

## Solution: 💡 
In light of these challenges, **MammoScan Pro** aims to create an intelligent and privacy-focused solution that revolutionizes breast cancer diagnosis using AI-driven analysis. By leveraging the power of **Azure Custom Vision**, the application seeks to empower patients with comprehensive cancer insights and personalized treatment recommendations, ultimately contributing to improved patient outcomes and enhanced breast health care.

* MammoScan Pro is an innovative medical software application designed to revolutionize breast cancer diagnosis through AI-driven Ultrasound analysis.
* Leveraging **Azure Custom Vision's** pre-trained machine learning model, the app accurately identifies Benign, Malignant cancers from uploaded Ultrasound scans.
* The platform ensures privacy by not storing any user data or Ultrasound scans, safeguarding sensitive medical information through **Streamlit**.
* With a user-friendly interface built using **Streamlit**, patients can easily upload Ultrasound scans and receive rapid and precise cancer identification results.
* Detailed insights about the detected cancer, including its characteristics, causes, effects, and potential treatments, are provided to enable informed decision-making.
* Personalized treatment recommendations based on the cancer type and stage empower patients to make the best healthcare choices.
* The app's focus on data privacy, accuracy, and efficiency contributes to early detection and timely intervention, improving patient outcomes and breast health care.

## Tech Stack:
The following tech stacks have been used to create the application and deploy it.  
* **Python** to build the application.
* **Streamlit** to create a responsive web application along with widgets. 
* **Streamlit Community Cloud** to deploy the web application for anyone across the globe to access it. 
* **Microsoft Azure AI Custom Vision** to get a computer vision model trained using our dataset and use it to predict the cancer type with the patient's Ultrasound scan. 
* **GitHub** to host the source code, use the version control (collaboration history), pull requests and GitHub collaboration features to build efficiently with the teammates. It helps a lot to understand the changes and go back and forth if required to complete the software. 

## Installation Guide: ⬇️
First, install the following:
* Python

Then, follow this step-by-step process to run this application:
* Get your Azure subscription: https://azure.microsoft.com/en-in/free
* Create an Azure Custom Vision resource and train the model
* Travel to the directory where you wish to store the project files using the cd command.
* Clone the repository in your local system.
```bash
git clone https://github.com/aditimahek16/MammoScan-Pro
```
* Go to your project directory where all the files are present.
```bash
cd MammoScan-Pro
```
* Install the required dependencies to run the project.
```bash
pip install -r requirements.txt
```
* Replace the endpoint and key with your Azure Custom Vision model resource endpoint and key in predictor.py. 
* Run the application
```bash
streamlit run About.py
```
* Enjoy the app!

## Website Link :globe_with_meridians: : https://mammoscanpro.streamlit.app/

## Social Impact / Novelty:
**MammoScan Pro** is a socially impactful and innovative solution that brings together AI technology, data privacy, and streamlined healthcare services to empower patients, advance medical practices, and improve breast health outcomes. Its emphasis on early detection, privacy, and informed decision-making holds the potential to positively impact the lives of countless individuals and contribute to the broader advancement of healthcare practices.
* **Enhanced breast Health Care Access:** MammoScan Pro brings cutting-edge AI technology to the field of breast cancer diagnosis, making it more accessible to a broader population. With rapid and accurate cancer identification, patients from diverse backgrounds can benefit from early detection and timely treatment, improving overall breast health care outcomes.
* **Empowering Informed Decision-Making:** By providing comprehensive cancer insights and personalized treatment recommendations, MammoScan Pro empowers patients to actively participate in their healthcare journey. Informed patients can collaborate more effectively with medical professionals, leading to better treatment adherence and improved patient satisfaction.
* **Privacy-Centric Approach:** MammoScan Pro sets a new standard for data privacy in medical applications. Its commitment to not storing any user data or Ultrasound scans ensures patient information remains secure, addressing concerns about data breaches and confidentiality in healthcare.
* **Time-Efficient Diagnosis:** The use of AI-driven Ultrasound analysis significantly reduces the time required for cancer identification compared to traditional manual methods. Expedited diagnosis allows medical professionals to make timely treatment decisions, potentially leading to improved patient outcomes and reduced healthcare costs.
* **Encouraging Early Detection:** Early detection of breast cancers is critical for successful treatment and increased survival rates. MammoScan Pro' accurate and efficient identification of cancer types facilitates early intervention, potentially saving lives and improving the long-term prognosis for patients.
* **Promoting Medical Advancement:** The integration of Azure Custom Vision's pre-trained machine learning model into MammoScan Pro represents a novel approach in the field of medical imaging and diagnosis. This innovation showcases the potential for AI technology to revolutionize healthcare practices and contribute to ongoing medical advancements.
* **Public Health Awareness:** By providing comprehensive insights into breast cancers and their implications, MammoScan Pro contributes to public health awareness. Increased understanding of breast health and the importance of early diagnosis may encourage more individuals to undergo regular screenings, promoting overall breast health and well-being.

## Future Scope:
MammoScan Pro has significant future potential to evolve and improve breast cancer diagnosis and treatment. Through continuous innovation, integration of advanced technologies, and global collaborations, MammoScan Pro can impact the lives of millions of individuals by fostering early detection, personalized care, and advancements in breast health research and treatment.
* **Expanding cancer Identification Capabilities:** In the future, MammoScan Pro can be enhanced to detect and identify a broader range of breast cancers beyond Benign, Malignant cancers. The integration of additional pre-trained machine learning models can extend its capabilities to include other rare or complex cancer types, further improving diagnostic accuracy.
* **Integration of Advanced Imaging Techniques:** MammoScan Pro can explore the incorporation of advanced imaging techniques, such as functional Ultrasound (Ultrasound) and diffusion tensor imaging (DTI), to provide more detailed insights into cancer characteristics and potential impact on breast function. This would enable a more comprehensive understanding of the cancer's effects on the patient's overall health.
* **Multi-Modal Analysis for Holistic Diagnosis:** By integrating multiple imaging modalities and clinical data, MammoScan Pro can adopt a multi-modal analysis approach for a more holistic and accurate diagnosis. The combination of Ultrasound scans with other patient data, such as genetic profiles and medical history, can lead to a deeper understanding of cancer behavior and personalized treatment recommendations.
* **Global Outreach and Collaboration:** MammoScan Pro can expand its reach to a global scale, collaborating with medical institutions and experts worldwide. This expansion would enable the platform to cater to a more diverse patient population, ensuring its benefits reach individuals from different geographic locations and socioeconomic backgrounds.
* **Predictive Analytics for Treatment Outcomes:** Leveraging historical treatment data, MammoScan Pro can incorporate predictive analytics to assess the likelihood of treatment success for specific cancer types and patient profiles. This feature would enable medical professionals and patients to make well-informed decisions regarding treatment plans and potential outcomes.
* **Integration with Electronic Health Records (EHRs):** To enhance patient care coordination, MammoScan Pro can integrate with existing electronic health record systems. This integration would enable seamless sharing of diagnostic reports and treatment recommendations with healthcare providers, facilitating a collaborative and patient-centric approach to care.
* **AI-Driven Research and Clinical Trials:** MammoScan Pro' vast dataset of anonymized Ultrasound scans and associated information can be leveraged for AI-driven research and clinical trials. The application's anonymized data repository could contribute to advancing breast cancer research, accelerating drug discovery, and facilitating the development of innovative treatment options.
* **AI-Driven Radiomics and Prognostics:** MammoScan Pro can explore radiomics, which involves extracting quantitative features from Ultrasound scans, to develop AI-driven prognostic models. These models could predict cancer growth rates, treatment responses, and patient outcomes, aiding in personalized treatment planning and long-term care.
* **Mobile Application and Remote Diagnosis:** Developing a mobile application for MammoScan Pro would enable users to access cancer analysis and treatment recommendations conveniently on their smartphones. This mobile version could also facilitate remote diagnosis, allowing healthcare providers to reach underserved areas and offer expert consultations without geographical constraints.

### Build with :heart: by Esita

