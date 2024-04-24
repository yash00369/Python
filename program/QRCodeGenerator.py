 #QR code generator

import qrcode as qr
img= qr.make("https://www.youtube.com/watch?v=CvZyQQmFqgU")
img.save("Song.png")

# advance QR Code
import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20 ,border=4,)
qr.add_data("https://www.youtube.com/watch?v=CvZyQQmFqgU")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save('OldSong.png')

