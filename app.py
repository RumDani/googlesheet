import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd
import toml

def load_google_credentials():
    # Load credentials from secrets.toml
    secrets = toml.load("secrets.toml")
    google_sheets_secrets = secrets["google_sheets"]

    creds = service_account.Credentials.from_service_account_info(
        {
            "type": google_sheets_secrets["type"],
            "project_id": google_sheets_secrets["project_id"],
            "private_key_id": google_sheets_secrets["private_key_id"],
            "private_key": google_sheets_secrets["private_key"],
            "client_email": google_sheets_secrets["client_email"],
            "client_id": google_sheets_secrets["client_id"],
            "auth_uri": google_sheets_secrets["auth_uri"],
            "token_uri": google_sheets_secrets["token_uri"],
            "auth_provider_x509_cert_url": google_sheets_secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": google_sheets_secrets["client_x509_cert_url"]
        }
    )
    return creds

def increment_number(sheet):
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
    
    # Initialize a connection to Google Sheets
    creds = load_google_credentials()
    client = gspread.authorize(creds)

    # Open the Google Sheet by name
    sheet_name = "Your Google Sheet Name"  # Replace with your actual sheet name
    sheet = client.open(sheet_name).sheet1
    
    # Display the current number from the Google Sheet
    current_number = sheet.cell(1, 1).value
    if not current_number:
        current_number = 0
    else:
        current_number = int(current_number)
    
    st.write(f"Current number: {current_number}")
    
    # Button to increment the number
    if st.button("Increment Number"):
        increment_number(sheet)
        st.write("Number incremented successfully!")
        # Display the updated number
        current_number = sheet.cell(1, 1).value
        st.write(f"New number: {current_number}")

if __name__ == "__main__":
    main()
