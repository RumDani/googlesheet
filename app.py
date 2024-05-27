import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

def main():
    try:
        creds = {
            "type": st.secrets["type"],
            "project_id": st.secrets["project_id"],
            "private_key_id": st.secrets["private_key_id"],
            "private_key": st.secrets["private_key"],
            "client_email": st.secrets["client_email"],
            "client_id": st.secrets["client_id"],
            "auth_uri": st.secrets["auth_uri"],
            "token_uri": st.secrets["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["client_x509_cert_url"]
        }

        st.write("Loaded credentials successfully.")
        credentials = Credentials.from_service_account_info(creds)
        client = gspread.authorize(credentials)

        # Get the spreadsheet URL from secrets
        spreadsheet_url = st.secrets["spreadsheet"]
        st.write(f"Spreadsheet URL: {spreadsheet_url}")

        # Open the Google Sheet using the URL from secrets
        sheet = client.open_by_url(spreadsheet_url)
        worksheet = sheet.get_worksheet(0)

        # Read data from the sheet
        data = worksheet.get_all_records()
        st.write(data)

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
