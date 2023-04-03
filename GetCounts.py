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
if response.status_code >= 200 and response.status_code<300:
    data= response.json()  
    auth = data['Token']
    st.write("the token is"+ auth)
else:
    st.write("Error: Could not retrieve Token from TTD.")
    sys.exit(1)
    
#
API_URL="https://api.thetradedesk.com/v3/thirdpartydata/query"
#
Headers = {"TTD-Auth": auth,
           "Content-Type": "application/json"}
       
#Start process
segID=input("Please insert SegmentID:")

# Parameters
Params = {"ProviderId": "startapp",
  "ProviderElementId":segID ,
  "IncludeActiveIDsCountExpandedFlag":" true",
  "PageStartIndex":"0",
  "PageSize": "100"}
 
 # Check if the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
  
