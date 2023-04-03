import streamlit as st
from PIL import Image
import pandas as pd
import requests
import json
import string

def intro():
    import streamlit as st

def get_counts():
    if demo_name=="Get Counts":
        st.subheader("Get segment count API")
        segID= st.text_input("Please insert SegmentID: ")
        # API endpoint URL
        API_URL = "https://api.thetradedesk.com/v3/authentication"
        # Data 
        data= {"Login": "ttd_api_startapp@startapp.com", 
        "Password": "sodaCSM2019!", 
        "TokenExpirationInMinutes": 1440.0}

        json_data = json.dumps(data)
        Headers = {"Content-Type": "application/json"}
        #
        response = requests.post(url=API_URL ,headers=Headers ,data=json_data)
        # Check if the request was successful
        if response.status_code >= 200 and response.status_code<300:
            data= response.json()  
            auth = data['Token']
        #  st.write("the token is"+ auth)
        else:
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
        # Check if the request was successful
        if response.status_code >= 200 and response.status_code<300 and (response.json())['ResultCount']!=0:
             data = response.json() 
             st.write(data)
        else:
             st.write("Could not retrieve data-plesae note that segmentID must be greater then 0 and valid")
    #   
    else:
        segID.clear()
        data.clear()
        
def Update_Segment_Name():
    if demo_name=="Update segment name":
        st.subheader("Update segment name and/or description API")
        segID2= st.text_input("Please insert SegmentID: ")
        NewSegName= st.text_input("Please insert the new segment name: ")
        NewDescription= st.text_input("Please insert the new description: ")
        # API endpoint URL
        API_URL = "https://api.thetradedesk.com/v3/authentication"
        # Data 
        data= {"Login": "ttd_api_startapp@startapp.com", 
        "Password": "sodaCSM2019!", 
        "TokenExpirationInMinutes": 1440.0}

        json_data = json.dumps(data)
        Headers = {"Content-Type": "application/json"}
        #
        response = requests.post(url=API_URL ,headers=Headers ,data=json_data)
        # Check if the request was successful
        if response.status_code >= 200 and response.status_code<300:
            data= response.json()  
            auth = data['Token']
        #  st.write("the token is"+ auth)
        else:
            st.write("Error: Could not retrieve Token from TTD.")
         #
        API_URL="https://api.thetradedesk.com/v3/thirdpartydata"
        #Start process
        #
        Headers = {"TTD-Auth": auth,
               "Content-Type": "application/json"}
        # data
        payload  = {"ProviderId": "startapp",
         "ProviderElementId":segID2 ,
         "ParentElementId": "customstartapp",
         "DisplayName":NewSegName,
         "Buyable": 1,
         "Description":NewDescription}
        #
        json_data = json.dumps(payload)
        #
        if NewSegName=="" or NewDescription=="" or segID2=="":
            flag=1
            st.write("Please insert all mandatory fields")
        else:
            flag=0
            response = requests.put(url=API_URL ,headers=Headers ,data =json_data)
        # Check if the request was successful
        if response.status_code >= 200 and response.status_code<300 and flag!=1  :
             data = response.json() 
             st.subheader("Segment name and/description updated successfully")
             st.write(data)
        else:
             st.write("Request was not succeeded")
                
    else:
        segID2.clear()
        data.clear()

page_names_to_funcs = {
    "—": intro,
    "Get Counts": get_counts,
    "Update segment name": Update_Segment_Name
   # "Mapping Demo": mapping_demo,
   # "DataFrame Demo": data_frame_demo
}

st.sidebar.title(" Welcome to Start.io's TTD's UI tool")
st.sidebar.subheader("""This tools was created to enable Start.io's team to get details/ update custom/prepack segments on TTD's side.""")

demo_name = st.sidebar.selectbox("Choose a UI", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()    
st.sidebar.success("Select a UI tool.")

