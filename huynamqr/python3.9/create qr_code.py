import qrcode
a='due123'
generate_image = qrcode.make(a)
generate_image.save("test.png")