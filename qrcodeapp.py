import streamlit as st
import qrcode
from PIL import Image
import io


def main():
    st.title("QR Code Generator")

    url = st.text_input("Enter the URL:")
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        pil_image = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL image to bytes
        img_byte_array = io.BytesIO()
        pil_image.save(img_byte_array, format='PNG')

        # Display the image using st.image
        st.image(img_byte_array, caption="Generated QR Code", use_column_width=True)


if __name__ == "__main__":
    main()
