import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data('https://t.me/AirticketsWebAppBot/qrchecking')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="transparent")

img.save("qrcode.webp")
