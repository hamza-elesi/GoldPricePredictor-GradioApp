import gradio as gr
import pandas as pd
import joblib

# Load the trained models from the files
linear_model_filename = 'linear_regression_model.pkl'
forest_model_filename = 'forest_regressor_model.pkl'
linear_regressor = joblib.load(linear_model_filename)
forest_regressor = joblib.load(forest_model_filename)

def compare_models(SPX, USO, SLV, EURUSD):
    """
    Use both models to predict the GLD price based on input features
    and return both predictions for comparison.
    """
    features_df = pd.DataFrame([[SPX, USO, SLV, EURUSD]], columns=['SPX', 'USO', 'SLV', 'EUR/USD'])
    
    # Predict using Linear Regression
    linear_predicted_price = linear_regressor.predict(features_df)
    
    # Predict using Random Forest Regressor
    forest_predicted_price = forest_regressor.predict(features_df)
    
    # Convert NumPy floats to Python floats for compatibility
    return float(linear_predicted_price[0]), float(forest_predicted_price[0])

# Define the Gradio interface
def main():
    with gr.Blocks() as demo:
        gr.Markdown("## Gold Price Prediction Model Comparison 📊")
        gr.Markdown("This app compares predictions from a Linear Regression model and a Random Forest Regressor based on various economic indicators. Please enter the values for the following indicators:")
        
        # Input fields
        with gr.Row():
            SPX = gr.Number(label="SPX Index", precision=2)
            USO = gr.Number(label="USO (Oil)", precision=2)
            SLV = gr.Number(label="SLV (Silver)", precision=2)
            EURUSD = gr.Number(label="EUR/USD Exchange Rate", precision=4)
        
        # Button to trigger prediction
        predict_button = gr.Button("Compare Predictions")
        
        # Outputs to display predictions from both models
        output_linear = gr.Number(label="Linear Regression Predicted GLD Price")
        output_forest = gr.Number(label="Random Forest Predicted GLD Price")
        
        # Set up the button click action
        predict_button.click(
            fn=compare_models,
            inputs=[SPX, USO, SLV, EURUSD],
            outputs=[output_linear, output_forest]
        )
    
    demo.launch(share=True)

if __name__ == "__main__":
    main()
