🎧 Podcast Episode Listening Time Prediction

This project focuses on predicting the average listening time of a podcast episode using machine learning techniques.
The goal is not only to build an accurate predictive model, but also to understand what truly drives listening behavior, communicate results through visualization, and make the model accessible via a simple application.

The project is structured into three main stages: modeling, visualization, and deployment.

📌 Project Objective

To develop a machine learning model capable of estimating how long a podcast episode will be listened to, based on intrinsic episode characteristics, popularity metrics, and contextual metadata.

Beyond prediction accuracy, this project emphasizes:

Model interpretability

Feature importance analysis

Clear communication of results

Practical usability through an interactive app

🧠 Dataset Overview

The dataset contains metadata for podcast episodes, including:

Podcast name

Episode title

Episode length (minutes)

Genre

Host popularity

Guest popularity

Publication day and time

Number of ads

Episode sentiment

Listening time (target variable)

🔬 Stage 1: Modeling & Data Science

This stage includes the full data science workflow:

🔍 Exploratory Data Analysis (EDA)

Distribution analysis of listening time

Identification of dominant features

Detection of low-impact variables

🧹 Data Cleaning & Feature Engineering

Handling missing values

Encoding categorical variables

Temporal feature transformation using sine and cosine encoding

Feature enrichment and normalization experiments

🤖 Model Training & Evaluation

Three models were trained and evaluated:

Linear Regression

Random Forest Regressor

XGBoost Regressor

After cross-validation and stability analysis, Random Forest was selected as the final model due to its:

Strong performance

Robustness

Interpretability

📈 Final Model Performance

Mean Absolute Error (MAE): ~9.18 minutes

R²: ~0.78

These results indicate that the model explains approximately 78% of the variance in listening time, with an average prediction error of about 9 minutes.

🔑 Key Insight

Feature importance analysis revealed that:

Episode length alone accounts for nearly 78% of the model’s predictive power

Popularity-related features (host and guest) have moderate influence

Temporal, genre, sentiment, and contextual variables have minimal impact

📊 Stage 2: Visualization (Power BI Dashboard)

A Power BI dashboard was built to communicate both model performance and business insights.

Dashboard Features

Listening Time by Genre:
Comparison between real and predicted values

Model Explanation Rate:
R² score presented in an intuitive card

Average Prediction Error:
MAE displayed in minutes

Feature Importance:
Bar chart highlighting the most influential variables

Genre Filter:
Dynamic filtering applied across all visuals

🔗 Power BI Report:
https://app.powerbi.com/groups/me/reports/f0767012-e6b8-43b1-844f-5070311e6b89/91bd459ac4101b372619?experience=power-bi

🚀 Stage 3: Deployment & Application

To make the model usable beyond analysis, a lightweight application was developed.

🖥️ Streamlit App

Simple and intuitive interface

Users input episode characteristics

The model predicts the expected listening time

Includes a Quick Prediction mode with minimal inputs

Advanced inputs are available for more detailed predictions

🔗 Live App:
https://podcast-listening-time.streamlit.app/

☁️ Model Serving

The trained model is deployed using AWS Lambda

The Streamlit app consumes the model via a serverless endpoint

This setup ensures scalability and low-latency predictions

🧩 Project Structure

The project is organized to clearly separate:

Data preparation and modeling

Visualization and reporting

Application and deployment logic

This modular approach improves maintainability and reproducibility.

🏁 Conclusion

This project demonstrates an end-to-end machine learning workflow:

From raw data to insights

From model training to interpretability

From analysis to real-world usability

A key takeaway is that simple, intrinsic episode characteristics dominate listening behavior, while many commonly assumed factors play a minor role.
The final solution balances accuracy, interpretability, and user experience.

📬 Contact

If you have questions, feedback, or would like to discuss the project, feel free to reach out.