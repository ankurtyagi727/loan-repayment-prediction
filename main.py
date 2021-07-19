#%%writefile app.py
import pickle
import streamlit as st

# Load trained model
pickle_in = open("pick.pkl", 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
def prediction(loan_amnt, term, int_rate,installment, grade, emp_length,annual_inc_log, dti,fico_range_low, inq_last_6mths):

    prediction = classifier.predict([[loan_amnt, term, int_rate,installment, grade, emp_length,annual_inc_log, dti,fico_range_low, inq_last_6mths]])


    if prediction == 0:
        pred = "Charged Off"
    else:
        pred = "Fully Paid"
    return pred


# Main function:
def main():
    # Front end Elements:
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Lending Club Loan Prediction ML App</h1>
    </div>
    """

    # Display aspect of front end
    st.markdown(html_temp, unsafe_allow_html=True)
    Loan_Amount = st.number_input("Loan Amount")
    Term = st.number_input("Term")
    Interest_Rate = st.number_input("Interest Rate")
    Installment = st.number_input("Installment")
    Grade = st.number_input("Grade")
    Employee_Length = st.number_input("Employee Length")
    Annual_Income = st.number_input("Annual Income")
    Debt_To_Income_Ratio = st.number_input("Debt To Income Ratio")
    Fico_range_low = st.number_input("Fico_range(low) ")
    Inq_last_6mths = st.number_input("Inquiry in last 6 months")

    # When Predict is clicked:
    if st.button("Predict"):
        result = prediction(Loan_Amount,Term,Interest_Rate ,Installment,Grade,Employee_Length,Annual_Income,
                            Debt_To_Income_Ratio,
                            Fico_range_low,Inq_last_6mths )
        st.success(f"Your Loan is {result}")
        print(Loan_Amount)


if __name__ == '__main__':
    main()
