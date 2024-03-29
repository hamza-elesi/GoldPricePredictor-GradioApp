import gradio as gr
import pandas as pd
import joblib

# Load the trained model from the file
model_filename = 'linear_regression_model.pkl'
linear = joblib.load(model_filename)

def predict_gld_price(SPX, USO, SLV, EURUSD):
    """
    Predict the GLD price based on input features.
    """
    features_df = pd.DataFrame([[SPX, USO, SLV, EURUSD]], columns=['SPX', 'USO', 'SLV', 'EUR/USD'])
    predicted_price = linear.predict(features_df)
    return float(predicted_price[0])  # Convert NumPy float to Python float

# Define the Gradio interface
def main():
    with gr.Blocks() as demo:
        gr.Markdown("## Gold Price Prediction Model Using Linear Regression 📈")
        gr.Markdown("This model predicts the GLD price based on various economic indicators. Please enter the values for the following indicators:")
        with gr.Row():
            SPX = gr.Number(label="SPX Index")
            USO = gr.Number(label="USO (Oil)")
            SLV = gr.Number(label="SLV (Silver)")
            EURUSD = gr.Number(label="EUR/USD Exchange Rate")
        predict_button = gr.Button("Predict GLD Price")
        
        output_label = gr.Number(label="Predicted GLD Price")

        predict_button.click(
            fn=predict_gld_price, 
            inputs=[SPX, USO, SLV, EURUSD], 
            outputs=output_label
        )
    
    demo.launch(share=True)

if __name__ == "__main__":
    main()