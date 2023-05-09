import base64
from PIL import Image
from io import BytesIO

# dữ liệu base64 của ảnh
base64_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=="

# giải mã dữ liệu base64 để có được dữ liệu ảnh gốc
image_data = base64.b64decode(base64_data)

# tạo đối tượng hình ảnh từ dữ liệu ảnh
img = Image.open(BytesIO(image_data))

img.show()
# lưu ảnh thành tệp
# img.save("image2.png")