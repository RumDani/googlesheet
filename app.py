import streamlit as st
import gspread
from google.oauth2 import service_account

def load_google_credentials():
    try:
        secrets = st.secrets["connections.gsheets"]
        return {
            "type": secrets["type"],
            "project_id": secrets["project_id"],
            "private_key_id": secrets["private_key_id"],
            "private_key": secrets["private_key"].replace('\\n', '\n'),  # Kicseréli a '\n' escape karaktereket valódi sortörésekre
            "client_email": secrets["client_email"],
            "client_id": secrets["client_id"],
            "auth_uri": secrets["auth_uri"],
            "token_uri": secrets["token_uri"],
            "auth_provider_x509_cert_url": secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": secrets["client_x509_cert_url"],
        }
    except KeyError as e:
        st.error(f"KeyError: {e}. Make sure your secrets.toml file is correctly configured.")

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

def main():
    st.title("Increment Number App")
    
    # Load Google Sheets credentials
    creds = load_google_credentials()
    client = gspread.service_account_from_dict(creds)
    sheet = client.open("gombszamlalo").sheet1  # Replace with your actual sheet name

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
