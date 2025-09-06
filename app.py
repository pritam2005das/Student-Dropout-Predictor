# import necessary libraries
import streamlit as st
import pandas as pd
import cloudpickle

# Load model
with open("model.pkl", "rb") as f:
    model = cloudpickle.load(f)

# Categorical mappings
gender_map = {"Female": 0, "Male": 1}
marital_map = {"Single": 0, "Married": 1, "Divorced": 2, "Widowed": 3}
attendance_map = {"Daytime": 0, "Evening": 1}
yesno_map = {"No": 0, "Yes": 1}
application_mode_map = {"Online": 0, "In-Person": 1, "Referral": 2, "Other": 3}
course_map = {"Informatics":0, "Economics":1, "Law":2, "Medicine":3, "Other":4}
nationality_map = {"India":0, "Bangladesh":1, "Pakistan":2, "Other":3}
mother_qual_map = {"High School":0, "Bachelors":1, "Masters":2, "PhD":3, "Other":4}
father_qual_map = {"High School":0, "Bachelors":1, "Masters":2, "PhD":3, "Other":4}
mother_occ_map = {"Employed":0, "Unemployed":1, "Self-employed":2, "Other":3}
father_occ_map = {"Employed":0, "Unemployed":1, "Self-employed":2, "Other":3}
previous_qual_map = {"High School":0, "Bachelors":1, "Masters":2, "PhD":3, "Other":4}

# Streamlit app
st.title("🎓 Student Dropout Predictor")

# Personal Information
st.subheader("Personal Information")
gender = st.selectbox("Gender", list(gender_map.keys()))
age_at_enrollment = st.number_input(label="Age at Enrollment", min_value=15, max_value=80, step=1)
marital_status = st.selectbox("Marital Status", list(marital_map.keys()))
nationality = st.selectbox("Nationality", list(nationality_map.keys()))

# Application Details
st.subheader("Application Details")
application_mode = st.selectbox("Application Mode", list(application_mode_map.keys()))
application_order = st.number_input(label="Application Order", min_value=1, max_value=10, step=1)
course = st.selectbox("Course", list(course_map.keys()))
DE_attendance = st.selectbox("Daytime/Evening Attendance", list(attendance_map.keys()))

# Family Background
st.subheader("Family Background")
mothers_qualification = st.selectbox("Mother's Qualification", list(mother_qual_map.keys()))
fathers_qualification = st.selectbox("Father's Qualification", list(father_qual_map.keys()))
mothers_occupation = st.selectbox("Mother's Occupation", list(mother_occ_map.keys()))
fathers_occupation = st.selectbox("Father's Occupation", list(father_occ_map.keys()))

# Special Conditions
st.subheader("Special Conditions")
previous_qualification = st.selectbox("Previous Qualification", list(previous_qual_map.keys()))
displaced = st.selectbox("Displaced", list(yesno_map.keys()))
educational_special_needs = st.selectbox("Educational Special Needs", list(yesno_map.keys()))
debtor = st.selectbox("Debtor", list(yesno_map.keys()))
tution_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", list(yesno_map.keys()))
scholarship_holder = st.selectbox("Scholarship Holder", list(yesno_map.keys()))
international = st.selectbox("International", list(yesno_map.keys()))

# Academic Performance - 1st Semester
st.subheader("Academic Performance (1st Semester)")
curricular_units_1st_sem_credited = st.number_input(label="Credited Units", min_value=0, max_value=100, value=0, step=1)
curricular_units_1st_sem_enrolled = st.number_input(label="Enrolled Units", min_value=0, max_value=100, value=0, step=1)
curricular_units_1st_sem_evaluations = st.number_input(label="Evaluations", min_value=0, max_value=100, value=0, step=1)
curricular_units_1st_sem_approved = st.number_input(label="Approved Units", min_value=0, max_value=100, value=0, step=1)
curricular_units_1st_sem_grade = st.number_input(label="Average Grade", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
curricular_units_1st_sem_without_evaluations = st.number_input(label="Without Evaluations", min_value=0, max_value=100, value=0, step=1)

# Academic Performance - 2nd Semester
st.subheader("Academic Performance (2nd Semester)")
curricular_units_2nd_sem_credited = st.number_input(label="Credited Units (2nd Sem)", min_value=0, max_value=100, value=0, step=1)
curricular_units_2nd_sem_enrolled = st.number_input(label="Enrolled Units (2nd Sem)", min_value=0, max_value=100, value=0, step=1)
curricular_units_2nd_sem_evaluations = st.number_input(label="Evaluations (2nd Sem)", min_value=0, max_value=100, value=0, step=1)
curricular_units_2nd_sem_approved = st.number_input(label="Approved Units (2nd Sem)", min_value=0, max_value=100, value=0, step=1)
curricular_units_2nd_sem_grade = st.number_input(label="Average Grade (2nd Sem)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
curricular_units_2nd_sem_without_evaluations = st.number_input(label="Without Evaluations (2nd Sem)", min_value=0, max_value=100, value=0, step=1)

# Economic Indicators
st.subheader("Economic Indicators")
unemployment_rate = st.number_input(label="Unemployment Rate (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
inflation_rate = st.number_input(label="Inflation Rate (%)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
GDP = st.number_input(label="GDP (in billions)", min_value=0.0, max_value=100000.0, value=1000.0, step=100.0)

# Prediction
if st.button("Predict"):
    df = pd.DataFrame([{
        "Gender": gender_map[gender],
        "Marital status": marital_map[marital_status],
        "Application mode": application_mode_map[application_mode],
        "Course": course_map[course],
        "Daytime/evening attendance": attendance_map[DE_attendance],
        "Previous qualification": previous_qual_map[previous_qualification],
        "Nacionality": nationality_map[nationality],
        "Mother's qualification": mother_qual_map[mothers_qualification],
        "Father's qualification": father_qual_map[fathers_qualification],
        "Mother's occupation": mother_occ_map[mothers_occupation],
        "Father's occupation": father_occ_map[fathers_occupation],
        "Displaced": yesno_map[displaced],
        "Educational special needs": yesno_map[educational_special_needs],
        "Debtor": yesno_map[debtor],
        "Tuition fees up to date": yesno_map[tution_fees_up_to_date],
        "Scholarship holder": yesno_map[scholarship_holder],
        "International": yesno_map[international],
        "Age at enrollment": age_at_enrollment,
        "Application order": application_order,
        "Curricular units 1st sem (credited)": curricular_units_1st_sem_credited,
        "Curricular units 1st sem (enrolled)": curricular_units_1st_sem_enrolled,
        "Curricular units 1st sem (evaluations)": curricular_units_1st_sem_evaluations,
        "Curricular units 1st sem (approved)": curricular_units_1st_sem_approved,
        "Curricular units 1st sem (grade)": curricular_units_1st_sem_grade,
        "Curricular units 1st sem (without evaluations)": curricular_units_1st_sem_without_evaluations,
        "Curricular units 2nd sem (credited)": curricular_units_2nd_sem_credited,
        "Curricular units 2nd sem (enrolled)": curricular_units_2nd_sem_enrolled,
        "Curricular units 2nd sem (evaluations)": curricular_units_2nd_sem_evaluations,
        "Curricular units 2nd sem (approved)": curricular_units_2nd_sem_approved,
        "Curricular units 2nd sem (grade)": curricular_units_2nd_sem_grade,
        "Curricular units 2nd sem (without evaluations)": curricular_units_2nd_sem_without_evaluations,
        "Unemployment rate": unemployment_rate,
        "Inflation rate": inflation_rate,
        "GDP": GDP
    }])

    # Make prediction
    prediction = model.predict(df)[0]

    st.success(f"Prediction: {'Graduate' if prediction == 1 else 'Dropout'}")
