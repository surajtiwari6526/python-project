import qrcode as qr
data=(input("Enter the link:"))
img_name=str(input("Enter the name:"))
img=qr.make(data)
img.save(img_name) 