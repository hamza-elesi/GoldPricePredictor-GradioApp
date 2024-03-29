# Gold Price Prediction with Machine Learning and Gradio

Welcome to the Gold Price Prediction project! This repository houses a sophisticated machine learning application designed to forecast gold prices using key economic indicators. Leveraging the power of both RandomForestRegressor and Linear Regression models, we aim to provide accurate and insightful predictions. To bridge the gap between complex data science and user accessibility, we've developed an interactive web application utilizing Gradio, allowing users from all backgrounds to engage with our predictions effortlessly.

Dive into the source code to unravel the magic behind our models, or jump straight into making predictions with our easy-to-use web interface.

## Features
- **Predict gold prices** with just a few clicks using pivotal economic indicators: SPX Index, USO (Oil), SLV (Silver), and EUR/USD Exchange Rate.
- **User-friendly Gradio web app** for seamless interaction without the need for coding.
- **In-depth evaluation metrics** to understand model performance comprehensively.

## Getting Started

### Meta-data
Our models use the following indicators to predict gold prices:
1. **SPX**: S&P 500 index prices
2. **GLD**: Gold prices
3. **USO**: US Oil prices
4. **SLV**: Silver prices
5. **EUR/USD**: Euro to US Dollar exchange rate

### Prerequisites
Ensure you have Python 3.10 installed, as our models are optimized for this version. Additionally, the following packages are required:
- gradio
- joblib==1.1.1
- scikit-learn==1.3.1
- numpy
- seaborn

### Installation
To set up your local environment:
1. Clone the repository:
   ```sh
   git clone https://github.com/hamza-elesi/GoldPricePredictor-GradioApp.git
   ```
2. Navigate to the project directory and install the required packages:
   ```sh
   cd GoldPricePredictor-GradioApp
   pip install -r requirements.txt
   ```

### Launch the Application
Run the Gradio app with the following command:
```sh
python gradio_app.py in our case we have : gradioForest_app & gradioReg_app and fullapp
```
Follow the instructions in your terminal to access the web interface.

## Contributing
Your contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contributors
- [Hamza EL MAATAOUI](https://github.com/hamza-elesi) - *Initial Work*

## Acknowledgements
This project was developed with ❤️ and a deep interest in economic forecasting. We hope it serves as a useful tool for those looking to understand the intricacies of gold price movements.

## Contact
For any queries, feel free to contact us:
- [Linkedin : Hamza EL MAATAOUI ](https://www.linkedin.com/in/hamza-el-maataoui/)
Project Link: [https://github.com/hamza-elesi/GoldPricePredictor-GradioApp](https://github.com/hamza-elesi/GoldPricePredictor-GradioApp)
