import qrcode

qr_text = "TEL:980000000"
img = qrcode.make(qr_text)
type(img)  # qrcode.image.pil.PilImage
img.save("phone.png")
print("QR Image Successfully Saved.")

# Create QR Code To Display Your Name
