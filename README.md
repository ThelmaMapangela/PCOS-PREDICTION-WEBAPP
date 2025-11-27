
This project applies machine learning to estimate a patient’s likelihood of having Polycystic Ovary Syndrome (PCOS) using key clinical and hormonal features. It’s built to support healthcare professionals with quicker, data-driven diagnostic insights — and the best part? The model is fully deployed as a user-friendly web service for smooth, real-time interaction

PCOS is a hormonal condition that affects women of reproductive age and can contribute to infertility, weight changes, and several metabolic complications. Early identification is crucial for managing symptoms and reducing long-term risks. This project uses machine learning to estimate an individual’s likelihood of developing PCOS by analyzing a dataset containing key clinical and hormonal features.


[PCOS Prediction Dataset](https://www.kaggle.com/code/vengadeshwaran58/pcos-dataset-exploration-and-prediction) 📥


Files in `data/`:

- `cleaned_data.csv`: Data that's ready to go for training.
- `pcos_prediction_dataset.csv`: The raw dataset, ready for exploration.
- 
#### Findings
Numerical Summary

The mean age of participants was 31.98 years (range: 15–49).

The average lifestyle score was 5.51 on a 1–10 scale.

The mean predicted likelihood of undiagnosed PCOS was 0.15 (range: 0.05–0.25).

Diagnosis Distribution

89.5% of individuals were not clinically diagnosed with PCOS.

10.5% received a confirmed diagnosis.

BMI Classification

Normal BMI: 50.1%

Overweight: 30.0%

Obese: 14.9%

Underweight: 4.9%

Menstrual Regularity

Among participants reporting irregular menstrual cycles, 10.6% were diagnosed with PCOS.

Among those with regular cycles, the diagnosis rate was 10.4%.

Hirsutism

PCOS prevalence was higher in participants with hirsutism (15.0%) compared to those without (10.5%).

Correlation Analysis

Age, lifestyle score, and estimated undiagnosed PCOS probability exhibited only weak correlations with PCOS diagnosis, suggesting that symptom-based and categorical clinical features play a more substantial role in risk determination.

These notebooks present show how I prepared the data, analyzed feature importance, and chosen the perfect model.


- **URL to the deployed service**: [https://pcosdetection.streamlit.app/] 
- Steps to deploy to Streamlit Cloud
  - Login/Signup for streamlit cloud from here [https://share.streamlit.io/]


