import qrcode
from PIL import Image

# Define the data for the QR code
data = "https://github.com/Krishna-KumarGupta?tab=repositories"

# Create a QRCode object
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)

# Add the data to the QRCode object
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QRCode object
img = qr.make_image(fill_color="black", black_color="blue")

# Save the image
img.save("QRCode_GitHub.png")
