import streamlit as st
import pandas as pd
import requests
import json

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
if response.status_code >= 200 and response.status_code<300 and segID!=null:
    data = response.json() 
    st.write(data)
else:
    st.write("could not retrieve data")
