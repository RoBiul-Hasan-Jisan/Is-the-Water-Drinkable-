# 💧 Water Quality Potability Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-Web%20App-red?style=for-the-badge&logo=flask)
![Hugging Face](https://img.shields.io/badge/Deployed%20on-Hugging%20Face-yellow?style=for-the-badge&logo=huggingface)

A Machine Learning-powered web application that predicts whether water is **safe (potable)** or **unsafe** for human consumption based on chemical properties.

---

##  Live Demo
Click the link below to test the application live:

###  **[Launch Water Quality App (Hugging Face)](https://huggingface.co/spaces/robiulhasanjisan88/water-quality-predictor)**

*(Alternative Dev Link: [Gradio Live Preview](https://40b50e2405bc475ac2.gradio.live/))*

---

##  About the Project
Access to safe drinking water is essential for health. This project uses machine learning to analyze nine different water quality metrics and classify water samples into two categories:
1.  **Potable:**  Safe to drink.
2.  **Not Potable:** Contaminated or unsafe for consumption.

The model was trained on the **Water Potability Dataset** (3000+ samples) using historic data on water quality parameters.

---

##  Features
* **Real-time Prediction:** Instant analysis of water safety.
* **Dual Mode Testing:** * **Safe Data Loader:** Automatically fills the form with confirmed safe values (pH ~11.5, High Chloramines).
    * **Unsafe Data Loader:** Automatically fills the form with confirmed contaminated values (pH 9.9, Low Chloramines).
* **User-Friendly Interface:** Clean, responsive UI with visual status indicators (Green for Safe, Red for Unsafe).

---

##  Input Parameters
The model requires the following chemical inputs:

| Parameter | Description |
| :--- | :--- |
| **pH Level** | Acid-base balance of the water (0-14). |
| **Hardness** | Capacity of water to precipitate soap (mg/L). |
| **Solids (TDS)** | Total dissolved solids (ppm). |
| **Chloramines** | Amount of Chloramines (major disinfectant) (ppm). |
| **Sulfate** | Amount of Sulfates dissolved (mg/L). |
| **Conductivity** | Electrical conductivity of the water (μS/cm). |
| **Organic Carbon** | Amount of organic carbon in ppm. |
| **Trihalomethanes** | Amount of Trihalomethanes in μg/L. |
| **Turbidity** | Measure of light emitting property (cloudiness). |

---

##  Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Storage:** Joblib
* **Web Framework:** Flask
* **Deployment:** Hugging Face Spaces (Docker/Linux environment)

---

##  How to Run Locally
If you want to run this on your own computer:

1.  **Clone the repository:**
    ```bash
    git clone [https://huggingface.co/spaces/robiulhasanjisan88/water-quality-predictor](https://huggingface.co/spaces/robiulhasanjisan88/water-quality-predictor)
    cd water-quality-predictor
    ```

2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    python app.py
    ```

4.  **Open in Browser:**
    Go to `http://127.0.0.1:5000`

---

###  Author
**Robiul Hasan Jisan** *Water Quality Prediction Project*
