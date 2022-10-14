import wifi_qrcode_generator as qr

qrCode=qr.wifi_qrcode('YourWiFiName',False,'WPA','YourPassword')

qrCode.show()

grCode.save("wifi_qr_code.png")