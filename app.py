import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Function to increment the number in the Google Sheet
def increment_number():
    # Read the data from the Google Sheet
    df = conn.read()
    
    # Check if the DataFrame is empty
    if df.empty:
        # If DataFrame is empty, create a new DataFrame with one row and one column
        df = pd.DataFrame([[0]], columns=["Number"])
    else:
        # If DataFrame is not empty, get the current number
        current_number = df.iloc[0, 0]
        # Increment the number
        new_number = current_number + 1
        # Set the new number in the DataFrame
        df.iloc[0, 0] = new_number
    
    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)
    
    # Update the Google Sheet with the new CSV data
    conn.write(csv_data)

# Main Streamlit app
def main():
    st.title("Increment Number App")
    
    # Display the current number from the Google Sheet
    df = conn.read()
    if df.empty:
        current_number = 0
    else:
        current_number = df.iloc[0, 0]
    st.write(f"Current number: {current_number}")
    
    # Button to increment the number
    if st.button("Increment Number"):
        increment_number()
        st.write("Number incremented successfully!")

if __name__ == "__main__":
    main()
