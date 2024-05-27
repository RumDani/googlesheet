import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name("your_credentials.json", scope)

# Authorize the client
client = gspread.authorize(credentials)

# Open the Google Sheets spreadsheet
sheet = client.open("Your Google Sheet Name").sheet1

# Function to increment the number in the Google Sheet
def increment_number():
    # Read the current number from the Google Sheet
    current_number = int(sheet.cell(1, 1).value)
    
    # Increment the number
    new_number = current_number + 1
    
    # Update the Google Sheet with the new number
    sheet.update_cell(1, 1, new_number)

# Main Streamlit app
def main():
    st.title("Increment Number App")
    
    # Display the current number from the Google Sheet
    current_number = int(sheet.cell(1, 1).value)
    st.write(f"Current number: {current_number}")
    
    # Button to increment the number
    if st.button("Increment Number"):
        increment_number()
        st.write("Number incremented successfully!")

if __name__ == "__main__":
    main()
