import qrcode

def generate_whatsapp_qr(phone_number, message):
    whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(whatsapp_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save('whatsapp_qr.png')


phone_number = '01226714919'  # Enter the phone number
message = 'HELLO'  # Enter the default message
generate_whatsapp_qr(phone_number, message)
