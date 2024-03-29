# Gold Price Prediction with Machine Learning and Gradio

Welcome to the Gold Price Prediction project! This repository contains a machine learning model that forecasts gold prices using economic indicators, built with a RandomForestRegressor & Linear Regression model. To make our predictions accessible to everyone, we've created an interactive web app using Gradio . Whether you're a financial analyst, a data science enthusiast, or just curious, you can easily predict gold prices without writing a single line of code!

Of course there the soruce code if you want to check.

## Features
- Predict gold prices using SPX Index, USO (Oil), SLV (Silver), and EUR/USD Exchange Rate.
- Interactive Gradio web app for easy use.
- Comprehensive evaluation metrics for model performance analysis.

## Getting Started

**Meta-data**

1. SPX (presumably S&P 500 index prices)
2. GLD (Gold prices)
3. USO (US Oil prices)
4. SLV (Silver prices)
5. EUR/USD (Euro to US Dollar exchange rate)

### Prerequisites
- Python 3.6+ use 3.10
- gradio
- joblib==1.1.1  # Adjust to the version you need this version is compatbile with scikit-learn==1.3.1
- scikit-learn==1.3.1  # Use the version compatible with your saved model
- numpy
- seaborn

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/hamza-elesi GoldPricePredictor-GradioApp.git
