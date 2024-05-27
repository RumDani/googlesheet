import streamlit as st
import gspread
from google.oauth2 import service_account

# Function to load Google Sheets credentials from Streamlit secrets
def load_google_credentials():
    secrets = st.secrets["google_sheets"]
    return {
        "type": secrets["type"],
        "project_id": secrets["project_id"],
        "private_key_id": secrets["private_key_id"],
        "private_key": secrets["private_key"],
        "client_email": secrets["client_email"],
        "client_id": secrets["client_id"],
        "auth_uri": secrets["auth_uri"],
        "token_uri": secrets["token_uri"],
        "auth_provider_x509_cert_url": secrets["auth_provider_x509_cert_url"],
        "client_x509_cert_url": secrets["client_x509_cert_url"],
    }

# Function to increment the number in the Google Sheet
def increment_number(sheet):
    current_number = sheet.cell(1, 1).value
    if not current_number:
        current_number = 0
    else:
        current_number = int(current_number)
    new_number = current_number + 1
    sheet.update_cell(1, 1, new_number)

# Main function to run the Streamlit app
def main():
    st.title("Increment Number App")

    # Load Google Sheets credentials
    creds = load_google_credentials()
    client = gspread.service_account_from_dict(creds)
    sheet = client.open("YourGoogleSheetName").sheet1

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
        current_number = sheet.cell(1, 1).value
        st.write(f"New number: {current_number}")

if __name__ == "__main__":
    main()
