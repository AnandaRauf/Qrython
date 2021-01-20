import qrcode
print("-------------------------------------------------------------------\n")
nameapp = "Qrython"
version = "1.0\n"
devby = "Ananda Rauf Maududi / Retail Tech Source"
devdate = "21 Januari 2021"
print("-------------------------------------------------------------------\n")


# Input gambar / text seperti nomor rekening Bank
# QRcode berfungsi untuk payment gateway bisa di upload di Ovocash maupun pesan rahasia / pesan romantis ke gebetan :v ea
data = "Mohon isi data berupa text maupun file di variable data"
qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
gambar = qr.make_image(fill="black",warnabelakang="white")
gambar.save("Qrython2.png")

