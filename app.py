import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Function to increment the number in the Google Sheet
def increment_number():
    # Read the data from the Google Sheet
    df = conn.read()
    
    # Get the current number if DataFrame is not empty
    if not df.empty:
        current_number = df.iloc[0, 0]  # Assuming the number is in the first row, first column
    else:
        current_number = 0  # If DataFrame is empty, set current number to 0
    
    # Increment the number
    new_number = current_number + 1
    
    # Update the Google Sheet with the new number
    df.iloc[0, 0] = new_number
    conn.write(df)

# Main Streamlit app
def main():
    st.title("Increment Number App")
    
    # Display the current number from the Google Sheet
    df = conn.read()
    if not df.empty:
        current_number = df.iloc[0, 0]  # Assuming the number is in the first row, first column
    else:
        current_number = 0  # If DataFrame is empty, set current number to 0
    
    st.write(f"Current number: {current_number}")
    
    # Button to increment the number
    if st.button("Increment Number"):
        increment_number()
        st.write("Number incremented successfully!")

if __name__ == "__main__":
    main()
