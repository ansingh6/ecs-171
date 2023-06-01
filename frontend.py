import streamlit as st
import numpy as np
import pandas as pd
import json
import requests

# use this to actually get the prediction
def predictFunction(text):
    res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(text))
    output = res.json() # convert python parsed info to a dictionary
    st.write("Fraud probability: ", output["fraud_probability"][0])

    if (output["fraud_probability"][0] > 0.5):
        st.markdown("Fraud classification: **:red[True]**")
    else:
        st.markdown("Fraud classification: **:green[False]**")

# set state when input is disabled
if 'exception' not in st.session_state:
    st.session_state.exception = False

if 'select_setting' not in st.session_state:
    st.session_state.select_setting = True

# read csv file for pandas
postings = pd.read_csv('fake_job_postings.csv')
fraud_row = postings.iloc[843]

# remove nan's
postings = pd.DataFrame.dropna(postings)
postings = postings.head(10)

# title
st.title("Fraudulent Job Predictor")

# inputs
# title, department, company profile, etc.

setting = st.radio("Choose either text input or option selection: ", ('User Input', 'Selection'))
if setting == "User Input":
    st.session_state.select_setting = False
else:
    st.session_state.select_setting = True

if st.session_state.select_setting:
    title_arr, profile_arr = np.array(postings["title"]), np.array(postings["company_profile"])
    desc_arr, benefit_arr = np.array(postings["description"]), np.array(postings["benefits"])
    req_arr, location_arr = np.array(postings["requirements"]), np.array(postings["location"])
    dept_arr = np.array(postings["department"])

    # prepend arrays with empty strings
    title_arr, profile_arr = np.insert(title_arr, 0, ""), np.insert(profile_arr, 0, "")
    desc_arr, benefit_arr = np.insert(desc_arr, 0, ""), np.insert(benefit_arr, 0, "")
    req_arr, location_arr = np.insert(req_arr, 0, ""), np.insert(location_arr, 0, "")
    dept_arr = np.insert(dept_arr, 0, "")

    # add a fraudulent posting
    title_arr, profile_arr = np.insert(title_arr, title_arr.size, fraud_row["title"]), np.insert(profile_arr, profile_arr.size, fraud_row["company_profile"])
    desc_arr, benefit_arr = np.insert(desc_arr, desc_arr.size, fraud_row["description"]), np.insert(benefit_arr, benefit_arr.size, fraud_row["benefits"])
    req_arr, location_arr = np.insert(req_arr, req_arr.size, fraud_row["requirements"]), np.insert(location_arr, location_arr.size, fraud_row["location"])
    dept_arr = np.insert(dept_arr, dept_arr.size, fraud_row["department"])

    title = st.selectbox(
        label = 'Title',
        options = title_arr
    )

    profile = st.selectbox(
        label = 'Profile',
        options = profile_arr
    )

    desc = st.selectbox(
        label = 'Description',
        options = desc_arr
    )

    req = st.selectbox(
        label = 'Requirements',
        options = req_arr
    )        

    benefit = st.selectbox(
        label = 'Benefits',
        options = benefit_arr
    )

    department = st.selectbox(
        label = 'Job department',
        options = dept_arr
    )

    location = st.selectbox(
        label = 'Location',
        options = location_arr
    )

else: 
    title = st.text_input('Title', placeholder="Write the job title here")
    profile = st.text_input('Company Profile', placeholder='Insert the company profile here')
    desc = st.text_input('Description', placeholder="Write the job description here")
    req = st.text_input('Requirements', placeholder="List the job requirements")
    benefit = st.text_input('Benefits', placeholder="List benefits here")
    department = st.text_input('Department', placeholder="List the job department")
    location = st.text_input('Location', placeholder="Choose location")


feature_arr = [title, profile, desc, req, benefit, department, location]

for feat in feature_arr:
    if not feat or feat.isspace():
        st.session_state.exception = True
        st.error("No empty values allowed!")
        break
    else:
        st.session_state.exception = False

if not st.session_state.exception:
    combined_text = " ".join([profile, title, desc, department, req, benefit, location]) # concatenate
    # st.write(combined_text)
    text_dict = {
        "text": combined_text
    }
    predictFunction(text_dict)