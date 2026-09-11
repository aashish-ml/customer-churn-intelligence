import streamlit as st
import requests


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)


# ==================================================
# TITLE
# ==================================================

st.title("📊 Customer Churn Prediction")

st.write(
    "Predict whether a customer is likely to churn "
    "using a trained Machine Learning model."
)

st.divider()


# ==================================================
# FASTAPI URL
# ==================================================

API_URL = "http://127.0.0.1:8000/predict"


# ==================================================
# CUSTOMER INPUT
# ==================================================

st.subheader("🔍 Customer Information")


tenure = st.number_input(
    "Tenure (months)",
    min_value=0.0,
    value=12.0,
    step=1.0
)


monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0,
    step=1.0
)


total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0,
    step=10.0
)


# ==================================================
# PREDICTION
# ==================================================

if st.button("🔮 Predict Churn", use_container_width=True):

    # ----------------------------------------------
    # Prepare data
    # ----------------------------------------------

    payload = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }


    try:

        # ------------------------------------------
        # Send request to FastAPI
        # ------------------------------------------

        response = requests.post(
            API_URL,
            json=payload,
            timeout=10
        )


        # ------------------------------------------
        # Successful response
        # ------------------------------------------

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]

            probability = result["churn_probability"]

            probability_percent = probability * 100


            # ======================================
            # PREDICTION RESULT
            # ======================================

            st.divider()

            st.subheader("📈 Prediction Result")


            # --------------------------------------
            # Prediction message
            # --------------------------------------

            if prediction == 1:

                st.error(
                    "🔴 Customer is likely to churn"
                )

            else:

                st.success(
                    "🟢 Customer is unlikely to churn"
                )


            # ======================================
            # RISK LEVEL
            # ======================================

            if probability_percent < 30:

                risk_level = "Low Risk"

            elif probability_percent < 60:

                risk_level = "Moderate Risk"

            else:

                risk_level = "High Risk"


            # ======================================
            # METRICS
            # ======================================

            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "Churn Probability",
                    f"{probability_percent:.1f}%"
                )


            with col2:

                st.metric(
                    "Risk Level",
                    risk_level
                )


            # ======================================
            # RISK BAR
            # ======================================

            st.write("### 📊 Churn Risk")

            st.progress(
                min(max(probability, 0.0), 1.0)
            )


            # ======================================
            # INTERPRETATION
            # ======================================

            if probability_percent < 30:

                st.info(
                    "💡 Very low churn probability. "
                    "The customer appears highly stable."
                )


            elif probability_percent < 60:

                st.warning(
                    "⚠️ Moderate churn probability. "
                    "Consider monitoring this customer."
                )


            else:

                st.error(
                    "🚨 High churn probability. "
                    "Customer retention action is recommended."
                )


            # ======================================
            # CUSTOMER DETAILS
            # ======================================

            st.write("### 👤 Customer Details")

            detail_col1, detail_col2, detail_col3 = st.columns(3)


            with detail_col1:

                st.metric(
                    "Tenure",
                    f"{tenure:.0f} months"
                )


            with detail_col2:

                st.metric(
                    "Monthly Charges",
                    f"${monthly_charges:.2f}"
                )


            with detail_col3:

                st.metric(
                    "Total Charges",
                    f"${total_charges:.2f}"
                )


        # ==========================================
        # API ERROR
        # ==========================================

        else:

            st.error(
                f"❌ API Error: {response.status_code}"
            )

            st.write(response.text)


    # ==============================================
    # CONNECTION ERROR
    # ==============================================

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to the FastAPI server."
        )

        st.info(
            "Please make sure FastAPI is running at "
            "http://127.0.0.1:8000"
        )


    # ==============================================
    # TIMEOUT ERROR
    # ==============================================

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ API request timed out."
        )


    # ==============================================
    # OTHER ERRORS
    # ==============================================

    except Exception as e:

        st.error(
            f"❌ Unexpected error: {e}"
        )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Customer Churn Intelligence • "
    "Machine Learning + FastAPI + Streamlit"
)