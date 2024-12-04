import os
import pandas as pd
import streamlit as st
from joblib import load
from PIL import Image

# Load the Random Forest model and car data
model_path = os.path.join('mycdapp', 'Scripts', 'RFmodel.joblib')
data_path = os.path.join('mycdapp', 'Scripts', 'CarData_Cleaned_UsedCarPricePrediction.csv')
rf_model = load(model_path)
car_df = pd.read_csv(data_path)

# Map car colors to image file paths
color_image_map = {
    "white": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.01 PM.jpeg",
    "red": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.53.59 PM.jpeg",
    "black": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.00 PM (2).jpeg",
    "blue": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.00 PM.jpeg",
    "silver": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.02 PM.jpeg",
    "grey": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.04 PM.jpeg",
    "green": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.03 PM (3).jpeg",
    "yellow": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-04 at 3.36.11 PM.jpeg",
    "orange": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.53.59 PM (1).jpeg",
    "brown": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.02 PM (1).jpeg",
    "others": r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 12.54.03 PM (2).jpeg",
}

# Prediction function
def predict(data):
    data = pd.DataFrame(data, index=[0])
    prediction = rf_model.predict(data)
    return round(prediction[0], 2)  

# Display car details after prediction
def display_car_details(data, car_details):
    data_df = pd.DataFrame(data, index=[0])
    data_df['modelyear'] = data_df['modelyear'].astype(int)
    if car_details: 
        data_df['mileage'] = round(car_details.get('mileage', 0), 1)
        data_df['comfort_count'] = car_details.get('comfort_count', 0)
        data_df['top_features_count'] = car_details.get('top_features_count', 0)
        data_df['safety_count'] = car_details.get('safety_count', 0)
        data_df['displacement'] = car_details.get('displacement', 0)
        data_df['seats'] = car_details.get('seats', 0)
    else: 
        data_df['mileage'] = 0
        data_df['comfort_count'] = 0
        data_df['top_features_count'] = 0
        data_df['safety_count'] = 0
        data_df['displacement'] = 0
        data_df['seats'] = 0

    st.write("Car Details:")
    st.dataframe(data_df.style.format({'modelyear': '{:d}', 'mileage': '{:.1f}'}, na_rep='0'))

# Sidebar inputs
st.image(r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 7.09.23 PM.jpeg", width=900)
st.sidebar.image(r"C:\Users\Shalini\Downloads\WhatsApp Image 2024-12-02 at 7.09.22 PM.jpeg", width=200)
st.sidebar.header("Input Car Specifications:")

# Sidebar inputs
body_type = st.sidebar.selectbox("Select body type:", options=['All'] + list(car_df['body_type'].unique()))
available_fuel_types = car_df[car_df['body_type'] == body_type]['fuel_type'].unique() if body_type != 'All' else car_df['fuel_type'].unique()
fuel_type = st.sidebar.selectbox("Select fuel type:", options=['All'] + list(available_fuel_types))
available_brands = car_df[(car_df['body_type'] == body_type) & (car_df['fuel_type'] == fuel_type)]['brand'].unique() if fuel_type != 'All' else car_df['brand'].unique()
brand = st.sidebar.selectbox("Select the brand:", options=['All'] + list(available_brands))
filtered_models = car_df[(car_df['brand'] == brand) & (car_df['body_type'] == body_type) & (car_df['fuel_type'] == fuel_type)]['model'].unique() if brand != 'All' else car_df['model'].unique()
model = st.sidebar.selectbox("Select the model:", options=['All'] + list(filtered_models))
available_transmissions = car_df[(car_df['model'] == model)]['transmission'].unique() if model != 'All' else car_df['transmission'].unique()
transmission = st.sidebar.selectbox("Select transmission type:", options=['All'] + list(available_transmissions))
km_driven = st.sidebar.selectbox("Select kilometers driven:", options=['All'] + list(range(0, 100001, 5000)))  
owner_number = st.sidebar.selectbox("Enter number of previous owners:", options=['All'] + [1, 2, 3, 4, 5])
model_year = st.sidebar.selectbox("Enter the model year:", options=['All'] + list(range(1900, 2025)))  
insurance_validity = st.sidebar.selectbox("Select insurance validity:", options=['All'] + list(car_df['insurance_validity'].unique()))
color = st.sidebar.selectbox("Select the car color:", options=['All'] + list(car_df[car_df['model'] == model]['color'].unique() if model != 'All' else car_df['color'].unique()))
city = st.sidebar.selectbox("Select the city:", options=['All'] + list(car_df['city'].unique()))

car_details = car_df[car_df['model'] == model].iloc[0].to_dict() if model != 'All' else None

# Prepare input data for prediction
input_data = {
    'body_type': body_type if body_type != 'All' else "Unknown",
    'km': km_driven if km_driven != 'All' else 0,  
    'transmission': transmission if transmission != 'All' else "Unknown",
    'ownerno': owner_number if owner_number != 'All' else 0, 
    'brand': brand if brand != 'All' else "Unknown",
    'model': model if model != 'All' else "Unknown",
    'modelyear': model_year if model_year != 'All' else 0, 
    'insurance_validity': insurance_validity if insurance_validity != 'All' else "Unknown",
    'fuel_type': fuel_type if fuel_type != 'All' else "Unknown",
    'color': color if color != 'All' else "Unknown",
    'city': city if city != 'All' else "Unknown",
    'comfort_count': car_details.get('comfort_count', 0) if car_details else 0,
    'top_features_count': car_details.get('top_features_count', 0) if car_details else 0,
    'safety_count': car_details.get('safety_count', 0) if car_details else 0,
    'displacement': car_details.get('displacement', 0) if car_details else 0,
    'mileage': car_details.get('mileage', 0) if car_details else 0,
    'seats': car_details.get('seats', 0) if car_details else 0
}

# Convert input data to DataFrame
input_df = pd.DataFrame(input_data, index=[0])

# Ensure all necessary fields are present and fill NaNs
input_df.fillna({
    'km': 0,
    'modelyear': 0,
    'ownerno': 0,
    'comfort_count': 0,
    'top_features_count': 0,
    'safety_count': 0,
    'displacement': 0,
    'mileage': 0,
    'seats': 0
}, inplace=True)

# Button to trigger prediction
if st.sidebar.button("Predict Price"):
    try:
        # Make prediction
        predicted_price = predict(input_df)
        st.success(f"The predicted price is: ₹{predicted_price} Lakhs")

        # Display car details
        display_car_details(input_data, car_details)

        # Display selected color image
        image_path = color_image_map.get(color.lower(), None)  
        if image_path:
            st.image(image_path, caption=f"Selected Car Color: {color}", width=300)
        else:
            st.warning("No image path found for the selected color")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Button to display all data
if st.sidebar.button("Show All Cars Data"):
    st.subheader("All Available Cars Data")
    st.dataframe(car_df)


# Additional Information
st.sidebar.header("Additional Information")
st.sidebar.markdown("""
- **Objective:** To predict the price of used cars based on various specifications.
- **Features:**
    - Dynamic filtering of options based on user input.
    - Predicts car prices using a trained Random Forest model.
    - Displays relevant car details after prediction.
""")
