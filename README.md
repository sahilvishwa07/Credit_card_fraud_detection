# Credit Card Fraud Detection with Machine Learning
- **Web Interface** (`frontend.py`): Interactive Streamlit application for real-time fraud prediction
- **Pre-trained Model**: Serialized LightGBM model and label encoders ready for inference

### 🌐 Live Demo
Try the working application here: [https://creditcardfraud0detection.streamlit.app/]
(https://creditcardfraud0detection.streamlit.app/)

## ✨ Features

- **Real-time Fraud Detection**: Enter transaction details to get instant predictions
- **Geographic Distance Calculation**: Computes distance between cardholder and merchant locations using the Haversine formula
- **Temporal Features**: Uses hour, day, and month from transaction data
- **Categorical Encoding**: Handles merchant, category, and gender encoding
- **Interactive Web Interface**: User-friendly Streamlit application for making predictions
- **Pre-trained Model**: LightGBM classifier ready to use without additional training



## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sahilvishwa07/Credit_card_fraud_detection.git
   cd Credit_card_fraud_detection
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Fraud Detection App

Launch the interactive Streamlit interface:

```bash
streamlit run frontend.py
```

The app will open at `http://localhost:8501`

### Input Transaction Details

Enter the following information:
- **Merchant Name**: Name of the merchant
- **Category**: Transaction category
- **Amount**: Transaction amount in dollars
- **Transaction Location**: Latitude and longitude where transaction occurred
- **Merchant Location**: Merchant's latitude and longitude
- **Time**: Hour (0-23), day (1-31), and month (1-12) of transaction
- **Gender**: Cardholder's gender (Male/Female)
- **Credit Card Number**: Cardholder's credit card number

Click **"Predict Fraud"** to get the prediction result.

## 📁 Project Structure

```
Credit_card_fraud_detection/
├── frontend.py                    # Streamlit web application
├── fraud_detection_model.jb       # Trained LightGBM model
├── label_encoders.jb              # Categorical encoders
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🤖 Model Details

### Algorithm
**LightGBM** (Light Gradient Boosting Machine) - A fast, distributed gradient boosting framework

### Model Configuration
- **Boosting Type**: GBDT (Gradient Boosting Decision Tree)
- **Objective**: Binary Classification
- **Metric**: AUC (Area Under Curve)
- **Learning Rate**: 0.05
- **Number of Leaves**: 31
- **Number of Estimators**: 200

### Features Used
The model uses 9 key features for prediction:
1. Merchant name (encoded)
2. Transaction category (encoded)
3. Transaction amount
4. Credit card number
5. Transaction hour
6. Transaction day
7. Transaction month
8. Cardholder gender (encoded)
9. Geographic distance (Haversine)

## 🛠 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Scikit-learn** | Machine learning utilities |
| **LightGBM** | Gradient boosting classifier |
| **GeoPy** | Geographic distance calculations |
| **Streamlit** | Web application framework |
| **Joblib** | Model serialization |

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For questions or feedback, please reach out to [sahilvishwa07](https://github.com/sahilvishwa07).

---

**Note**: This model is intended for educational and demonstration purposes. In production environments, additional considerations such as data privacy, model interpretability, and regulatory compliance should be addressed.
