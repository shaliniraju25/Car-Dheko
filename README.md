![WhatsApp Image 2024-11-05 at 2 54 23 PM (1)](https://github.com/user-attachments/assets/c8e2fd46-7db6-48d3-8b6d-780798c556d6)

# Car Dekho - Used Car Price Prediction 🚗

# Project Overview 📚
This project focuses on developing an interactive, predictive tool for determining the price of used cars based on various factors. Leveraging machine learning and the data from Car Dekho, we aim to create a robust model for accurate price prediction, deployed as a Streamlit application. This tool is designed to streamline the car pricing process for both customers and sales representatives, enhancing the car-buying and selling experience.


# Skills and Techniques 🚀

1.Data Cleaning and Preprocessing
2.Exploratory Data Analysis (EDA)
3.Machine Learning Model Development
4.Price Prediction Techniques
5.Model Evaluation and Optimization
6.Model Deployment with Streamlit
7.Documentation and Reporting


# Problem Statement 📝
**Objective**: 
Build an intuitive and accurate predictive tool that estimates the prices of used cars based on various features (e.g., make, model, year, fuel type, transmission type, and city). This tool is deployed as an interactive web application on Streamlit, enabling both customers and sales representatives to seamlessly predict car prices in real time.

**Project Scope**: 
Car Dheko’s historical dataset provides essential car features from different cities. The task is to process this data, build a machine learning model for price prediction, and deploy the model as a Streamlit web app.


# Business Use Cases 💼

**Enhanced Customer Experience**: Offers customers easy access to realistic price estimates.

**Sales Optimization:** Helps sales representatives set competitive prices based on accurate data.

**Operational Efficiency:** Enables streamlined pricing processes, minimizing manual assessments.

**Informed Decision-Making:** Provides insights for strategic planning based on predictive analysis.



# Approach 🔍

# 1.Data Processing:

**Concatenation:** Import and merge datasets from various cities into a unified format.
**Missing Value Treatment:** Handle missing values with imputation or by creating new categories.
**Data Standardization:** Ensure consistent formatting (e.g., converting "70 kms" to numerical).
**Categorical Encoding:** Apply One-Hot or Label Encoding for categorical variables.
**Feature Scaling:** Normalize numerical features as required.
**Outlier Removal:** Remove or cap outliers to maintain data quality.

# 2.Exploratory Data Analysis (EDA):

**Descriptive Statistics:** Summarize key statistics for each variable.
**Data Visualization:** Use plots (scatter, box, histogram, etc.) to uncover trends.
**Feature Selection:** Identify influential features impacting price prediction.

![image](https://github.com/user-attachments/assets/6b0bf4a2-067c-4da4-bdcd-6640ad5ddd3d)
![image](https://github.com/user-attachments/assets/9ffaddb2-0a01-40aa-818d-3d0e4237621d)
![image](https://github.com/user-attachments/assets/6417f815-c62d-40f8-9c96-b217497051f9)
![image](https://github.com/user-attachments/assets/4bd90bea-0f7d-48e9-84c3-fc3199e69c13)
![image](https://github.com/user-attachments/assets/752b325d-351b-4a04-b8d9-5546c0da7a26)


# .Skewness Visualization 📊
To understand the distribution of car prices, we visualized the skewness before and after handling outliers:

# Before Handling Outliers: 
![image](https://github.com/user-attachments/assets/831dca62-0e13-4d22-85b3-ea23040f5872)

# After Handling Outliers:
![image](https://github.com/user-attachments/assets/69958ff1-060c-4197-9934-58b7a493ecf9)

# 3.Model Development:
**Train-Test Split:** Separate data into training and testing sets.
**Model Selection:** Choose suitable algorithms like Linear Regression, Random Forest, or Gradient Boosting.
**Hyperparameter Tuning:** Optimize model parameters for best performance.

# 4.Model Evaluation:
Use evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to assess model accuracy.

# 5.Optimization:
**Feature Engineering:** Create or refine features for enhanced prediction accuracy.
**Regularization:** Apply Lasso or Ridge to prevent model overfitting.

# 6.Deployment:
**Streamlit Application:** Build and deploy an interactive web app with user input options for real-time predictions.
**User Interface Design:** Ensure an intuitive, easy-to-navigate app layout.

# Project Evaluation Metrics 📏

**Model Performance:** MAE, MSE, R-squared.
**Data Quality:** Completeness and consistency of preprocessed data.
**Application Usability:** User feedback and satisfaction from using the Streamlit app.
**Documentation:** Clarity and comprehensiveness of project documentation.

# Data Set 📂

      Sources: Multiple Excel files from Car Dekho for different cities.
      Features: Includes car specifications like make, model, mileage, engine type, year, city, etc.
      Preprocessing Steps: Handled missing values, standardized formats, encoded categorical variables, and normalized numerical data.

# Project Deliverables 📝

**Source Code:**
        Data Preprocessing Script: For cleaning and structuring the data.
        EDA & Visualization: In-depth exploration of data patterns.
        Model Training & Tuning Scripts: Model training, evaluation, and hyperparameter tuning.
        Prediction Script: Generates predictions for new car data.
        Streamlit Application: Deployed interactive web application for price prediction.

# Streamlit Application 🌐

**Features:**
       User Input Options: Accepts details like make, model, fuel type, year, and city.
       Instant Price Prediction: Outputs a predicted price based on the input data.
       Interactive Visualizations: Displays historical pricing data, feature impacts, and more.

# Video Demonstration 🎥
Click below to watch how the Streamlit app works in this demonstration:

# THANK YOU 🤝
