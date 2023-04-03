import streamlit as st
from PIL import Image
import pandas as pd
import requests
import json
import string

def intro():
    import streamlit as st


page_names_to_funcs = {
    "—": intro
  #  "Plotting Demo": plotting_demo,
   # "Mapping Demo": mapping_demo,
   # "DataFrame Demo": data_frame_demo
}
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

my_logo = add_logo(logo_path="C:/Users/MaorKaufman/Downloads/StartLogo.jpg", width=50, height=60)
st.sidebar.image(my_logo)
st.sidebar.title(" Welcome to Start.io's TTD's UI tool")
st.sidebar.subheader("""This tools was created to enable Start.io's team to get details/ update custom/prepack segments on TTD's side.""")

demo_name = st.sidebar.selectbox("Choose a UI", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()    
st.sidebar.success("Select a UI tool.")


#
st.subheader("Get segment count API")
segID= st.text_input("Please insert SegmentID: ")

# API endpoint URL
API_URL = "https://api.thetradedesk.com/v3/authentication"

# Data 
data= {"Login": "ttd_api_startapp@startapp.com", 
"Password": "sodaCSM2019!", 
"TokenExpirationInMinutes": 1440.0}
#
# st.write(type(json.dumps(data)))
json_data = json.dumps(data)
#
Headers = {"Content-Type": "application/json"}
#
response = requests.post(url=API_URL ,headers=Headers ,data=json_data)

# Check if the request was successful
if response.status_code >= 200 and response.status_code<300:
    data= response.json()  
    auth = data['Token']
  #  st.write("the token is"+ auth)
else:
     #   st.write(response.status_code)
      #  st.write(response.json()['Token']) 
        st.write("Error: Could not retrieve Token from TTD.")
    
#
API_URL="https://api.thetradedesk.com/v3/thirdpartydata/query"
       
#Start process
#segID=input("Please insert SegmentID:")
#
Headers = {"TTD-Auth": auth,
           "Content-Type": "application/json"}
# data
data = {"ProviderId": "startapp",
  "ProviderElementId":segID ,
  "IncludeActiveIDsCountExpandedFlag":" true",
  "PageStartIndex":"0",
  "PageSize": "100"}
#
json_data = json.dumps(data)
#

response = requests.post(url=API_URL ,headers=Headers ,data=json_data)
#
#st.write(response.status_code)
      #  st.write(response.json()['Token']) 
# Check if the request was successful
if response.status_code >= 200 and response.status_code<300 and (response.json())['ResultCount']!=0:
    data = response.json() 
    st.write(data)
else:
     st.write("Could not retrieve data-plesae note that segmentID must be greater then 0 and valid")
    

