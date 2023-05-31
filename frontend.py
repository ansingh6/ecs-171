import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_text as text
import json
import requests

# use this to actually get the prediction
def predictFunction(text):
    res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(text))
    output = res.json() # convert python parsed info to a dictionary
    st.write("Fraud probability: ", output["fraud_probability"][0])

    if (output["fraud_probability"][0] > 0.5):
        st.write("Fraud classification: True")
    else:
        st.write("Fraud classification: False")

# set state when input is disabled
if 'exception' not in st.session_state:
    st.session_state.exception = False

if 'profile_input' not in st.session_state:
    st.session_state.profile_input = "..."

# title
st.title("Fraudulent Job Posting Model")

# arrays for selectboxes
dept_arr, country_arr = ['Accounting', 'Sales', 'Engineering', 'Marketing'], ["United States of America", "Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua & Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

# inputs
# title, department, company profile, etc.

title = st.text_input('Title', placeholder="Write the job title here")
if not title or title.isspace():
    st.error("Can't input an empty value, try again!", icon="🚨")

profile = st.text_input('Company Profile', placeholder='Insert the company profile here')
if not profile or profile.isspace():
    st.error("Can't input an empty value, try again!", icon="🚨")

desc = st.text_input('Description', placeholder="Write the job description here")
if not desc or desc.isspace():
    st.error("Can't input an empty value, try again!", icon="🚨")

req = st.text_input('Requirements', placeholder="List the job requirements")
if not req or req.isspace():
    st.error("Can't input an empty value, try again!", icon="🚨")

benefit = st.text_input('Benefits', placeholder="List benefits here")
if not benefit or benefit.isspace():
    st.error("Can't input an empty value, try again!", icon="🚨")

department = st.selectbox(
    label = 'Job department',
    options = dept_arr
)

country = st.selectbox(
    label = 'Country',
    options = country_arr
)

city = st.text_input('City', placeholder="City within selected country")
if not city or city.isspace():
    st.error("Can't input an empty value, try again!", icon="🚨")

feature_arr = [title, profile, desc, req, benefit, department, country, city]

for feat in feature_arr:
    if not feat or feat.isspace():
        st.session_state.exception = True
        break
    else:
        st.session_state.exception = False

if not st.session_state.exception:
    combined_text = " ".join([profile, title, desc, department, req, benefit, country, city]) # concatenate
    text_dict = {
        "text": combined_text
    }
    predictFunction(text_dict)