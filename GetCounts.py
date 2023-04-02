import streamlit as st
import requests



# API endpoint URL
API_URL = "https://api.thetradedesk.com/v3/authentication"
#
Headers = {"Content-Type": "application/json"}

# Parameters 
Params= {"Login": "ttd_api_startapp@startapp.com", 
"Password": "sodaCSM2019!", 
"TokenExpirationInMinutes": 1440.0}

#
response = requests.get(API_URL)

# Check if the request was successful
if response.status_code == 200:
   data = response.json()
    TTD-Auth=data
else:
    st.write("Error: Could not retrieve Token from TTD.")
    
#
API_URL="https://api.thetradedesk.com/v3/thirdpartydata/query?TTD-Auth="TTD-Auth

Headers=
{"Content-Type": "application/json"}

segID=input("Please insert SegmentID:")

# Parameters
{ Params=  "ProviderId": "startapp",
  "ProviderElementId": ,
  "IncludeActiveIDsCountExpandedFlag":" true",
  "PageStartIndex":"0",
  "PageSize": "100"}
 
 # Check if the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
  
