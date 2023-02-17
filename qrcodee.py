import qrcode

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QR code
data = "Hello, World!"
nom = "hasnaoui"
prenom = "yahya"
age = "23"
qr.add_data(data)
qr.add_data(nom)
qr.add_data(prenom)
qr.add_data(age)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode1.png")