# Predictive Analytics for Real Estate Price System

## Overview

The Predictive Analytics for Real Estate Price System is designed to predict house prices in Sydney based on user-specified features. The system leverages historical and live data to provide accurate and up-to-date predictions, assisting buyers, real estate agents, and brokers in making informed decisions. The product consists of a front-end interface for users and a back-end machine learning model for predictions.

## Table of Contents

1. [Front-End](#front-end)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Features](#features)
2. [Machine Learning Model](#machine-learning-model)
    - [Installation](#installation-1)
    - [Usage](#usage-1)
    - [Data Requirements](#data-requirements)
    - [Model Training](#model-training)
    - [Prediction](#prediction)

## Front-End & Machine Learning

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ClaytonLesmana/Data-Systems-Real-Estate-Prediction.git
    cd Data-Systems-Real-Estate-Prediction/frontend
    ```

2. Run the file main.py:

4. Open your browser and navigate to the link provided.

### Usage

- **Home Page**: Provides an overview of the system and its features.
- **Prediction Page**: Allows users to input property details (e.g., address, property type, area, number of bedrooms, number of bathrooms, suburb) and get a predicted price.
- **Contact Page**: A function that allows user to contact us

### Features

- **User-Friendly Interface**: Intuitive design for users with any level of background information.
- **Real-Time Predictions**: Get instant price predictions based on the latest data.

## Machine Learning Model

### Data Requirements

- **Suburb Data**: Information about suburbs including name, postcode, population, elevation, and distance from the city.
- **Property Data**: Details of properties including address, type, area, number of bedrooms, number of bathrooms, and suburb name.
- **Market Trends Data**: Historical market trends with timestamps and trend types.
- **Property Price Data**: Historical property prices for model training.

### Model Training

1. **Data Preprocessing**:
    - Clean and format the data.
    - Handle missing values and outliers.
    - Normalize or standardize features as required.

2. **Model Selection**:
    - Choose appropriate machine learning algorithms (e.g., linear regression, random forest, gradient boosting).

3. **Training**:
    - Split data into training and testing sets.
    - Train the model using the training set.
    - Evaluate the model using the testing set.

4. **Model Evaluation**:
    - Assess model performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

5. **Model Saving**:
    - Save the trained model for future predictions.

### Prediction

- **Input**: Accepts features such as address, property type, area, number of bedrooms, number of bathrooms, and suburb name.
- **Output**: Returns a predicted price based on the input features.

For further details or support, please refer to the documentation or contact the project maintainer.
