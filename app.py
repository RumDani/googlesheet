import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd
import toml

# Load secrets from the secrets.toml file
secrets = toml.load("secrets.toml")

# Initialize a connection to Google Sheets using the service account key from secrets
creds = service_account.Credentials.from_service_account_info(secrets["google_sheets"]["service_account_key"])
client = gspread.authorize(creds)
sheet = client.open("Your Google Sheet Name").sheet1  # Replace with your actual sheet name

def increment_number():
    current_number = sheet.cell(1, 1).value
    if not current_number:
        current_number = 0
    else:
        current_number = int(current_number)
    new_number = current_number + 1
    sheet.update_cell(1, 1, new_number)

def main():
    st.title("Increment Number App")
    
    current_number = sheet.cell(1, 1).value
    if not current_number:
        current_number = 0
    else:
        current_number = int(current_number)
    
    st.write(f"Current number: {current_number}")
    
    if st.button("Increment Number"):
        increment_number()
        st.write("Number incremented successfully!")
        current_number = sheet.cell(1, 1).value
        st.write(f"New number: {current_number}")

if __name__ == "__main__":
    main()
