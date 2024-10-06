import streamlit as st
import segno
from io import BytesIO

# Function to generate QR code
def generate_qr(url, color='black', background='white', error='L', size=1):
    qr = segno.make(url, error=error)
    buffer = BytesIO()
    qr.save(buffer, kind='png', scale=size, dark=color, light=background)
    buffer.seek(0)
    return buffer

# Streamlit application
st.title("Customizable QR Code Generator")

# Step 1: URL Input
url = st.text_input("Enter the URL you want to generate a QR code for:")

if url:
    # Step 2: Customization Option
    customize = st.radio("Do you want to customize the QR code?", ("No", "Yes"))

    color = 'black'
    background = 'white'
    size = 1
    error_correction = 'L'

    if customize == 'Yes':
        # Customization inputs
        color = st.color_picker("Pick the QR code color:", '#000000')
        background = st.color_picker("Pick the background color:", '#FFFFFF')
        size = st.slider("Select the size of the QR code (scale):", 1, 10, 1)
        error_correction = st.selectbox("Select error correction level:", ['L', 'M', 'Q', 'H'])

    # Step 3: QR Code Generation
    if st.button("Generate QR Code"):
        try:
            buffer = generate_qr(url, color, background, error_correction, size)
            st.image(buffer, caption='Generated QR Code')

            # Step 4: Download Option
            st.download_button(label="Download QR Code", data=buffer, file_name="qr_code.png", mime="image/png")
        except Exception as e:
            st.error(f"Failed to generate QR code: {e}")
else:
    st.info("Please enter a valid URL to generate the QR code.")
