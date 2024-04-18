import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.ensemble import RandomForestClassifier

# Memisahkan fitur (X) dan target (y)


X_train=pd.read_csv('model/X_train.csv' ,usecols=lambda column: column not in ['Unnamed: 0', 'index'])
y_train=pd.read_csv('model/y_train.csv' ,usecols=lambda column: column not in ['Unnamed: 0', 'index'])
model = RandomForestClassifier()

joblib.dump(model, 'model/random_forest_classifier.joblib')

# Saat memuat model:
model = joblib.load('model/random_forest_classifier.joblib')
model.fit(X_train, y_train)

# Fungsi untuk halaman Home
def home():
    st.title("Welcome to Customer Churn Prediction")

    # Tampilkan navigasi
    st.write()
    menu = ["Home", "About", "Prediction App"]
    choice = st.sidebar.radio("", menu)

    if choice == "Home":
        # Tampilkan pesan selamat datang
        st.write("""
        Predict whether a customer will churn or be retained based on provided data.
        """)
      

        st.write("---")
        st.subheader('Evaluasi Model')

        show_image = "images/acuracy.png"  
        st.image(show_image, width=100, use_column_width=True)
        show_image = "images/roccomparison.png"  
        st.image(show_image, width=100, use_column_width=True)


        st.markdown("""
        <p style='text-align: justify;'>
        Comparison of the three machine learning models on accuracy and also ROC AUC.
        Random Forest has the highest value in both comparisons. The advantage of
        Random Forest is its flexibility and ease of use, as well as its ability to predict accurately
        and stable.</p>
        """, unsafe_allow_html=True)

        st.write("---")
    

        show_image = "images/confusion.png"  
        st.image(show_image, width=100, use_column_width=True)
    
        st.markdown("""
        <p style='text-align: justify;'>
        <b>Plot into Confusion Matrix</b>
        Out of 1754 data, 219 are False Negatives
        Out of 246 data, 58 are False Positives
        Accuracy = (True Positives + True Negatives) / Total Test Data
        = ((1535 + 188) / 2000) * 100%
        = 86.15%.</p>
        """, unsafe_allow_html=True)

        st.write("---")
        show_image = "images/ROC.png"  
        st.image(show_image, width=100, use_column_width=True)
    
        st.markdown("""
        <p style='text-align: justify;'>
        From the curve above, the Area Under the Curve (AUC) for the ROC curve is 0.71, 
        indicating that the model has better quality than random prediction (AUC-ROC value > 0.5).
        </p>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("""
        Please check the prediction results in the <b>Prediction App</b> menu.
        """, unsafe_allow_html=True)





    elif choice == "Prediction App":
        # Create input form for the user to input data
        st.sidebar.header("Input Customer Data")

        with st.sidebar.form("input_form"):
            customer_id = st.number_input("Customer ID", value=72322212)
            credit_score = st.number_input("Credit Score", value=645)
            gender = st.radio("Gender", ["Male", "Female"])
            age = st.number_input("Age", value=44)
            tenure = st.number_input("Tenure", value=8)
            balance = st.number_input("Balance", value=113755.78)
            products_number = st.number_input("Number of Products", value=2)
            credit_card = st.checkbox("Has Credit Card")
            active_member = st.checkbox("Active Member")
            estimated_salary = st.number_input("Estimated Salary", value=149756.71)
            country = st.selectbox("Country", ["France", "Germany", "Spain"])
            submit_button = st.form_submit_button("Predict")

        # Create a DataFrame from the input data
        data_baru = pd.DataFrame({
            'customer_id': [customer_id],
            'credit_score': [credit_score],
            'gender': [gender],
            'age': [age],
            'tenure': [tenure],
            'balance': [balance],
            'products_number': [products_number],
            'credit_card': [1 if credit_card else 0],
            'active_member': [1 if active_member else 0],
            'estimated_salary': [estimated_salary],
            'France': [1 if country == "France" else 0],
            'Germany': [1 if country == "Germany" else 0],
            'Spain': [1 if country == "Spain" else 0]
        })

        data_baru = data_baru.drop('customer_id', axis=1)

        # Data preprocessing
        category_mappings = {
            "gender": {"Male": 1, "Female": 0}
        }
        data_baru.replace(category_mappings, inplace=True)

        # Define the feature columns used during training (replace with your actual feature names)
        data_baru = data_baru[X_train.columns]

        # Scale the new data using the same scaler used for training
        scaler = StandardScaler()

        # Fit the scaler on the training data (X_train) before transforming
        scaler.fit(X_train)

        # Transform the new data (data_baru) using the fitted scaler
        scaled_data_baru = scaler.transform(data_baru)

        # Make predictions using the trained model when the form is submitted
        if submit_button:
            prediction = model.predict(scaled_data_baru)
            probability = model.predict_proba(scaled_data_baru)

            st.subheader("Prediction Result")
            if prediction[0] == 1:
                st.success("Customer: Churn")
            else:
                st.success("Customer: Retained")

            st.subheader("Prediction Probabilities")
            st.write(f"Probability of Churn: {probability[0][1]*100:.2f}%")
            st.write(f"Probability of Retained: {probability[0][0]*100:.2f}%")

    elif choice == "About":
        # Tampilkan halaman About
        st.title("About This App")
        st.write("""
        This web application is built to predict whether a customer will churn (leave) or be retained based on the provided customer data. It uses a trained machine learning model to make predictions.

        - **Model**: Random Forest Classifier
        - **Features**: Credit Score, Gender, Age, Tenure, Balance, Number of Products, Has Credit Card, Active Member, Estimated Salary, Country
        - **Data Source**: Dummy data for demonstration purposes.

        Feel free to use the input form to make predictions or explore other features of this app.
        """)
        

# Define the Streamlit app
def main():
    home()  # Tampilkan halaman Home secara default

if __name__ == '__main__':
    main()