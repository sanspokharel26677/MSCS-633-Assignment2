"""
QR Code Generator - Interactive Version

This Python script allows the user to input a URL and generates a QR code image based on that input.
The image is saved with a user-defined filename, and we include error handling to make it robust.
"""

import qrcode
import datetime

def generate_qr_code(data, filename="qrcode.png"):
    """
    Generates a QR code for the given data and saves it as an image file.

    Parameters:
    data (str): The data to be encoded into the QR code (e.g., a URL)
    filename (str): The desired filename for the output image
    """
    try:
        # Create a QRCode object with specific parameters
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
            box_size=10,  # Size of each square box
            border=4  # Thickness of the border
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to disk
        img.save(filename)

        # Confirm success to the user
        print(f"\n✅ QR Code successfully generated and saved as '{filename}'")

    except Exception as e:
        # Catch and report any errors that occur
        print(f"❌ An error occurred: {e}")

# ---- Main Execution Starts Here ----

if __name__ == "__main__":
    print("=== QR Code Generator ===")

    # Ask the user for the URL they want to convert to QR code
    url_input = input("Enter the URL to encode into a QR code: ").strip()

    # Validate the input (basic check)
    if not url_input.startswith("http"):
        print("⚠️ Warning: The URL doesn't seem to start with 'http'. Make sure it's valid.")

    # Generate a filename using timestamp to keep it unique
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"qr_{timestamp}.png"

    # Ask user for custom filename or use default
    file_input = input(f"Enter filename to save (or press Enter to use '{default_filename}'): ").strip()
    final_filename = file_input if file_input else default_filename

    # Call the function to generate and save QR code
    generate_qr_code(url_input, final_filename)

