import streamlit as st
from google.oauth2 import service_account
import gspread
import pandas as pd
import json

# Load the service account key JSON file from the secret file
with open('/path/to/your/secrets/service_account.json') as f:
    creds_dict = json.load(f)

creds = service_account.Credentials.from_service_account_info(creds_dict)

# Initialize a connection to Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("Your Google Sheet Name").sheet1  # Replace with your actual sheet name

def increment_number():
    # Read the current number from the first cell (A1)
    current_number = sheet.cell(1, 1).value
    
    # If the cell is empty, start with 0
    if not current_number:
        current_number = 0
    else:
        current_number = int(current_number)
    
    # Increment the number
    new_number = current_number + 1
    
    # Update the cell with the new number
    sheet.update_cell(1, 1, new_number)

# Main Streamlit app
def main():
    st.title("Increment Number App")
    
    # Display the current number from the Google Sheet
    current_number = sheet.cell(1, 1).value
    if not current_number:
        current_number = 0
    else:
        current_number = int(current_number)
    
    st.write(f"Current number: {current_number}")
    
    # Button to increment the number
    if st.button("Increment Number"):
        increment_number()
        st.write("Number incremented successfully!")
        # Display the updated number
        current_number = sheet.cell(1, 1).value
        st.write(f"New number: {current_number}")

if __name__ == "__main__":
    main()
