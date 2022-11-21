import qrcode

filename = input("Filename (no extension): ")
qr_text = input("QR Content : ")

image = qrcode.make(qr_text)
file_to_save = open(filename+".png", "wb")
image.save(file_to_save)
file_to_save.close()
print("QR Code generated successfully")
print("QR Code Saved on script folder")

