# scaled_qrcode.py

import segno

qrcode = segno.make_qr("http://10.120.128.101:3000/")
qrcode.save(
    "scaled_qrcode.png",
    scale=5,
)