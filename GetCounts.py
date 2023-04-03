import streamlit as st
import requests
import json



# API endpoint URL
API_URL = "https://api.thetradedesk.com/v3/authentication"

# Data 
data= {"Login": "ttd_api_startapp@startapp.com", 
"Password": "sodaCSM2019!", 
"TokenExpirationInMinutes": 1440.0}
#
json_data = json.dumps(data)
#
Headers = {"Content-Type": "application/json"}
#
response = requests.post(API_URL ,Headers ,json_data)

# Check if the request was successful
if response.status_code >= 200 and response.status_code<300:
    data= response.json()  
    auth = data['Token']
    st.write("the token is"+ auth)
else:
        st.write(response.status_code)
        st.write("Error: Could not retrieve Token from TTD.")
    
#
API_URL="https://api.thetradedesk.com/v3/thirdpartydata/query"
#
Headers = {"TTD-Auth": auth,
           "Content-Type": "application/json"}
       
#Start process
segID=input("Please insert SegmentID:")

# data
data = {"ProviderId": "startapp",
  "ProviderElementId":segID ,
  "IncludeActiveIDsCountExpandedFlag":" true",
  "PageStartIndex":"0",
  "PageSize": "100"}
 
 # Check if the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
  
